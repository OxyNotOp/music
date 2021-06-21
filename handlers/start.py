from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEKd9hg0EIdTk33yJYqYQqKylZl2uyrHQAClQMAAqLbyFSvfONBbv7Jtx8E")
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name}! Hii
I am powerful VC music Bot..🔥
I can play songs in your group's VC 😉

To listen songs also add @Music_op_bot to your group..

And don't forgot to promote me with all rights..😉
Otherwise I can't play songs..🙄

Use the buttons below to know more about me..🔥
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❤️ About Me ❤️", url="https://t.me/aboutoxy",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Official Group 🔥", url="https://t.me/X_F0RCE_TEAM"
                    ),
                    InlineKeyboardButton(
                        "My Creator 😎", url="https://t.me/FallenAngel_xD"
                    ),
                    InlineKeyboardButton(
                        "Commands ⚔️", url="https://telegra.ph/%F0%9D%95%90%F0%9D%96%94%F0%9D%96%9A%F0%9D%96%97---%F0%9D%95%AF%F0%9D%96%86%F0%9D%96%89%F0%9D%96%89%F0%9D%95%AA-%EA%97%84-04-18-8"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Music_op_bot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
