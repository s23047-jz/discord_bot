import discord
from discord.ext import commands
from discord_slash import cog_ext

SERVER_ID = 710091413903114241

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help commands loaded!")

    @cog_ext.cog_slash(name='help', description='show all bot commands', guild_ids=[SERVER_ID])
    async def help(self, ctx):
        embed = discord.Embed(title="Embeb")
        embed.add_field(name='help', value='how all commands', inline=True)
        embed.add_field(name='hello', value='send hello message', inline=True)
        embed.add_field(name='greetings_options', value='Choose what kind of greetings you want', inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommands(bot))