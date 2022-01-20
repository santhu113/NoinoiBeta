from NoinoiRobot import Stark
from telethon import events, Button
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

PM_START_TEXT = """
**Hey {}** [.](https://telegra.ph/file/622a49ad89f050473b18a.jpg)
I am simple manager robot whos help to you for manage your group

**Click the below help button for the open help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [InlineKeyboardButton(
            text="️Add Kazuko to your group", url="t.me/KazukoRobot?startgroup=true",),],
        [Button.inline("Help & Commands", data="help")],
        [Button.url("Source Code", "GitHub.com/HYKO-XD/NOINOIBETA")]])
       return

    if event.is_group:
       await event.reply("**I AM ALIVE ✨**")
       return
