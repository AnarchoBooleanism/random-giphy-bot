from random_giphy_bot import giphy_api_handler

async def gif(message, *args, **kwargs):
    """
    Reply to a message with a URL to a GIF, or another message if a GIF cannot be found.

    Parameters:
        message (message): Discord.py message to be used and analyzed.
    
    """
    if len(message.content.split()) != 2:
        await message.reply("`!gif` accepts only one word.")
    else:
        response = await giphy_api_handler.batch_request(message.content.split()[1])
        if response == -1:
            await message.reply("Giffybot is broken and was unable to find a GIF.")
        elif not response:
            await message.reply(f"No GIF found for \"{message.content.split()[1]}\".")
        else:
            await message.reply(response)

async def bot_help(message, *args, **kwargs):
    """
    Reply to a message with a list of commands available to be used.

    Parameters:
        message (message): Discord.py message to reply to.
    
    """
    await message.reply("""
**Available commands for Giffybot:**
`!gif (word)` - Find a random GIF using the word selected. One word only.
`!repeat` - Find another random GIF using the word from the previous `!gif` command. 
`!help` - List available commands for Giffybot. 
                        """)

# List of commands, with commands corresponding to specific functions to be called.
command_list = {
    "!gif": gif,
    "!help": bot_help
}