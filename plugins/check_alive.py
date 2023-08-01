import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("<b>Contact ~ @DaDa_Linkz</b>")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("<b>Contact ~ @DaDa_Linkz</b>")

@Client.on_message(filters.command("credits", CMD))
async def help(_, message):
    await message.reply_text("<b>Contact ~ @DaDa_Linkz</b>")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("<b>Contact ~ @DaDa_Linkz</b>")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("<b>Contact ~ @DaDa_Linkz</b>")

@Client.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("<b>Contact ~ @DaDa_Linkz</b>")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
