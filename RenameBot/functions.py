import humanize
import time
from pyrogram.errors import FloodWait


async def progress(current, total, message, process):
    new_current = humanize.naturalsize(current)
    new_total = humanize.naturalsize(total)
    percentage = round((current * 100) / total, 2)
    try:
        await message.edit(f"**{process}** \n\n**Progress : {percentage}℅** \n **Done** : {new_current} \n **Size** : {new_total} ")
    except FloodWait as e:
        time.sleep(e.x)
