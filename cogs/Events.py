import discord
from discord.ext import commands
from discord_slash import cog_ext

import __main__


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Events commands loaded!")

    @commands.Cog.listener(name='new_user')
    async def welcome_new_user(self, user:discord.Member):
        new_user = discord.utils.get(user.guild.channels, id(__main__.Config.community_chat_id))
        await new_user.send(f"Welcome {user.metion}!! Hope you will enjoy on our server 😍'")



def setup(bot):
    bot.add_cog(Events(bot))