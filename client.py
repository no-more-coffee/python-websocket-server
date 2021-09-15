import asyncio

import websockets
from websockets.legacy.client import WebSocketClientProtocol

from settings import WS_URL


async def consumer_handler(websocket: WebSocketClientProtocol):
    async for message in websocket:
        print(message)


async def consume(ws_url: str):
    print("consume:", ws_url)
    async with websockets.connect(ws_url) as websocket:
        await consumer_handler(websocket)


async def produce(message: str, ws_url: str):
    async with websockets.connect(ws_url) as websocket:
        await websocket.send(message)
        print(await websocket.recv())


def send_test_message():
    asyncio.run(produce(message='hi', ws_url=WS_URL))


if __name__ == '__main__':
    asyncio.run(consume(WS_URL))
