import os
from pyrogram.types import KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo,ReplyKeyboardMarkup

#get from https://my.telegram.org/auth
API_ID:int =(os.environ.get("API_ID",27498647))
API_HASH:str = os.environ.get("API_HASH", "f7764b70861584bca951040781111bfb")
BOT_TOKEN:str = os.environ.get("BOT_TOKEN", "6770406589:AAFzxvc7IwyoPGAynm4oJ5QCJZg1_TAktOA")


REFER_BONUS=int(1)
NEW_USER_BONUS=int(1)

#username without @
UPDATE_CHNL:str = os.environ.get("UPDATE_CHNL", "Crypto_Loot_AK")
SUPPORT_GRP:str = os.environ.get("SUPPORT_GRP", "Looters_Money_Trick")
BOT_USERNAME:str = os.environ.get("BOT_USERNAME", "Earn_Money_UPI_Bot")

#get it from @username_to_id_bot this bot 

log_channel = int(os.environ.get("LOG_CHANNEL", "-1001933029304"))
OWNER_ID=int(os.environ.get("OWNER_ID",1807927334))


# search on youtube "how to create mongodburl""

MONGO_DB_URI:str = os.environ.get(
    "MONGO_DB_URI",
    "mongodb+srv://Storm72:khan7860@cluster0.udehz9j.mongodb.net/?retryWrites=true&w=majority")
	


INR_IMG="https://graph.org/file/591e034f3ebaca25e0692.jpg"
START_IMG= "https://graph.org/file/877838e68ea8e3099f343.jpg"
start_img2="https://graph.org/file/e1f08dea685a9051b264c.jpg"
photo="https://graph.org/file/8e2df166f47509590c88e.jpg"
deposit_IMG="https://graph.org/file/d46f6efe8fe5c991491ed.jpg"



                


main_button = ReplyKeyboardMarkup(
        [
            [KeyboardButton("🪪 ᴍʏ ᴘʀᴏꜰɪʟᴇ"), KeyboardButton("🤑 ꜰʀᴇᴇ ᴍᴏɴᴇʏ 🤑")],
            [KeyboardButton("⚡️ ᴡɪᴛʜᴅʀᴀᴡᴀʟ ⚡️")], 
            [KeyboardButton("ᴄʀᴇᴀᴛᴏʀ 😉", web_app=WebAppInfo(url="https://t.me/Ak74400"))]
        ],
        resize_keyboard=True
    )

all_platform = ReplyKeyboardMarkup(
        [
        [KeyboardButton("❤️‍🔥 ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ"), KeyboardButton("ᴅɪᴄᴇ ɢᴀᴍᴇ 🥳")],
            [KeyboardButton("⚽️ ꜰᴏᴏᴛʙᴀʟʟ "), KeyboardButton("ᴄᴏʟᴏʀ ᴘʀᴇᴅɪᴄᴛɪᴏɴ 🎱")],
            [ KeyboardButton("〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄")]
        ],
        resize_keyboard=True
    )

