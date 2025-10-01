class TodoApp {
    constructor() {
        this.todoInput = document.getElementById('todoInput');
        this.addBtn = document.getElementById('addBtn');
        this.todoContainer = document.getElementById('todoContainer');
        this.loading = document.getElementById('loading');
        
        this.init();
    }
    
    init() {
        this.addBtn.addEventListener('click', () => this.addTodo());
        this.todoInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.addTodo();
            }
        });
        
        this.loadTodos();
    }
    
    async loadTodos() {
        try {
            this.showLoading(true);
            const response = await fetch('/todos');
            const todos = await response.json();
            this.renderTodos(todos);
        } catch (error) {
            console.error('할일 목록 로드 실패:', error);
            this.showError('할일 목록을 불러올 수 없습니다.');
        } finally {
            this.showLoading(false);
        }
    }
    
    async addTodo() {
        const title = this.todoInput.value.trim();
        if (!title) return;
        
        try {
            const response = await fetch('/todos', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title })
            });
            
            if (response.ok) {
                this.todoInput.value = '';
                this.loadTodos();
            } else {
                throw new Error('할일 추가 실패');
            }
        } catch (error) {
            console.error('할일 추가 실패:', error);
            alert('할일을 추가할 수 없습니다.');
        }
    }
    
    async toggleTodo(id) {
        try {
            const response = await fetch(`/todos/${id}`, {
                method: 'PATCH'
            });
            
            if (response.ok) {
                this.loadTodos();
            } else {
                throw new Error('할일 상태 변경 실패');
            }
        } catch (error) {
            console.error('할일 상태 변경 실패:', error);
            alert('할일 상태를 변경할 수 없습니다.');
        }
    }
    
    async deleteTodo(id) {
        if (!confirm('정말로 이 할일을 삭제하시겠습니까?')) {
            return;
        }
        
        try {
            const response = await fetch(`/todos/${id}`, {
                method: 'DELETE'
            });
            
            if (response.ok) {
                this.loadTodos();
            } else {
                throw new Error('할일 삭제 실패');
            }
        } catch (error) {
            console.error('할일 삭제 실패:', error);
            alert('할일을 삭제할 수 없습니다.');
        }
    }
    
    renderTodos(todos) {
        if (todos.length === 0) {
            this.todoContainer.innerHTML = `
                <div class="empty-state">
                    <p>아직 할일이 없습니다.</p>
                    <p>위에서 새로운 할일을 추가해보세요! 🚀</p>
                </div>
            `;
            return;
        }
        
        this.todoContainer.innerHTML = todos.map(todo => `
            <div class="todo-item ${todo.completed ? 'completed' : ''}">
                <input 
                    type="checkbox" 
                    class="todo-checkbox" 
                    ${todo.completed ? 'checked' : ''}
                    onchange="app.toggleTodo('${todo._id}')"
                />
                <span class="todo-text">${this.escapeHtml(todo.title)}</span>
                <button 
                    class="delete-btn" 
                    onclick="app.deleteTodo('${todo._id}')"
                >
                    삭제
                </button>
            </div>
        `).join('');
    }
    
    showLoading(show) {
        this.loading.style.display = show ? 'block' : 'none';
    }
    
    showError(message) {
        this.todoContainer.innerHTML = `
            <div class="empty-state">
                <p>❌ ${message}</p>
            </div>
        `;
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// 앱 초기화
const app = new TodoApp();