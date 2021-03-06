#    Lion - UserBot
#    Copyright (C) 2020 Lion

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon.tl.types import Channel

from Lion import *
from Lion import ALIVE_NAME, bot, lionver
from Lion.LionConfig import Config, Var

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

LIONUSER = str(ALIVE_NAME) if ALIVE_NAME else "@discuss_group_cs"

lion = f"π·πΎππ» ππ΄πππΈπΎπ½: {lionver}\n"
lion += f"π»πΎπΆ πΆππΎππΏ: {log}\n"
lion += f"πΌπ π°πππΈπππ°π½π π±πΎπ: {bots}\n"
lion += f"π»ππ³πΈπ°: {lyd}\n"
lion += f"πππ³πΎ πππ΄π: {sudo}\n"
lion += f"πΏπΌ ππ΄π²πππΈππ: {pm}\n"
lion += f"\nππΈππΈπ @discuss_group_cs π΅πΎπ π°πππΈπππ°π½π.\n"
lionstats = f"{lion}"

LION_NAME = bot.me.first_name
OWNER_ID = bot.me.id
omkvro = bot.uid
# count total number of groups


async def lion_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
