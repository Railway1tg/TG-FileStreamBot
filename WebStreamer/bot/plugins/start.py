# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'Hi {t𝙘𝙝𝙚𝙘𝙠\t/help.\n\n🚨\t𝗣𝗼𝗿𝗻\t𝗖𝗼𝗻𝘁𝗲𝗻𝘁𝘀\t"
        "𝐰𝐢𝐥𝐥\t𝐛𝐞\t𝐠𝐢𝐯𝐞𝐬\t𝐲𝐨𝐮\t𝙋𝙀𝙍𝙈𝘼𝙉𝙀𝙉𝙏\t𝘽𝘼𝙉\t🚨\n\n🍃\tBᴏᴛ\tMade\tBʏ\t:\t@MD_OWNER",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🍬 ℙ𝕣𝕠𝕛𝕖𝕔𝕥\t𝕔𝕙𝕒𝕟𝕟𝕖𝕝', url='https://telegram.me/MD_BOTZ'),
                    InlineKeyboardButton('🍭 𝕊𝕦𝕡𝕡𝕠𝕣𝕥\t𝕘𝕣𝕠𝕦𝕡', url='https://telegram.me/MD_BOTZ_DISCUSS')
                ],
                [
                    InlineKeyboardButton('🌹 𝕊𝕠𝕦𝕣𝕔𝕖\t𝕔𝕠𝕕𝕖', url='tg://resolve?domain=MD_BOTZ&post=10'),
                    InlineKeyboardButton('👩‍💻 𝕄𝕒𝕤𝕥𝕖𝕣', url='https://telegram.me/MD_OWNER')
                ],
                [
                    InlineKeyboardButton('**𝑯𝒐𝒘\t𝒖𝒔𝒆\t𝒕𝒉𝒊𝒔\t𝒃𝒐𝒕\t🤔**', url='tg://resolve?domain=MD_BOTZ&post=20')
                ]
            ]
        )
    )
