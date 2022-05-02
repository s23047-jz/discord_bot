import discord
from discord.ext import commands
from discord_slash import cog_ext

import __main__


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help commands loaded!")

    @cog_ext.cog_slash(name='help', description='show all bot commands', guild_ids=[__main__.Config.guild_id])
    async def help(self, ctx, user:discord.Member):
        embed = discord.Embed(title="Embeb")
        embed.add_field(name='help', value='how all commands', inline=True)
        embed.add_field(name='hello', value='send hello message', inline=True)
        embed.add_field(name='greetings_options', value='Choose what kind of greetings you want', inline=True)
        if __main__.Config.owners_name in user.roles:
            embed.add_field(name='ban', value='ban a user', inline=True)
            embed.add_field(name='kick', value='kick a user', inline=True)
            embed.add_field(name='add_role', value='add role to user', inline=True)
            embed.add_field(name='remove_role', value='remove role to user', inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommands(bot))