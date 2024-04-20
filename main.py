from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode="aiohttp", cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

async def manager():
    pass

@sio.event
async def connect(sid, auth, environ):
    print(sid)

async def init_app():
    sio.start_background_task(manager)
    return app

if __name__ == '__main__':
    web.run_app(init_app(), port=2700)