# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from MusicMan.modules.msg import Messages as tr
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import Message
from MusicMan.config import SOURCE_CODE
from MusicMan.config import ASSISTANT_NAME
from MusicMan.config import PROJECT_NAME
from MusicMan.config import SUPPORT_GROUP
from MusicMan.config import UPDATES_CHANNEL
from MusicMan.config import BOT_USERNAME
from MusicMan.config import OWNER
logging.basicConfig(level=logging.INFO)



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐ Haii {message.from_user.first_name} saya adalah {PROJECT_NAME}\n
Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group.

โข Gunakan Perintah ยป /help ยซ untuk Mengetahui Fitur Lengkap saya
โโโโโโโโโโโโโโ
โ Managed With By [Owner](https://t.me/Xcimers)
โ Thanks To [GroupSupport](https://t.me/CariTemanSntuy)
โโโโโโโโโโโโโโโ
Ingin Menambahkan Saya ke Grup Anda? Tambahkan Saya Ke Group Anda!
</b>""",

# Edit Yang Perlu Lu ganti 
# Tapi Jangan di Hapus Thanks To nya Yaaa :D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Tambahkan saya ke Grup Anda โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "๐ฌ Channel Updates", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "๐ฎ Group Support", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "Developer", url=f"https://t.me/Xcimers")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if (pos==1):
        return [
            [InlineKeyboardButton(text = 'Next ยป', callback_data = "help+2")]
        ]
    elif pos==len(tr.HELP_MSG)-1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        return [
            [
                InlineKeyboardButton(
                    "โ Tambahkan saya ke Grup Anda โ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text='๐ฌ Channel Updates',
                    url=f"https://t.me/{UPDATES_CHANNEL}",
                ),
                InlineKeyboardButton(
                    text='๐ฎ Group Support', url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Developer', url=f"https://t.me/Xcimers"
                )
            ],
            [InlineKeyboardButton(text='ยซ', callback_data=f"help+{pos-1}")],
        ]

    else:
        return [
            [
                InlineKeyboardButton(text = 'ยซ', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'ยป', callback_data = f"help+{pos+1}")
            ],
        ]


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "๐๐ปโโ๏ธ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "โ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "โ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Cara Menggunakan BOT ๐", url=f"https://t.me/BeKing_Bots/9"
                    )
                ]
            ]
        ),
    )

