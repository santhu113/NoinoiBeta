from NoinoiRobot import Stark
from telethon import events, Button

PM_START_TEXT = """
**Hey {}** [.](https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg)
𝐄𝐲 𝐍𝐞𝐧𝐮 𝐆𝐫𝐨𝐮𝐩 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐛𝐨𝐭 𝐧𝐢 𝐚𝐝𝐯𝐚𝐧𝐜𝐞 𝐛𝐨𝐭 𝐧𝐢 😍 𝐧𝐚𝐧𝐮 𝐦𝐞 𝐠𝐫𝐨𝐮𝐩 𝐥𝐨 𝐚𝐝𝐝 𝐜𝐡𝐞𝐬𝐮 𝐤𝐨𝐧𝐝𝐢. 
┏━━━━━━━━━━━━━━━━━┓
┣» 𝐚𝐝𝐯𝐚𝐧𝐜𝐞 𝐠𝐫𝐨𝐮𝐩 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐛𝐨𝐭. 
┣» 𝐩𝐨𝐰𝐞𝐫 𝐟𝐮𝐥𝐥 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭.
┣» 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬.
┣» 𝐓𝐡𝐢𝐬 𝐛𝐨𝐭 𝐦𝐚𝐝𝐞 𝐨𝐧𝐥𝐲 𝐟𝐨𝐫 𝐠𝐫𝐨𝐮𝐩𝐬 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐩𝐮𝐫𝐩𝐨𝐬𝐞. 
┣» 𝐃𝐄𝐏𝐋𝐎𝐘 𝐁𝐘 💞[𝚂𝙰𝙽𝚃𝙷𝙾𝚂𝙷 ❤](https://t.me/santhu_music_bot)
┗━━━━━━━━━━━━━━━━━┛
[𝙽𝙴𝚃𝚆𝙾𝚁𝙺 ❤️](https://t.me/santhuvc

**𝐞𝐝𝐢𝐧𝐚 𝐡𝐞𝐥𝐩 𝐤𝐨𝐬𝐚𝐦 𝐤𝐢𝐧𝐝𝐡𝐚 𝐜𝐥𝐢𝐜𝐤 𝐜𝐡𝐞𝐲𝐚𝐧𝐝𝐢!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help & Commands", data="help")],
        [Button.url("OWNER 😁", "https://t.me/santhu_music_bot")]])
       return

    if event.is_group:
       await event.reply("**Nenu unna ✨**")
       return
