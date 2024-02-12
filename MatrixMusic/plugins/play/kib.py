import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

#كسمك تحياتي😂
REPLY_MESSAGE = "**🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️**\n**⤵️︙ اليـكـ كيب الاعضاء الخاص بسورس البوب**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("المطور"),                   
             ("السورس")

          ],
          [
             ("ذكاء الاصطناعي"),
              ("افلام")
          ],
          [
             ("لو خيروك"),
             ("كت تويت") 
          ],
          [
             ("اذكار"),
             ("صراحه") 
          ],
          [
             ("افاتار شباب"),
             ("افاتار بنات") 
          ],
          [
             ("استوري"),
              ("متحركه")
          ],
          [
             ("قران"),
              ("نقشبندي")
          ],
          [
              ("عبدالباسط"),
              ("تلاوات")
          ],
          [
             ("غنيلي"),
             ("سوال")         
          ],
          [
             ("الالعاب"),
             ("انمي")
          ],
          [
             ("اقتباس"),
             ("هيدرات")
          ],
          [           
        ("❎ ¦ حذف الكيبورد")
    ]
]

@app.on_message(filters.command(["/alpop"], "") & filters.private & ~BANNED_USERS)
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

