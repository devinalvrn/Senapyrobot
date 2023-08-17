import os
from dotenv import load_dotenv, set_key, unset_key
from pyromek import *
import subprocess

load_dotenv("jembit.env")

def hapus_var(env_file, var_name):
    try:
        unset_key(env_file, var_name)
        return True
    except KeyError:
        return False


@Client.on_message(filters.me & filters.command("tambah", prefixes="."))
async def tambah_var(_, message: Message):
    command_parts = message.text.split("=", 1)
    if len(command_parts) != 2:
        await message.reply("Invalid format. Usage: `.tambah VAR_NAME=VALUE`")
        return

    var_name, var_value = command_parts
    var_name = var_name.strip(".tambah ").strip()
    var_value = var_value.strip()

    set_key("jembit.env", var_name, var_value)
    await message.reply(f"Variable '{var_name}' added to .env successfully.")


@Client.on_message(filters.me & filters.command("hapus", prefixes="."))
def hapus_var_cmd(_, message: Message):
    try:
        var_name = message.text.split(" ", 1)[1].strip()
        if hapus_var("jembit.env", var_name):
            message.reply(f"Variable '{var_name}' removed from .env successfully.")
        else:
            message.reply(f"Variable '{var_name}' not found in .env.")
    except IndexError:
        message.reply("Invalid format. Usage: `.hapus VAR_NAME`")

@Client.on_message(filters.me & filters.command("restart", prefixes=","))
def restart_system(_, message: Message):
    message.reply("`restarting....`")
    subprocess.run(["bash", "start"])
    load_dotenv("jembit.env")  # Reload the updated environment variables after restart
    message.reply("System restarted.")

@Client.on_message(filters.me & filters.command("cek", prefixes="."))
def cek_vars(_, message: Message):
    variables = os.environ.keys()
    session_vars = [var for var in variables if var.startswith("SESSION")]
    message.reply(f"Session variables in .env: {', '.join(session_vars)}")
