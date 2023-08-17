#CREDIT BY IZZY
"""
• • • • • • • • • • • • • • • • • • • • • • • •
• Created By hakutakaid@github.com •
• Thanks To Pyroman-Userbot • 
• Thanks To Naya-Pyro •
• Thanks To Zaid-Userbot •
• • • • • • • • • • • • • • • • • • •• • • • • •
"""
import asyncio

from .config import *
import asyncio
from pyrogram import Client
from pyrogram.types import Message 
from pyrogram.errors import FloodWait
from helper import *

@Client.on_message(filters.user(DEVS) & filters.command("cdel", ".") & ~filters.me)
@Client.on_message(filters.me & filters.command("del", cmd))
async def del_user(_, message):
    rep = message.reply_to_message
    await message.delete()
    await rep.delete()


@Client.on_message(filters.me & filters.command("purgeme", cmd))
async def purgeme(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.delete()
    n = message.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return await message.edit_text("Please enter a number")
    n = int(n)
    if n < 1:
        return await message.edit_text("Enter the number of messages you want to delete!")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    if not message_ids:
        return await message.edit_text("Could not find message.")
    to_delete = [message_ids[i : i + 99] for i in range(0, len(message_ids), 99)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
    await message.delete()

@Client.on_message(filters.user(DEVS) & filters.command("cpurge", ".") & ~filters.me)
@Client.on_message(filters.me & filters.command("purge", cmd))
async def purgefunc(client, message):
    await message.delete()
    if not message.reply_to_message:
        return await eor(message, "Membalas pesan untuk dibersihkan.")
    chat_id = message.chat.id
    message_ids = []
    for message_id in range(
        message.reply_to_message.id,
        message.id,
    ):
        message_ids.append(message_id)
        if len(message_ids) == 100:
            await client.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            message_ids = []
    if len(message_ids) > 0:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )