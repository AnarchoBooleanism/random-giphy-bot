import asyncio
from aioconsole import ainput, aprint

async def bot_quit(discord_client=None, giphy_handler=None, *args, **kwargs):
    """
    Quit any connections from Discord or GIPHY.

    Parameters:
        discord_client (client) - Discord client to be disconnected and closed.
        giphy_handler (class) - aiohttp class with a connection to be closed.
    
    """
    if discord_client:
        await discord_client.close()

async def console_help(*args, **kwargs):
    """Print out list of commands and what they do."""
    await aprint(f"""Available commands to use:
help - Show list of available commands.
quit, exit - Exit the program safely.
""")

# A list of commands that the console will refer to.
command_list = {
    "quit": bot_quit,
    "exit": bot_quit,
    "help": console_help
}

async def console(discord_client=None, giphy_handler=None):
    """
    Receive input for commands and execute commands asynchonously.

    Parameters:
        discord_client (client): Discord client class to access for certain commands.
        giphy_client (giphy_handler): GIPHY handler class to access for certain commands.

    """
    console_input = None
    await aprint("You are now running Random GIPHY Bot! Type \"help\" for more!")
    await asyncio.sleep(5)

    while console_input not in ["quit", "exit"]:
        console_input = await ainput(">>> ")
        if console_input:
            command = console_input.split()[0]
        else:
            command = None

        if command in command_list:
            await command_list[command](discord_client=discord_client, giphy_handler=giphy_handler)
        elif command:
            await aprint(f"Command \"{command}\" is invalid. Type \"help\" for more.")


if __name__ == "__main__":
    asyncio.run(console())
