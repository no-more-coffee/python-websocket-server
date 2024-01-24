import asyncio
import signal

import websockets

from settings import CURRENT_CONFIG


class Server:
    clients = set()

    async def handler(self, ws: websockets.WebSocketServerProtocol, uri: str) -> None:
        print('Starting')
        self.clients.add(ws)
        try:
            await self.distribute(ws)
        finally:
            print('Stopping')
            self.clients.remove(ws)

    async def distribute(self, ws: websockets.WebSocketServerProtocol) -> None:
        async for message in ws:
            websockets.broadcast(self.clients, message)


async def server():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    print('Current config:', CURRENT_CONFIG)
    async with websockets.serve(Server().handler, **CURRENT_CONFIG):
        await stop


if __name__ == '__main__':
    asyncio.run(server())
