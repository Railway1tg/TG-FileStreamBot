# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(f'ങ്ക് ഇവിടെ 👉 [paste ചെയ്യുക](tg://resolve?domain=SCREEN_SHOT_ROBOT)\n\n𝙁𝙤𝙧\t𝙢𝙤𝙧𝙚\t"
        "𝙙𝙚𝙩𝙖𝙞𝙡𝙨\t𝙘𝙝𝙚𝙘𝙠\t/help.\n\n🚨\t𝗣𝗼𝗿𝗻\t𝗖𝗼𝗻𝘁𝗲𝗻𝘁𝘀\t"
        "𝐰𝐢𝐥𝐥\t𝐛𝐞\t𝐠𝐢𝐯𝐞𝐬\t𝐲𝐨𝐮\t𝙋𝙀𝙍𝙈𝘼𝙉𝙀𝙉𝙏\t𝘽𝘼𝙉\t🚨\n\n🍃\tBᴏᴛ\tMade\tBʏ\t:\t@MHND_KDR",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🍬 ℙ𝕣𝕠𝕛𝕖𝕔𝕥\t𝕔𝕙𝕒𝕟𝕟𝕖𝕝', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL'),
                    InlineKeyboardButton('🍭 𝕊𝕦𝕡𝕡𝕠𝕣𝕥\t𝕘𝕣𝕠𝕦𝕡', url='https://telegram.me/MHND_BOT_UPDATE_GROUP')
                ],
                [
                    InlineKeyboardButton('🌹 𝕊𝕠𝕦𝕣𝕔𝕖\t𝕔𝕠𝕕𝕖', url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL/145'),
                    InlineKeyboardButton('👩‍💻 𝕄𝕒𝕤𝕥𝕖𝕣', url='https://telegram.me/MHND_KDR')
                ],
                [
                    InlineKeyboardButton('**𝑯𝒐𝒘\t𝒖𝒔𝒆\t𝒕𝒉𝒊𝒔\t𝒃𝒐𝒕\t🤔**', url='tg://resolve?domain=MHND_BOT_UPDATE_CHANNEL&post=147')
                ]
            ]
        )
    )
