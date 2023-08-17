"""
• • • • • • • • • • • • • • • • • • • • • • • •
• Created By hakutakaid@github.com •
• Thanks To Pyroman-Userbot • 
• Thanks To Naya-Pyro •
• Thanks To Zaid-Userbot •
• • • • • • • • • • • • • • • • • • •• • • • • •
"""
import os
import asyncio
from dotenv import load_dotenv
from pyromek import *

load_dotenv("gcast.env")

BLACKLIST_GCAST = os.getenv("BLACKLIST_GCAST", "")
if BLACKLIST_GCAST:
    BLACKLIST_GCAST = BLACKLIST_GCAST.split(" ")
else:
    BLACKLIST_GCAST = []

@Client.on_message(filters.command("addbl", prefixes=".") & filters.me)
async def add_blacklist(client: Client, message: Message):
    await message.edit_text("`Processing...`")
    chat_id = message.chat.id
    if str(chat_id) not in BLACKLIST_GCAST:
        BLACKLIST_GCAST.append(str(chat_id))
        blacklistgrup = " ".join(BLACKLIST_GCAST)
        await message.edit_text(
            f"**Berhasil Menambahkan `{chat_id}` **Ke Daftar Blacklist Gcast.**\n\nKetik `.restart` Untuk Menerapkan Perubahan."
        )
        await asyncio.sleep(5)
        await message.delete()
        try:
            dotenv_path = "gcast.env"  # Ganti dengan path ke file .env Anda jika perlu
            with open(dotenv_path, "w") as file:  # Mengubah mode file menjadi "w" untuk menulis ulang
                file.write(f"BLACKLIST_GCAST=\"{' '.join(BLACKLIST_GCAST)}\"")
            # restart()  # Tidak ada definisi restart() dalam kode yang Anda berikan
        except Exception as e:
            await message.edit(str(e))
    else:
        await message.edit_text("Chat ID Ini Sudah Ada Dalam Daftar Blacklist Gcast.")
