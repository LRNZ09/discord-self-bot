import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(verbose=True)

TOKEN = os.getenv('TOKEN', '')
