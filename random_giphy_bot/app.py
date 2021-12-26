import os
from random_giphy_bot import commands
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

        print(
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

    client.run(TOKEN)

if __name__ == "__main__":
    run()