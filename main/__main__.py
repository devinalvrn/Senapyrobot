#created By Hakutakaid
from main import *
async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("module" + all_module)
        print(f"🏠 Berhasil Mengimpor {all_module} 🀄")
    for cli in clients:
        await cli.start()
        ex = await cli.get_me()
        LOGGER("✓").info(f"🏠 Bot Berjalan Di {ex.first_name} | {ex.id} ")
        ids.append(ex.id)
        await cli.send_message("me", f"`🇮🇩 Sena Telah Di Aktifkan` ...\n\n**🀄 Pyrogram Version** : `{vp}`\n\n**🏠 Created By :** {ex.mention}")
    try:
        await client.join_chat("asukamuyaas")
    except BaseException as e:
        LOGGER("Info").warning(f"{e}") 
    await idle()
    await session.close()
for bot in clients:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
