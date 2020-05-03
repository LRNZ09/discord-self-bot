import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(verbose=True)


CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))
TOKEN = os.getenv('TOKEN', '')
