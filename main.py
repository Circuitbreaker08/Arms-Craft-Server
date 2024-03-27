import socketio
import eventlet
import threading

sio = socketio.Server(logger=False, async_mode='eventlet', cors_allowed_origins="*")
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ, auth):
    #print(sid)
    pass

def server():
    eventlet.wsgi.server(eventlet.listen(("", 2700)), app)

threading.Thread(target=server).start()