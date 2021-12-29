# random-giphy-bot
Discord bot that gives a random GIF from GIPHY, based on a single word, with a console to remotely manage it.

## Discord features
`!gif (tag)` - Request a random GIF with a certain tag. Must be one word.
![Example of !gif Discord command](https://github.com/AnarchoBooleanism/random-giphy-bot/blob/main/README-content/gif_command_example.png?raw=true)
`!repeat` - Request a random GIF with a previously requested tag.
![Example of !repeat Discord command](https://github.com/AnarchoBooleanism/random-giphy-bot/blob/main/README-content/repeat_command_example.png?raw=true)
`!help` - Lists commands available with the bot.
![Example of !help Discord command](https://github.com/AnarchoBooleanism/random-giphy-bot/blob/main/README-content/help_command_example.png?raw=true)

## Console features
| Command | Description |
| ------- | ----------- |
|`help` | Show list of available commands. |
| `quit, exit` | Exit the program safely. |
| `reload` | Reload the GIPHY handler and Discord client with updated tokens and API keys. |
| `clearhistory` | Clear random GIF query history. |

## Requirements
random-giphy-bot requires a Python version of `>=3.10`.
Its dependencies include `discord.py`, `python-dotenv`, `aioconsole`, and `aiohttp`.

## Setup
First, make sure to install [Python 3.10 or higher](https://www.python.org/downloads/).
Install random-giphy-bot's dependencies with this command:
`pip install -U discord.py python-dotenv aioconsole aiohttp`

Next, copy the repository, or a [release](https://github.com/AnarchoBooleanism/random-giphy-bot/releases), and copy it over to a folder where you want to deploy it.

Next, get a [Discord bot token](https://discord.com/developers/) and a [GIPHY API key](https://developers.giphy.com/).
Setup a `.env` file in the `random_giphy_bot` directory, and insert these values:
    GIPHY_API_KEY=(Your GIPHY API key)
    DISCORD_TOKEN=(Your Discord token)

To run, make sure you are in the root directory of the repository/release, and run this command:
`python -m random_giphy_bot`

## License
This project's license is [LGPL 2.1](LICENSE).