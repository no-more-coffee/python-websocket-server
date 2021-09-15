from importlib import resources

from dotenv import load_dotenv

"""
Environment variables have highest priorities.
Then `local.env` definitions.
"""

try:
    with resources.path('backend.envs', 'local.env') as p:
        print(f'Settings file `local.env` is read: {load_dotenv(p)}')
except FileNotFoundError:
    pass

# noinspection PyUnresolvedReferences
from settings import *
