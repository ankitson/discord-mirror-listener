from discord.ext import commands
from cogwatch import watch

from listener import config, const

import itertools

import todoist

class ListenerBot(commands.Bot):
    def __init__(self) -> None:
        commands.Bot.__init__(self, command_prefix=config.COMMAND_PREFIX)

    @watch(path=const.COGS_PATH, preload=True, default_logger=False)
    async def on_ready(self) -> None:
        print("Running...")

        td = None
        try:
            td = todoist.TodoistAPI(config.TODOIST_TOKEN)
            td.sync()
            self.td = td
        except BaseException as err:
            print(f"Todoist api init fail: {err=}, {type(err)=}")
            self.td = None
            pass

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith(config.COMMAND_PREFIX):
            content = message.content[1:]
            if (content == "time"):
                import time
                await message.reply(time.time())
            else:
                await message.reply(message.content)


def start() -> None:
    print("Launching bot")
    bot = ListenerBot()
    bot.run(config.DISCORD_TOKEN)
