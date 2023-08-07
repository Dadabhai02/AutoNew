class script(object):
    START_TXT = """<b>Hᴇʏ {}</b>
   \n<i>Iam A Simple Auto Filter + Movie Search + Manual Filter Bot. I Can Provide Movies In Telegram Groups. You Can Search Movies Via Inline. I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group And Enjoy</i>
   \n<b>Made BY 🌻: <a href=https://t.me/DaDaXBhai>DaDa Bhai</a></b> """

    HELP_TXT = """<b>Hᴇʏ {} Fʀɪᴇɴᴅ Hᴇʀᴇ Yᴏᴜʀ Bᴜᴛᴛᴏɴs 👇</b>"""

    PRIVATEBOT_TXT = """<b>Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ

- ›› Mᴜsᴛ Aᴅᴅ Mᴇ Aᴅᴍɪɴ Tᴏ Wᴏʀᴋ Oɴ Tʜɪs Gʀᴏᴜᴘ

- ›› Cʜᴀɴɢᴇ Sᴇᴛᴛɪɴɢ Fᴏʀ Uʀ Gʀᴏᴜᴘ Cʟɪᴄᴋ 👉 /connect

- ›› I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs/Sᴇʀɪᴇs Dᴏɴ'ᴛ Wᴏʀʀʏ

- ›› Eɴᴊᴏʏ !! Mᴏʀᴇ Iɴғᴏ Usᴇ Uɴᴅᴇʀ Bᴜᴛᴛᴏɴs</b>
"""

    MODS_TXT = """I Hᴀᴠᴇ Mᴀɴʏ Fᴇᴀᴛᴜʀᴇs"""

    PONGD_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""
    
    PONG_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""

    ABOUT_TXT = """<b>Ｍｙ Ｎａｍｅ: <a href=https://t.me/DADA_LINKZ>ＤａＤａ Ｘ  Ｍｏｖｉｅｓ Ｆｉｌｔｅｒ Ｂｏｔ</a>
➲ 𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 <a href=https://t.me/Dada_offil>𝖣𝖺𝖣𝖺 𝖡𝗁𝖺𝗂 🤾🏻‍♂️</a>
➲ 𝘓𝘢𝘯𝘨𝘶𝘢𝘨𝘦  : 𝘗𝘺𝘵𝘩𝘰𝘯 3
➲ 𝘋𝘢𝘵𝘢𝘣𝘢𝘴𝘦 : 𝘔𝘰𝘯𝘨𝘰𝘋𝘉
➲ 𝘉𝘰𝘵 𝘚𝘦𝘳𝘷𝘦𝘳 : <a href=https://t.me/DaDaXBhai/12>𝘍𝘳𝘦𝘦 𝘏𝘰𝘴𝘵</a></b>"""

    SOURCES_TXT = """Tʜɪs Is Aɴ Oᴩᴇɴ-Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Bʏ @Tamilan_BotsZ

- 100﹪ Cᴏᴅᴇᴅ Bʏ <a href=https://t.me/SharathItsIsme>sʜᴀʀᴀᴛʜ</a>

- & Rᴇᴩᴏ Lɪɴᴋ 👇 Hᴇʀᴇ"""

    SOURCE_TXT = """Tʜɪs Is Aɴ Oᴩᴇɴ-Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Bʏ @Tamilan_BotsZ</b>

- 100﹪ Cᴏᴅᴇᴅ Bʏ <a href=https://t.me/SharathItsIsme>sʜᴀʀᴀᴛʜ</a></b>

- Rᴇᴩᴏ Lɪɴᴋ 👇 Hᴇʀᴇ"""

    FONT_TXT = """I Cᴀɴ Gᴇɴᴇʀᴀᴛᴇ Aᴛᴛʀᴀᴄᴛɪᴠᴇ Fᴏɴᴛs Fᴏʀ Yᴏᴜʀ Tᴇxᴛ Sᴇɴᴅ Lɪᴋᴇ Tʜɪs 👇

ᴇɢ :- /font hi da"""

    CARBON_TXT = """/carbon ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /carbon hi"""

    SHARE_TXT = """/share ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /share hi da"""

    VIDEO_TXT ="""Dᴏᴡɴʟᴏᴀᴅ Aɴʏ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏ Fʀᴏᴍ Tʜᴇ Vɪᴅᴇᴏ Lɪɴᴋ

• Hᴏᴡ Tᴏ Usᴇ
• Tʏᴘᴇ /video 𝘈𝘯𝘥 (YᴏᴜTᴜʙᴇ Vɪᴅᴇᴏ Lɪɴᴋ)
• Exᴀᴍᴘʟᴇ:
• /video https://youtu.be/kB9TkCscX0"""

    TELE_TXT = """▫️Hᴇʟᴘ: ▪️ Tᴇʟᴇɢʀᴀᴘʜ ▪️
     Tᴇʟᴇɢʀᴀᴘʜ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ
    Usᴀɢᴇ
    🤧 /telegraph - Sᴇɴᴅ Mᴇ Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ (5ᴍʙ)"""

    MANUELFILTER_TXT = """<b>Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Mᴏᴠɪᴇs / Sᴇʀɪᴇs Usɪɴɢ Tʜɪs Bᴏᴛ</b> 😌 🔋

<b>Fɪʀsᴛ Jᴏɪɴ Tʜɪs Gʀᴏᴜᴩ » @TamilanMoviesChat</b>

<b>Sᴇɴᴅ Yᴏᴜ Wᴀɴᴛ Mᴏᴠɪᴇs Oʀ Sᴇʀɪᴇs Nᴀᴍᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴩᴇʟʟɪɴɢ</b>

<b>Aɴᴅ Bᴏᴛ Wɪʟʟ Sᴇɴᴅ Yᴏᴜ Asᴋᴇᴅ Fɪʟᴇ</b>

<b>Hᴏᴡ Tᴏ Oᴩᴇɴ Bᴏᴛ Sᴇɴᴅᴇᴅ Fɪʟᴇ Lɪɴᴋ. » <a href=https://t.me/Sharath_Links/13>ᴛᴜᴛᴏʀɪᴀʟ</a>.﹤/b>"""

    CONTACT_TXT = """<b>
<b>»» ° Oɴʟʏ Cᴏɴᴛᴀᴄᴛ Fᴏʀ Pᴀɪᴅ Wᴏʀᴋs / Pʀᴏʙʟᴇᴍ / Dᴏᴜʙᴛ / Cᴏʟʟᴀʙ / Hᴇʟᴩ °</b>

<b>»» Iғ U Cᴏɴᴛᴀᴄᴛ Mᴇ Sᴇᴇ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs 😙</b>
"""

    STATUS_TXT = """<b><u>𝘊𝘶𝘳𝘳𝘦𝘯𝘵 𝘋𝘢𝘵𝘢𝘣𝘢𝘴𝘦 𝘚𝘵𝘢𝘵𝘶𝘴 📊</b></u>
    
<b>➲ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌: <code>{}</code>
➲ 𝖳𝗈𝗍𝖺𝗅 𝖴𝗌𝖾𝗋𝗌: <code>{}</code>
➲ 𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌: <code>{}</code>
➲ 𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code></b>
"""
    LOG_TEXT_G = """<b> #NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} </b>
"""
    LOG_TEXT_P = """<b> #NewUser
ɪᴅ ♥️- <code>{}</code>
ɴᴀᴍᴇ 💥- {} </b>
"""
