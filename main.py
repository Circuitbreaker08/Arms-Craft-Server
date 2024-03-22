import socketio
import eventlet
import threading

sio = socketio.Server(logger=False, async_mode='eventlet')
app = socketio.WSGIApp(sio)

def server():
    eventlet.wsgi.server(eventlet.listen(("", 2700)), app)

threading.Thread(target=server).start()