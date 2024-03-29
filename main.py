import socketio
import uvicorn
import os

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=["*"], logger=True)
sio.instrument(auth=
    {
    'username': 'admin',
    'password': os.environ['ADMIN_PASSWORD'],
})
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, auth, environ):
    print(sid)

uvicorn.run(app, host="0.0.0.0", port=2700)