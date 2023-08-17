import os
from pyrogram import Client, filters
from py_trans import Async_PyTranslator
from helper.utils import get_arg
from .config import cmd

@Client.on_message(filters.command("tr", cmd) & filters.me)
async def pytrans_tr(_, message):
    tr_msg = await message.edit_text("`Processing...`")
    r_msg = message.reply_to_message
    args = get_arg(message)

    if not args:
        return await tr_msg.edit_text("`Please provide arguments for translation!`")

    if r_msg and r_msg.text:
        to_tr = r_msg.text
    else:
        return await tr_msg.edit_text("`Reply to a message that contains text!`")

    # Split the arguments into destination language and translation engine (if provided)
    sp_args = args.split(" ")
    dest_lang = sp_args[0]
    tr_engine = sp_args[1] if len(sp_args) > 1 else "google"

    # Translate the text
    py_trans = Async_PyTranslator(provider=tr_engine)
    translation = await py_trans.translate(to_tr, dest_lang)

    # Parse the translation message
    if translation["status"] == "success":
        tred_txt = f"""
        **Translation Engine**: `{translation["engine"]}`
        **Translated to:** `{translation["dest_lang"]}`
        **Translation:**
        `{translation["translation"]}`
        """
        if len(tred_txt) > 4096:
            await tr_msg.edit_text("`Wah!! Translated Text So Long Tho!, Give me a minute, I'm sending it as a file!`")
            tr_txt_file = open("translated.txt", "w+")
            tr_txt_file.write(tred_txt)
            tr_txt_file.close()
            await tr_msg.reply_document("translated.txt")
            os.remove("translated.txt")
            await tr_msg.delete()
        else:
            await tr_msg.edit_text(tred_txt)
