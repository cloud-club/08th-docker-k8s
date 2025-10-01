const express = require('express');
const mongoose = require('mongoose');
const redis = require('redis');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// 정적 파일 서빙 (프론트엔드)
app.use(express.static('public'));

// MongoDB 연결
const connectMongoDB = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI || 'mongodb://mongo:27017/todoapp');
    console.log('MongoDB 연결 성공');
  } catch (error) {
    console.error('MongoDB 연결 실패:', error);
    process.exit(1);
  }
};

// Redis 연결
const connectRedis = async () => {
  try {
    const client = redis.createClient({
      url: process.env.REDIS_URL || 'redis://redis:6379'
    });
    await client.connect();
    console.log('Redis 연결 성공');
    return client;
  } catch (error) {
    console.error('Redis 연결 실패:', error);
    return null;
  }
};

// Todo 스키마
const todoSchema = new mongoose.Schema({
  title: { type: String, required: true },
  completed: { type: Boolean, default: false },
  createdAt: { type: Date, default: Date.now }
});

const Todo = mongoose.model('Todo', todoSchema);

let redisClient;

// 헬스체크 엔드포인트
app.get('/health', (req, res) => {
  res.json({
    status: 'OK',
    timestamp: new Date().toISOString(),
    mongodb: mongoose.connection.readyState === 1 ? 'connected' : 'disconnected',
    redis: redisClient ? 'connected' : 'disconnected'
  });
});

// 모든 할일 조회
app.get('/todos', async (req, res) => {
  try {
    // Redis 캐시 확인
    if (redisClient) {
      const cached = await redisClient.get('todos');
      if (cached) {
        return res.json(JSON.parse(cached));
      }
    }

    const todos = await Todo.find().sort({ createdAt: -1 });

    // Redis에 캐시 저장 (30초)
    if (redisClient) {
      await redisClient.setEx('todos', 30, JSON.stringify(todos));
    }

    res.json(todos);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// 할일 생성
app.post('/todos', async (req, res) => {
  try {
    const { title } = req.body;
    if (!title) {
      return res.status(400).json({ error: '제목이 필요합니다' });
    }

    const todo = new Todo({ title });
    await todo.save();

    // 캐시 무효화
    if (redisClient) {
      await redisClient.del('todos');
    }

    res.status(201).json(todo);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// 할일 완료/미완료 토글
app.patch('/todos/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const todo = await Todo.findById(id);

    if (!todo) {
      return res.status(404).json({ error: '할일을 찾을 수 없습니다' });
    }

    todo.completed = !todo.completed;
    await todo.save();

    // 캐시 무효화
    if (redisClient) {
      await redisClient.del('todos');
    }

    res.json(todo);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// 할일 삭제
app.delete('/todos/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const todo = await Todo.findByIdAndDelete(id);

    if (!todo) {
      return res.status(404).json({ error: '할일을 찾을 수 없습니다' });
    }

    // 캐시 무효화
    if (redisClient) {
      await redisClient.del('todos');
    }

    res.json({ message: '할일이 삭제되었습니다' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// 서버 시작
const startServer = async () => {
  await connectMongoDB();
  redisClient = await connectRedis();

  app.listen(PORT, () => {
    console.log(`서버가 포트 ${PORT}에서 실행 중입니다`);
  });
};

startServer();