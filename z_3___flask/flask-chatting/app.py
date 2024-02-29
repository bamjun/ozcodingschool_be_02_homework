from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#라우팅
@app.route('/')
def index():
    return render_template('index.html')


def msg_received(methods=['GET', 'POST']):
    print("callback : msg received")
    # db 커넥션 -> save

#소켓 연결 (클라이언트 ~ 서버)
@socketio.on('my event')
def handle_chat_event(json, methods=['GET', 'POST']):
    print(f'데이터수신 완료 : {json}')
    socketio.emit('my response', json, callback=msg_received)
    


if __name__ == '__main__':
    socketio.run(app, debug=True)