import asyncio

import websockets


async def send_hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        print('Answer: ', await websocket.recv())

if __name__ == '__main__':
    asyncio.run(send_hello())
