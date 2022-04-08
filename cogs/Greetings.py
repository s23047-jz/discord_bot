import discord
from discord.ext import commands
from discord import Intents
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

SERVER_ID = 710091413903114241

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Greetings commands loaded!")

    # @commands.command(name='hi')
    # async def hi(self, ctx):
    #     await ctx.send("hi")

    @cog_ext.cog_slash(name="hello", description="sending hello message", guild_ids=[SERVER_ID])
    async def _hello(self, ctx):
        await ctx.send("hello from bot")

    @cog_ext.cog_slash(
        name="greetings_options",
        description="testing options function",
        options=[
            create_option(
                name='user',
                description='mention a user',
                required=True,
                option_type=6
            ),
            create_option(
                name='greetings',
                description='what want to send',
                required=True,
                option_type=3,
                choices=[
                    create_choice(
                        name='love',
                        value='I <3 you'
                    ),
                    create_choice(
                        name='day',
                        value='have a nice day'
                    ),
                    create_choice(
                        name='happy',
                        value='do not worry, be happy now ttutututu'
                    ),
                    create_choice(
                        name="birthday",
                        value="Happy birthday to You, Happy birthday to You"
                    )
                ]
            )
        ],
        guild_ids=[SERVER_ID]
    )
    async def greetings_a_member(self, ctx, user:discord.User, greetings:str):
        await ctx.send(f"{greetings} {user.mention} from {ctx.author.mention} ")


def setup(bot):
    bot.add_cog(Greetings(bot))