from random_giphy_bot import giphy_api_handler

async def gif_finder(tag, message, giphy_handler):
    """
    Reply to a message with a URL to a GIF, or another message if a GIF cannot be found.

    Parameters:
        tag (str): Tag of GIF to find.
        message (message): Discord.py message to be used and analyzed.
    
    """
    response = await giphy_handler.random_request(tag)
    if response == -1:
        await message.reply("Giffybot is broken and was unable to find a GIF.")
    elif not response:
        await message.reply(f"No GIF found for \"{message.content.split()[1]}\".")
    else:
        await message.reply(response)

async def gif(message, history, giphy_handler, *args, **kwargs):
    """
    Handle a command to request a URL to a GIF from a certain word.

    Parameters:
        message (message): Discord.py message to be used and analyzed.
        history (dict): A list of previously used words, per server, channel, and user.
    
    """
    if len(message.content.split()) != 2:
        await message.reply("`!gif` accepts only one word.")
    else:
        if (type(message.guild) is None):
            new_tag = (message.guild.id, message.channel.id, message.author.id)
        else:
            new_tag = (message.channel.id, message.author.id)
        
        gif_tag = message.content.split()[1]
        history[new_tag] = gif_tag
        await gif_finder(tag=gif_tag, message=message, giphy_handler=giphy_handler)

async def repeat(message, history, giphy_handler, *args, **kwargs):
    """
    Handle a command to request a URL to a GIF from a previously selected word.

    Parameters:
        message (message): Discord.py message to be used and analyzed.
        history (dict): A list of previous used words, per server, channel, and user.
    
    """
    if (type(message.guild) is None):
        previous_tag = (message.guild.id, message.channel.id, message.author.id)
    else:
        previous_tag = (message.channel.id, message.author.id)

    if previous_tag in history:
        await gif_finder(tag=history[previous_tag], message=message, giphy_handler=giphy_handler)
    else:
        await message.reply("Giffybot doesn't have a previous word query to work off of. Use `!gif` first.")

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
    "!repeat": repeat,
    "!help": bot_help
}
