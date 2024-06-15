import os
import random
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import tasks
from recieve_message import send_message, subscribers
from response_message import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f"[System]: {client.user} is now running!")
    send_news_to_all.start()


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {username}: \"{user_message}\"")
    await send_message(message, user_message)

@tasks.loop(hours=12)
async def send_news_to_all() -> None:
    if not subscribers:
        return
        
    print("[System]: Sending News...")

    number = random.randint(1, 9)

    await client.wait_until_ready()
    link = get_response(str(number))

    for subscriber in subscribers:
        daily_response = "News for today\n" + link

        try:
            await subscriber.send(daily_response)
            print(f"[System]: Sent News to {subscriber}")
        except Exception as e:
            print(f"[System]: Failed to send message to {subscriber}: {e}")

client.run(token=TOKEN)