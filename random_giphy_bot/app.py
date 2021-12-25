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
        if message.author == client.user:
            return
        
        if "!gif" in message.content.split():
            if len(message.content.split()) != 2:
                await message.channel.send("!gif accepts only one word.")
            else:
                for runs in range(5):
                    response = giphy_api_handler.api_request(message.content.split()[1])
                    if response != -1:
                        break
                    await asyncio.sleep(2)
                if response == -1:
                    await message.channel.send("Giffybot is broken and was unable to find a GIF.")
                elif not response:
                    await message.channel.send("There was no GIF to be found.")
                else:
                    await message.channel.send(response)

    client.run(TOKEN)

if __name__ == "__main__":
    run()