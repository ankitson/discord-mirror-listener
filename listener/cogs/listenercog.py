import json
from os import path

from discord.ext import commands

from listener import const
from listener import utils


class ListenerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings = self.load_settings()

    @commands.command()
    async def watch_channel(self, ctx, channel_id: str):
        if channel_id.isnumeric():
            channel_id = int(channel_id)
            self.settings["channels"].append(channel_id)
            self.save_settings()
            await ctx.send(f"Added channel {channel_id} to watch list.")
        else:
            await ctx.send("Channel ID is not valid")

    @commands.command()
    async def unwatch_channel(self, ctx, channel_id: str):
        if channel_id.isnumeric():
            channel_id = int(channel_id)
            self.settings["channels"].pop(channel_id)
            self.save_settings()
            await ctx.send(f"Removed channel {channel_id} from watch list.")
        else:
            await ctx.send("Channel ID is not valid")

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        if message.channel.id in self.settings["channels"]:
            content = message.content
            print(content)

    def save_settings(self):
        with open(const.SETTINGS_PATH / "settings.json", "w") as f:
            json.dump(self.settings, f)

    def load_settings(self):
        if path.exists(const.SETTINGS_PATH / "settings.json"):
            with open(const.SETTINGS_PATH / "settings.json", "r") as infile:
                return utils.pythonify(json.load(infile))
        return {"channels": []}


def setup(bot):
    bot.add_cog(ListenerCog(bot))
