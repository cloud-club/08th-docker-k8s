from flask import Flask

app = Flask(__name__)

@app.route('/greeting')
def greeting():
    return "안녕하세요. 클둥이 여러분"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
