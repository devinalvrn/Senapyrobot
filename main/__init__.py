from . import *
import asyncio
import importlib
from pyromek import *
from pyrogram import Client, idle
from module.config import *
from module import ALL_MODULES
#from pyromod import listen
from pyrogram import __version__ as vp
from platform import python_version
import time
from datetime import datetime
from pytgcalls import GroupCallFactory
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
clients = []
ids = []
CMD_HELP = {}
CMD_HELP = {}
LOOP = asyncio.get_event_loop_policy()
event_loop = LOOP.get_event_loop()
asyncio.set_event_loop(event_loop)
aiosession = ClientSession()
scheduler = AsyncIOScheduler()
#UP TO 100 CLIENT SESSION
for i in range(1, 101):
    session_var = globals().get(f"SESSION{i}")
    if session_var:
        print(f"🏠 Client {i} Di Temukan...\n Sedang Memulai Sena🀄\n")
        client = Client(
            f"haku{i}",
            api_hash=API_HASH,
            api_id=API_ID,
            session_string=session_var,
            in_memory=True,
            plugins=dict(root="module")
        )
        clients.append(client)
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)
logging.basicConfig(level=logging.INFO)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


loop = asyncio.get_event_loop()

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="module/bot"),
    in_memory=True,
)