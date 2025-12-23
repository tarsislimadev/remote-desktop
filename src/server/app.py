from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

connections = []

@app.route('/')
def main():
  return { 'remote-desktop': 'v0.1.0' }

@socketio.on('*')
def any_event(event, sid, data):
  print(f'any event: {sid}; data: {data}')

@socketio.on('connect')
def connect(sid, environ, auth):
  connections.append(sid)
  print('connect ', sid, auth)

@socketio.on('disconnect')
def disconnect(sid, reason):
  connections.remove(sid)
  print('disconnect ', sid, reason)
