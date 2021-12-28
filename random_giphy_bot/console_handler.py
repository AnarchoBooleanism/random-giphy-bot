import asyncio
import os
from aioconsole import ainput, aprint
from dotenv import load_dotenv

async def bot_quit(discord_client=None, giphy_handler=None, *args, **kwargs):
    """
    Quit any connections from Discord or GIPHY.

    Parameters:
        discord_client (client) - Discord client to be disconnected and closed.
        giphy_handler (class) - aiohttp class with a connection to be closed.
    
    """
    if giphy_handler:
        await giphy_handler.close()
    await asyncio.sleep(2)
    if discord_client:
        await aprint("Closing Discord client...")
        await discord_client.close()

async def bot_reload(discord_client=None, giphy_handler=None, *args, **kwargs):
    """
    Reload environmental variables and reset GIPHY handler and Discord handler with new tokens/API keys.

    Parameters:
        discord_client (client) - Discord client to be reloaded with new token.
        giphy_handler (class) - aiohttp class to be reloaded with new API key.

    """
    load_dotenv(override=True)

    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

    if giphy_handler:
        await giphy_handler.reload(api_key=GIPHY_API_KEY)
    if discord_client:
        await aprint("Logging in Discord bot with new token...")
        try:
            await discord_client.login(DISCORD_TOKEN) # Note: Test this somewhere else besides Windows to see if it actually works...
        except BaseException as problem:
            await aprint("Could not log in with new Discord token:", problem)

async def console_help(*args, **kwargs):
    """Print out list of commands and what they do."""
    await aprint(f"""Available commands to use:
help - Show list of available commands.
quit, exit - Exit the program safely.
reload - Reload the GIPHY handler and Discord client with updated tokens and API keys.""")

# A list of commands that the console will refer to.
command_list = {
    "quit": bot_quit,
    "exit": bot_quit,
    "reload": bot_reload,
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
