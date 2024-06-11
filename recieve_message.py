from discord import Message
from response_message import get_response

subscribers: set = set()

help_info = '''# About BOTTER
This is a Discord Bot that sends you English News from *engoo.com*.

## Daily News Function
If you want to recieve a piece of news on an hour basis, just type `-register`.
And just type `-unregister` whenever you don't want to recieve.

## Specific News Function
If you want to recieve a piece of news with specific category, just type the `-(number)` for specififc news.
Don't forget to change the `(number)` for your destined ones.
(e.g. Type `-3` for Economy & Business.)

### Categories
:one: Science & Technology
:two: Culture & Environment
:three: Economy & Business
:four: Health
:five: Travel & Lifestyle
:six: Language & Education
:seven: Asia & Pacific
:eight: USA & Americas
:nine: Europe


:bulb: Noting that BOTTER can send private message to you whenever you add `$` before any messages.
'''

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("[System]: Message was empty.")
        return

    if is_private := user_message[0] == '$':
        user_message = user_message[1:]

    if user_message[0:1] != "-":
        return

    if user_message == "-help":
        await message.author.send(help_info) if is_private else await message.channel.send(help_info)

    elif user_message == "-register":
        subscribers.add(message.author)
        subscribe_response: str = "Subscribed Successfully!"
        print(f"[System]: {message.author} subscribed!")
        await message.author.send(subscribe_response) if is_private else await message.channel.send(subscribe_response)

    elif user_message == "-unregister":
        subscribers.remove(message.author)
        subscribe_response: str = "Unsubscribed Successfully!"
        print(f"[System]: {message.author} unsubscribed!")
        await message.author.send(subscribe_response) if is_private else await message.channel.send(subscribe_response)
        
    else:
        user_message = user_message[1:]
        try:
            number: int = int(user_message)
            await message.author.send("Got it! Wait a second...") if is_private else await message.channel.send("Got it! Wait a second...")
            response: str = "Here you go: " + get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)

        except Exception as e:
            response = "Nice try! But your format might be something wrong :("
            await message.author.send(response) if is_private else await message.channel.send(response)
            print(f"[System]: {e}")
