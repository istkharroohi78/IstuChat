from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from ISTKHAR_CHATBOT import OWNER, ISTKHAR_CHATBOT


START_BOT = [
    [
        InlineKeyboardButton(
            text="▪️ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ▪️",
            url=f"https://t.me/{ISTKHAR_CHATBOT.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="▪️ ᴏᴡɴᴇʀ ▪️", user_id=OWNER),
        InlineKeyboardButton(text="▪️ ꜱᴜᴘᴘᴏʀᴛ ▪️", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="▪️ ʏᴏᴜʀ ᴄᴏᴍᴍᴀɴᴅ ▪️", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(text="▪️ ᴏᴡɴᴇʀ ▪️", user_id=OWNER),
        InlineKeyboardButton(text="▪️ ꜱᴜᴘᴘᴏʀᴛ ▪️", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="▪️ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ▪️",
            url=f"https://t.me/{ISTKHAR_CHATBOT.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="▪️ ʜᴇʟᴘ ▪️", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="▪️ ᴀʙᴏᴜᴛ ▪️", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="▪️ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ▪️",
            url=f"https://t.me/{ISTKHAR_CHATBOT.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="▪️ ᴄʟᴏꜱᴇ ▪️",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="▪️ ʙᴀᴄᴋ ▪️", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="▪️ ᴄʜᴀᴛʙᴏᴛ ▪️", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="▪️ ᴛᴏᴏʟꜱ ▪️", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="▪️ ᴄʟᴏꜱᴇ ▪️", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="▪️ ᴄʟᴏꜱᴇ ▪️", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="▪️ ᴇɴᴀʙʟᴇ ▪️", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="▪️ ᴅɪꜱᴀʙʟᴇ ▪️", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="ꜱᴏᴏɴ", callback_data="soom"),
    ],
]


S_BACK = [
    [
        InlineKeyboardButton(text="▪️ ʙᴀᴄᴋ ▪️", callback_data="SBACK"),
        InlineKeyboardButton(text="▪️ ᴄʟᴏꜱᴇ ▪️", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="▪️ ʙᴀᴄᴋ ▪️", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="▪️ ᴄʟᴏꜱᴇ ▪️", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="▪️ ʜᴇʟᴘ ▪️", callback_data="HELP"),
        InlineKeyboardButton(text="▪️ ᴄʟᴏꜱᴇ ▪️", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="▪️ ʜᴇʟᴘ ▪️",
            url=f"https://t.me/{ISTKHAR_CHATBOT.username}?start=help",
        ),
        InlineKeyboardButton(text="▪️ ᴄʟᴏꜱᴇ ▪️", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="▪️ ꜱᴜᴘᴘᴏʀᴛ ▪️", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="▪️ ʜᴇʟᴘ ▪️", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="▪️ ᴏᴡɴᴇʀ ▪️", user_id=OWNER),
    ],
    [
        InlineKeyboardButton(text="▪️ ᴜᴘᴅᴀᴛᴇ ▪️", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="▪️ ʙᴀᴄᴋ ▪️", callback_data="BACK"),
    ],
]
