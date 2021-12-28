import os
import asyncio
from aioconsole import ainput, aprint
from random_giphy_bot import commands
from random_giphy_bot.console_handler import console
from random_giphy_bot.giphy_api_handler import GiphyHandler
import discord
from dotenv import load_dotenv

def run():
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    DISCORD_GUILD = os.getenv('DISCORD_GUILD')
    GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

    client = discord.Client()
    history = dict()
    giphy_handler = GiphyHandler()

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == DISCORD_GUILD:
                break

        await aprint(
            f'{client.user} is connected to the following guild(s):\n'
            f'{guild.name}(id: {guild.id})'
        )

    @client.event
    async def on_message(message):
        if message.author.id == client.user.id:
            return
        
        command = message.content.split()[0].lower()

        if message.content.startswith("!"):
            if command in commands.command_list:
                await commands.command_list[command](message=message, history=history, giphy_handler=giphy_handler)
            else:
                await message.reply(f"Invalid command: `{command}`")
    
    # Start console (passing in Discord client and GIPHY handler), then run Discord client, which is blocking.
    # When Discord client stops, then it will make sure that the console loop finishes before ending. 
    console_loop = asyncio.get_event_loop()
    console_task = console_loop.create_task(console(discord_client=client, giphy_handler=giphy_handler))
    giphy_handler.start(GIPHY_API_KEY)
    print("Opening Discord bot...")
    client.run(DISCORD_TOKEN)
    console_loop.run_until_complete(console_task)

if __name__ == "__main__":
    run()