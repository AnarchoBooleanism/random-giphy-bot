import os
import asyncio
from aioconsole import ainput, aprint
from random_giphy_bot import commands
from random_giphy_bot.console_handler import console
import discord
from dotenv import load_dotenv

def run():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    client = discord.Client()
    history = dict()

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        aprint(
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
                await commands.command_list[command](message=message, history=history)
            else:
                await message.reply(f"Invalid command: `{command}`")
    
    # Start console (passing in Discord client and GIPHY handler), then run Discord client, which is blocking.
    # When Discord client stops, then it will make sure that the console loop finishes before ending. 
    console_loop = asyncio.get_event_loop()
    console_task = console_loop.create_task(console(discord_client=client))
    client.run(TOKEN)
    console_loop.run_until_complete(console_task)

if __name__ == "__main__":
    run()