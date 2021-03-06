import glob
from Lion import bot
from sys import argv
from telethon import TelegramClient
from Lion.LionConfig import Var
from Lion.utils import load_module, start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from Lion import CMD_HNDLR

LION = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(LION, f"**π·πΎππ» π±πΎπ πΈπ π³π΄πΏπ»πΎππ΄π³.\nππ΄π½π³** `{CMD_HNDLR}alive` **ππΎ ππ΄π΄ π±πΎπ πΈπ ππΎππΊπΈπ½πΆ πΎπ π½πΎπ.\n\nAdd** @{BOTNAME} **π°π³π³ ππΎ ππ·πΈπ πΈπ½ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ π·πΈπΌ π°π³πΌπΈπ½ π΅πΎπ π΄π½π°π±π»πΈπ½πΆ π°π»π» ππ·π΄ π΅π΄π°ππππ΄π πΎπ΅ π·πΎππ» π±πΎπ**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'Lion/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Lion has been deployed! ")

print("Setting up TGBot")
path = "Lion/plugins/mybot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "Lion/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    αα§αα X Κα΄s Κα΄α΄Ι΄ α΄α΄α΄Κα΄Κα΄α΄, α΄α΄ α΄ ΙͺsΙͺα΄ @discuss_group_cs !!
                    ΚΙͺα΄Ι΄ α΄ α΄Κ: V2.2
                    Β©Tα΄α΄α΄ ΚΙͺα΄Ι΄
                ----------------------------------------------------------------------
"""
)
bot.loop.run_until_complete(startup_log_all_done())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
