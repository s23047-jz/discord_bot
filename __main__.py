from discord.ext import commands
from dotenv import load_dotenv
import os

if __name__ == "__main__":

    load_dotenv()
    bot = commands.Bot(command_prefix='.')

    @bot.command()
    async def load(ctx, extension):
        bot.load_extension(f'cogs.{extension}')

    @bot.command()
    async def unload(ctx, extension):
        bot.load_extension(f'cogs.{extension}')

    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    bot.run(os.getenv("TOKEN"))