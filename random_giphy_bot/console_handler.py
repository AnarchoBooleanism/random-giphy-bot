import asyncio
import os
from aioconsole import ainput, aprint
from dotenv import load_dotenv

class ConsoleHandler:
    """
    A class to asynchronously handle console commands and input.

    Attributes:
        discord_client (discord.Client): Discord client class that ConsoleHandler will communicate with. (default: None)
        giphy_handler (GiphyHandler): GIPHY handler class that ConsoleHandler will communicate with. (default: None)
        history (dict): Dictionary object that stores previous queries per guild, channel, and user. (default: None)
        command_list (dict): Dictionary matching console commands to ConsoleHandler methods.
    Methods:
        async program_quit():
            Quit any connections from Discord or GIPHY.
        async program_reload():
            Reload environmental variables and reset GIPHY handler and Discord handler with new tokens/API keys.
        async program_help():
            Print out list of commands and what they do.
        async program_clear_history():
            Clear random GIF query history.
        async run():
            Receive input for commands and execute commands asynchonously.
        __init__(discord_client=None, giphy_handler=None):
            Initialize object by passing in a Discord client class and a GIPHY handler class.

    """
    discord_client = None
    giphy_handler = None
    history = None

    # Command methods

    async def program_quit(self):
        """Quit any connections from Discord or GIPHY."""
        if self.giphy_handler:
            await self.giphy_handler.close()
            await asyncio.sleep(2)
        if self.discord_client:
            await aprint("Closing Discord client...")
            await self.discord_client.close()

    async def program_reload(self):
        """Reload environmental variables and reset GIPHY handler and Discord handler with new tokens/API keys."""
        load_dotenv(override=True)

        DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
        GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

        if self.giphy_handler:
            await self.giphy_handler.reload(api_key=GIPHY_API_KEY)
        if self.discord_client:
            await aprint("Logging in Discord bot with new token...")
            try:
                await self.discord_client.login(DISCORD_TOKEN) # Note: Test this somewhere else besides Windows to see if it actually works...
            except BaseException as problem:
                await aprint("Could not log in with new Discord token:", problem)

    async def program_help(self):
        """Print out list of commands and what they do."""
        await aprint(f"""Available commands to use:
help - Show list of available commands.
quit, exit - Exit the program safely.
reload - Reload the GIPHY handler and Discord client with updated tokens and API keys.
clearhistory - Clear random GIF query history.""")

    async def program_clear_history(self):
        """Clear random GIF query history."""
        if type(self.history) is dict and self.history:
            await aprint(f"Clearing {len(self.history)} value(s) from history...")
            self.history.clear()
        elif not type(self.history) is dict:
            await aprint("Cannot clear history. A history dictionary was not passed into ConsoleHandler.")
        else:
            await aprint("Nothing to clear from history.")

    # A list of commands that the console will refer to.
    command_list = {
        "quit": program_quit,
        "exit": program_quit,
        "reload": program_reload,
        "help": program_help,
        "clearhistory": program_clear_history
    }

    # Non-command methods

    async def run(self):
        """Receive input for commands and execute commands asynchonously."""
        console_input = None
        await aprint("You are now running Random GIPHY Bot! Type \"help\" for more!")
        await asyncio.sleep(5)

        while console_input not in ["quit", "exit"]:
            console_input = await ainput(">>> ")
            if console_input:
                command = console_input.split()[0]
            else:
                command = None

            if command in self.command_list:
                await self.command_list[command](self)
            elif command:
                await aprint(f"Command \"{command}\" is invalid. Type \"help\" for more.")

    def __init__(self, discord_client=None, giphy_handler=None, history=None):
        """Initialize object by passing in a Discord client class and a GIPHY handler class."""
        self.discord_client = discord_client
        if not self.discord_client:
            print("Warning: No discord.Client object was passed into ConsoleHandler")
        self.giphy_handler = giphy_handler
        if not self.giphy_handler:
            print("Warning: No GiphyHandler object was passed into ConsoleHandler")
        self.history = history
        if not type(self.history) is dict:
            print("Warning: No history dict was passed into ConsoleHandler")

def console_test():
    print("Note: You are running the console standalone!")
    """Run the console standalone."""
    console = ConsoleHandler()
    asyncio.run(console.run())

if __name__ == "__main__":
    console_test()
