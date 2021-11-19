import os

from dotenv import load_dotenv

from listener import const

load_dotenv(const.DOTENV_PATH)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TODOIST_TOKEN = os.getenv("TODOIST_TOKEN")

COMMAND_PREFIX = "!"
