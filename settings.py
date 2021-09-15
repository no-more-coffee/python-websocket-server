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

PORT_CONFIG = 'port'
SOCK_CONFIG = 'sock'
WS_CONFIG = os.environ.get('WS_CONFIG', PORT_CONFIG)
WS_HOST = os.environ.get('WS_HOST', 'localhost')
WS_PORT = os.environ.get('WS_PORT', 8765)
WS_URL = f'ws://{WS_HOST}:{WS_PORT}'
WS_REUSE_PORT = os.environ.get('WS_REUSE_PORT', 'FALSE').upper() == 'TRUE'
SUPERVISOR_PROCESS_NAME = os.environ.get('SUPERVISOR_PROCESS_NAME')
WS_PATH = f"{SUPERVISOR_PROCESS_NAME}.sock"

CONFIGS = {
    PORT_CONFIG: {
        'host': WS_HOST,
        'port': WS_PORT,
        'reuse_port': WS_REUSE_PORT,
    },
    SOCK_CONFIG: {
        'path': WS_PATH,
        'unix': True,
    },
}

CURRENT_CONFIG = CONFIGS[WS_CONFIG]
