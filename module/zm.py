from pyrogram import Client, filters
from .config import cmd
from helper.basic import *

@Client.on_message(filters.command("zombies", cmd) & filters.me)
async def _(client, message):
    chat_id = message.chat.id
    deleted_users = []
    m = await eor(
        message, "<code>Sedang Mencari Akun Terhapus...</code>"
    )

    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if deleted_users:
        banned_users = 0
        for deleted_user in deleted_users:
            try:
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
            banned_users += 1
        await m.edit(
            f"<b>Berhasil Mengeluarkan {banned_users} Akun Yang Terhapus..</b>"
        )
    else:
        await m.edit("<b>Tidak Menemukan Akun Yang Terhapus</b>")
