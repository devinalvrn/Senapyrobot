"""
• • • • • • • • • • • • • • • • • • • • • • • •
• Created By hakutakaid@github.com •
• Thanks To Pyroman-Userbot • 
• Thanks To Naya-Pyro •
• Thanks To Zaid-Userbot •
• • • • • • • • • • • • • • • • • • •• • • • • •
"""
from .basic import *
from .misc import *
from .utility import *
from .PyroHelpers import *
from .utils import *
from .notes import *
from .pmpermitdb import *


import motor.motor_asyncio
from pyrogram import *
from module.config import MONGO_URL


cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

dbb = cli.program
notesdb = cli.notes
logdb = cli.gruplog