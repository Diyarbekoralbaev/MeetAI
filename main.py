from telethon.sync import TelegramClient, events
from func import *
import os
# Replace these values with your own API ID, API hash, and bot token
api_id = '23247142'
api_hash = '2ccfb68088cebfe211570d372b292170'
bot_token = '6708808913:AAHkUFWqpYZBirCgSbIOueXzQET7vkFXaKM'

client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond('Hello! I am your Audio Bot. Send me an audio message in MP3 format.')

@client.on(events.NewMessage)
async def audio_handler(event):
    # Check if the message has audio
    if event.message.audio:
        # Download the audio file
        audio = await event.message.download_media()
        
        response = await transcribe_audio(audio)
        
        await event.respond(response)
        
        os.remove(audio)

        # You can add your own processing logic here

    else:
        await event.respond('Please send an audio message in MP3 format.')


client.run_until_disconnected()
