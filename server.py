import asyncio

import websockets


async def echo(websocket, path):
    print('Path: ', path)
    async for message in websocket:
        print('Message: ', message)
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(main())
