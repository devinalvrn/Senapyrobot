from pyrogram.types import InlineKeyboardButton
from main import CMD_HELP
from module.config import cmd
class Data:

    text_help_menu = (
        f"**Menu Inline Sena**\n**Prefixes:** `{cmd}"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Reopen", callback_data="reopen")]]
