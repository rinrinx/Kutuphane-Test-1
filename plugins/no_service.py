import logging
from pyrogram import Client, filters
from info import NO_SERVICE
from pyrogram.types import Message

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@Client.on_message(filters.group & filters.service)
async def no_service(_, message:Message):
    if not NO_SERVICE: return
    try: await message.delete()
    except Exception as e:
        logger.error(e)
