import os
from importlib import resources

"""
Environment variables have highest priorities.
Then `local.env` definitions.
"""

try:
    from dotenv import load_dotenv

    with resources.path('envs', 'local.env') as p:
        print(f'Settings file `local.env` is read: {load_dotenv(p)}')
except (FileNotFoundError, ModuleNotFoundError):
    pass

WS_HOST = os.environ.get('WS_HOST', 'localhost')
WS_PORT = os.environ.get('WS_PORT', 8765)
WS_URL = f'ws://{WS_HOST}:{WS_PORT}'
