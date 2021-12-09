import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DB_PATH = BASE_DIR.joinpath('data', 'DO.pkl')

version_info = json.load(BASE_DIR.joinpath('version', 'version.json').open())
__version__ = version_info['version']
