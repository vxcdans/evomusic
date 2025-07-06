from pyrogram.types import Message

from WinxMusic import app
from WinxMusic.utils.database import is_on_off
from config import LOG, LOG_GROUP_ID


async def play_logs(message: Message, streamtype: str):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "🔒 Grupo Privado"

        logger_text = f"""
🎵 **BOT MUSIC - {app.mention}** 🎵

📌 **ID Chat:** `{message.chat.id}`
🏷️ **Group Chat:** {message.chat.title}
🔗 **Username Group Chat:** {chatusername}

👤 **ID:** `{message.from_user.id}`
📛 **Name:** {message.from_user.mention}
📱 **Username:** @{message.from_user.username}

🔍 **Result:** {message.text.split(None, 1)[1]}
🎧 **Type:** {streamtype}"""

        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(e)
        return
