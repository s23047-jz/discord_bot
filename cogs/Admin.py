import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

SERVER_ID = 710091413903114241

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands loaded!")

    # @cog_ext.cog_slash(name="kick", description="ban memeber")


def setup(bot):
    bot.add_cog(Admin(bot))