import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from MatrixMusic import app


# Replace the following line with your actual OWNER_ID
OWNER_ID = 956893993

@app.on_message(filters.command(['بوت'], prefixes=""))
async def Italymusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك🏅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 956893993:
             rank = "**يالهوي ده مالك السورس بنفسو ياعيال في البار😱⚡️**"
        elif user_id == OWNER_ID:
             rank = "مـالك الـبوت العظمه 🫡⚡️"
        elif member.status == 'creator':
             rank = "**مـالك الـبـار 🫡⚡️**"
        elif member.status == 'administrator':
             rank = "**مـشـرف الـبـار🫡⚡️**"
        else:
             rank = "**لاسف انت عضو فقير🥺💔**"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
    
    await message.reply_text(f"أرسل لي صورة ملف تعريفية حتى أستطيع عرضها مع رسالتك.")

    # Wait for the user to send their profile photo
    photo_message = await client.listen(filters.photo & filters.private)

    # Get the photo file id from the received photo message
    photo_file_id = photo_message.photo.file_id

    # Reply to the user with their profile photo
    await message.reply_photo(photo_file_id, caption=f"""**نعم حبيبي :** {italy} 🥰❤\n**انا اسمي القميل :** {bot_name} 🥺🙈\n**رتبتك هي :** {rank}""", reply_markup=keyboard)

