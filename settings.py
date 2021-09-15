import os

WS_HOST = os.environ.get('WS_HOST', 'localhost')
WS_PORT = os.environ.get('WS_PORT', 8765)
WS_URL = f'ws://{WS_HOST}:{WS_PORT}'
