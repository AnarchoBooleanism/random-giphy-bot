import os
from random_giphy_bot import giphy_api_handler
import discord
import asyncio
from dotenv import load_dotenv

def run():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    client = discord.Client()

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
        
        if "!gif" in message.content.split():
            if len(message.content.split()) != 2:
                await message.reply("!gif accepts only one word.")
            else:
                response = await giphy_api_handler.batch_request(message.content.split()[1])
                if response == -1:
                    await message.reply("Giffybot is broken and was unable to find a GIF.")
                elif not response:
                    await message.reply(f"No GIF found for \"{message.content.split()[1]}\".")
                else:
                    await message.reply(response)

    client.run(TOKEN)

if __name__ == "__main__":
    run()