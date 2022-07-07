import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, ALIVE_PIC, OWNER_ID
from TbhXSpam.plugins.help import *


UstaD_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/37a99a9688f89b847a252.jpg"

UstaD_Button = [
        [
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/THE_BROTHERHOOD_COUNCIL")
        ],
        [
        Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")
        ]
        ]
               
UstaDX_Button = [
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/THE_BROTHERHOOD_COUNCIL"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/SCHOOL_WALLI_MASTII")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/Popay-ckl/TBH-BOTFATHER-SPAMDeploy")
        ]
        ]
        
        
#USERS 


@UstaD.on(events.NewMessage(pattern="/start"))
@UstaD2.on(events.NewMessage(pattern="/start"))
@UstaD3.on(events.NewMessage(pattern="/start"))
@UstaD4.on(events.NewMessage(pattern="/start"))
@UstaD5.on(events.NewMessage(pattern="/start"))
@UstaD6.on(events.NewMessage(pattern="/start"))
@UstaD7.on(events.NewMessage(pattern="/start"))
@UstaD7.on(events.NewMessage(pattern="/start"))
@UstaD8.on(events.NewMessage(pattern="/start"))
@UstaD9.on(events.NewMessage(pattern="/start"))
@UstaD10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       UstaDBot = await event.client.get_me()
       bot_name = UstaDBot.first_name
       bot_id = UstaDBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       Popay = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From The Button Given Below.** \n\n**Powered By : [𝙏𝙗𝙝 𝙓 𝙎𝙥𝙖𝙢](https://t.me/SCHOOL_WALLI_MASTII)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(Popay,
                  MIG_IMG,
                  caption=ownermsg, 
                  buttons=Mig_Button)
       else:
            await event.client.send_file(Popay,
                  UstaD_IMG,
                  caption=usermsg, 
                  buttons=TbhX_Button)
                
