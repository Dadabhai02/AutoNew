import re
from pyrogram import filters, Client, enums
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, UsernameInvalid, UsernameNotModified
from info import ADMINS, LOG_CHANNEL, FILE_STORE_CHANNEL, PUBLIC_FILE_STORE
from database.ia_filterdb import unpack_new_file_id
from utils import temp
import re
import os
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False

@Client.on_message(filters.command(['link', 'plink']) & filters.create(allowed))
async def gen_link_s(bot, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴀ ꜱʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ.')
    file_type = replied.media
    if file_type not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.AUDIO, enums.MessageMediaType.DOCUMENT]:
        return await message.reply("ʀᴇᴘʟʏ ᴛᴏ sᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ")
    if message.has_protected_content and message.chat.id not in ADMINS:
        return await message.reply("okDa")
    file_id, ref = unpack_new_file_id((getattr(replied, file_type.value)).file_id)
    string = 'filep_' if message.text.lower().strip() == "/plink" else 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    await message.reply(f"Here is your Link:\nhttps://t.me/{temp.U_NAME}?start={outstr}")
    
    
@Client.on_message(filters.command(['batch', 'pbatch']) & filters.create(allowed))
async def gen_link_batch(bot, message):
    if " " not in message.text:
        return await message.reply("𝖴𝗌𝖾 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖥𝗈𝗋𝗆𝖺𝗍 : \n\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾 : <code>/batch https://t.me/DaDa_Linkz/3 https://t.me/DaDa_Linkz/3</code>.")
    links = message.text.strip().split(" ")
    if len(links) != 3:
        return await message.reply("𝖴𝗌𝖾 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖥𝗈𝗋𝗆𝖺𝗍 : \n\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾 : <code>/batch https://t.me/DaDa_Linkz/3 https://t.me/DaDa_Linkz/3</code>.")
    cmd, first, last = links
    regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
    match = regex.match(first)
    if not match:
        return await message.reply('ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ')
    f_chat_id = match.group(4)
    f_msg_id = int(match.group(5))
    if f_chat_id.isnumeric():
        f_chat_id  = int(("-100" + f_chat_id))

    match = regex.match(last)
    if not match:
        return await message.reply('ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ')
    l_chat_id = match.group(4)
    l_msg_id = int(match.group(5))
    if l_chat_id.isnumeric():
        l_chat_id  = int(("-100" + l_chat_id))

    if f_chat_id != l_chat_id:
        return await message.reply("ᴄʜᴀᴛ ɪᴅ's ɴᴏᴛ ᴍᴀᴛᴄʜᴇᴅ.")
    try:
        chat_id = (await bot.get_chat(f_chat_id)).id
    except ChannelInvalid:
        return await message.reply('Tʜɪꜱ ᴍᴀʏ ʙᴇ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ / ɢʀᴏᴜᴘ. Mᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏᴠᴇʀ ᴛʜᴇʀᴇ ᴛᴏ ɪɴᴅᴇx ᴛʜᴇ ғɪʟᴇꜱ.')
    except (UsernameInvalid, UsernameNotModified):
        return await message.reply('ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ sᴘᴇᴄɪғɪᴇᴅ.')
    except Exception as e:
        return await message.reply(f'Errors - {e}')

    sts = await message.reply("ɢᴇɴᴇʀᴀᴛɪɴɢ ʟɪɴᴋ's ғᴏʀ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ.\nTʜɪꜱ ᴍᴀʏ ᴛᴀᴋᴇ ᴛɪᴍᴇ ᴅᴇᴘᴇɴᴅɪɴɢ ᴜᴘᴏɴ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇꜱꜱᴀɢᴇꜱ")
    if chat_id in FILE_STORE_CHANNEL:
        string = f"{f_msg_id}_{l_msg_id}_{chat_id}_{cmd.lower().strip()}"
        b_64 = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
        return await sts.edit(f"ʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋ https://t.me/{temp.U_NAME}?start=DSTORE-{b_64}")

    FRMT = "ɢᴇɴᴇʀᴀᴛɪɴɢ ʟɪɴᴋ...\nᴛᴏᴛᴀʟ ᴍᴇssᴀɢᴇs: `{total}`\nᴅᴏɴᴇ: `{current}`\nʀᴇᴍᴀɪɴɪɴɢ : `{rem}`\nsᴛᴀᴛᴜs: `{sts}`"

    outlist = []

    # file store without db channel
    og_msg = 0
    tot = 0
    async for msg in bot.iter_messages(f_chat_id, l_msg_id, f_msg_id):
        tot += 1
        if msg.empty or msg.service:
            continue
        if not msg.media:
            # only media messages supported.
            continue
        try:
            file_type = msg.media
            file = getattr(msg, file_type.value)
            caption = getattr(msg, 'caption', '')
            if caption:
                caption = caption.html
            if file:
                file = {
                    "file_id": file.file_id,
                    "caption": caption,
                    "title": getattr(file, "file_name", ""),
                    "size": file.file_size,
                    "protect": cmd.lower().strip() == "/pbatch",
                }

                og_msg +=1
                outlist.append(file)
        except:
            pass
        if not og_msg % 20:
            try:
                await sts.edit(FRMT.format(total=l_msg_id-f_msg_id, current=tot, rem=((l_msg_id-f_msg_id) - tot), sts="Saving Messages"))
            except:
                pass
    with open(f"batchmode_{message.from_user.id}.json", "w+") as out:
        json.dump(outlist, out)
    post = await bot.send_document(LOG_CHANNEL, f"batchmode_{message.from_user.id}.json", file_name="Batch.json", caption="⚠️ɢᴇɴᴇʀᴀᴛᴇᴅ ғᴏʀ ғɪʟᴇ sᴛᴏʀᴇ.")
    os.remove(f"batchmode_{message.from_user.id}.json")
    file_id, ref = unpack_new_file_id(post.document.file_id)
    await sts.edit(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ \nContains `{og_msg}` files.\n https://t.me/{temp.U_NAME}?start=BATCH-{file_id}")
