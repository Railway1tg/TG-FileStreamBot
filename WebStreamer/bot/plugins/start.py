# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply_photo(
                  photo="https://telegra.ph/file/c0ada5cbcfdfcd5b2c269.jpg",
                  caption=f"""ℍ𝕚 {m.from_user.mention(style="md")}, 𝕊𝕖𝕟𝕕 𝕞𝕖 𝕒 𝕗𝕚𝕝𝕖 𝕥𝕠 𝕘𝕖𝕥 𝕒𝕟 𝕚𝕟𝕤𝕥𝕒𝕟𝕥 𝕤𝕥𝕣𝕖𝕒𝕞 𝕝𝕚𝕟𝕜.\n\n𝗪𝗔𝗥𝗡𝗜𝗡𝗚 ⚠️\n\n🚨 P🔞RN 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐋𝐞𝐚𝐝𝐬 𝐓𝐨 𝙋𝙀𝙍𝙈𝘼𝙉𝙀𝙉𝙏 𝘽𝘼𝙉 𝙔𝙊𝙐 🚨\n\n🍃 Bᴏᴛ Made Bʏ : @MD_OWNER\n\n┈┈┈••✿@MD_BOTZ✿••┈┈┈""",
                  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🍬 ℙ𝕣𝕠𝕛𝕖𝕔𝕥\t𝕔𝕙𝕒𝕟𝕟𝕖𝕝', url='https://telegram.me/MD_BOTZ'),
                    InlineKeyboardButton('🍭 𝕊𝕦𝕡𝕡𝕠𝕣𝕥\t𝕘𝕣𝕠𝕦𝕡', url='https://telegram.me/MD_BOTZ_DISCUSS')
                ],
                [
                    InlineKeyboardButton('🌹 Source code 🌹', url='https://github.com/EverythingSuckz/TG-FileStreamBot'),
                    InlineKeyboardButton('👩‍💻 Master', url='https://telegram.me/MD_OWNER')
                ]
            ]
        )
    )
