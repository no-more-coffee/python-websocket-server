import asyncio
import os
import signal

import websockets
from websockets.legacy.server import WebSocketServerProtocol

from settings import WS_PORT, WS_HOST

SUPERVISOR_PROCESS_NAME = os.environ.get('SUPERVISOR_PROCESS_NAME')
print("SUPERVISOR_PROCESS_NAME:", SUPERVISOR_PROCESS_NAME)


class Server:
    clients = set()

    async def handler(self, ws: WebSocketServerProtocol, uri: str) -> None:
        print('Starting')
        self.clients.add(ws)
        try:
            await self.distribute(ws)
        finally:
            print('Stopping')
            self.clients.remove(ws)

    async def distribute(self, ws: WebSocketServerProtocol) -> None:
        async for message in ws:
            websockets.broadcast(self.clients, message)


async def server():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    # async with websockets.unix_serve(Server().handler, path=f"{SUPERVISOR_PROCESS_NAME}.sock"):
    #     await stop

    print(WS_HOST, WS_PORT)
    async with websockets.serve(Server().handler, WS_HOST, WS_PORT):
        await stop
    # async with websockets.serve(Server().handler, host=WS_HOST, port=WS_PORT, reuse_port=True):
    #     await stop


if __name__ == '__main__':
    asyncio.run(server())
