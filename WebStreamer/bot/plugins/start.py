# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'ℍ𝕚 {m.from_user.mention(style="md")}, 𝕊𝕖𝕟𝕕 𝕞𝕖 𝕒 𝕗𝕚𝕝𝕖 𝕥𝕠 𝕘𝕖𝕥 𝕒𝕟 𝕚𝕟𝕤𝕥𝕒𝕟𝕥 𝕤𝕥𝕣𝕖𝕒𝕞 𝕝𝕚𝕟𝕜.\n\nപിന്നെ ഒരുകാര്യം ബോട്ട് start കൊടുത്തിട്ട് reply വരുന്നില്ലേ....  താഴെ കാണുന്ന 🅻︎🅸︎🅽︎🅺︎ എന്ന Box ൽ ക്ലിക്ക് ചെയ്യൂ\n\n🚨 Porn Contents will be gives you PERMANENT BAN 🚨\n\n🍃 Bᴏᴛ Made Bʏ :@MD_OWNER\n\n┈┈┈••✿ 👇👇🅻︎🅸︎🅽︎🅺︎👇👇 ✿••┈┈┈.'
    )
