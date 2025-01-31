# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton




@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = f"{Var.URL}{log_msg.message_id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    await m.reply_photo(
        photo="https://telegra.ph/file/847ab1940a2a2246c0417.jpg",
        caption="<b><u>𝗬𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱! 👍</u></b>\n\n<b><u>𝗖𝗼𝗽𝘆 𝘁𝗵𝗶𝘀 𝗹𝗶𝗻𝗸 👇</u></b>\n\n<code>{}</code>\n(<a href='{}'>shortened</a>)\n\n📝<b><u> 𝗡𝗢𝗧𝗘 </u></b>:\t𝑳𝑰𝑵𝑲 𝑾𝑶𝑵'𝑻 𝑬𝑿𝑷𝑰𝑹𝑬 𝑻𝑰𝑳𝑳 𝑰 𝑫𝑬𝑳𝑬𝑻𝑬\n\n🍃 Bᴏᴛ Made Bʏ : @MD_OWNER\n\n┈┈┈••✿ @MD_BOTZ ✿••┈┈┈".format(
            stream_link, short_link
        ),
        quote=True,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
             [
              InlineKeyboardButton("📥 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻 📥", url=stream_link),
              InlineKeyboardButton('🍬 ℙℝ𝕆𝕁𝔼ℂ𝕋 🍬', url='tg://resolve?domain=MD_BOTZ')
             ]
            ]
        ),
    )
