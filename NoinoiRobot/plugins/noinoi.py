#Noinoi personal plugin soon..... 

from NoinoiRobot import Stark

from telethon import events, Button

NOINOI_ZOOM = """

**{}** [.](https://telegra.ph/file/1c5a4d918e34d18f031ab.jpg)

** Noinoi zoom meeting on group video chats 💬**

** • /join - [ zoom meating id ] **

** • /new -  [ to make new meeting ] **
"""

@Stark.on(events.NewMessage(pattern="^[?!/]zoom$"))

async def start(event):

    if event.is_private:

       await event.reply(NOINOI_ZOOM.format(event.sender.first_name), buttons=[

        [Button.inline("Share ➡️", data="help")],

        [Button.url("Login 🔒", "https://zoom.us/signin?_x_zm_rtaid=oB5VpOlwR5-MFctcvBb7CA.1642674678628.b976594d906f86c6a5cf5e3d3cb3ec7f&_x_zm_rhtaid=124")]])

       return

    if event.is_group:

       await event.reply("**Please type in pm @NOINOI_BOT **")

       return
