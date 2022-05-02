import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

import __main__


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands loaded!")

    @cog_ext.cog_slash(name='ban',
                       description='ban an user',
                       options=[
                           create_option(
                               name='user',
                               description='choose user',
                               required=True,
                               option_type=6
                           ),
                           create_option(
                               name='reason',
                               description='say why you want ban this user',
                               required=True,
                               option_type=3,
                               choices=[
                                   create_choice(
                                       name="offending language",
                                       value="User used incorrect vocabullary"
                                   ),
                                   create_choice(
                                       name="spam",
                                       value='User was spamming links or incorrect words'
                                   ),
                                   create_choice(
                                       name="advertisement",
                                       value="user advertised websites, other servers or programs"
                                   ),
                                   create_choice(
                                       name="idiot",
                                       value='for being idiot'
                                   )
                               ]
                           )
                       ], guild_ids=[__main__.Config.guild_id]
    )
    @commands.has_permissions(ban_members=True)
    async def ban_user(self, ctx, user:discord.Member, reason:str):
        if user.id == ctx.author.id:
            await ctx.channel.send(f"You can not ban yourself {ctx.author.metion} !!", delete_after=15)
        elif __main__.Config.owners_name in user.roles:
            await ctx.channel.send(f"You can not ban server's owner!!! You moron. 🤦‍♀️{ctx.author.metion}", delete_after=15)
        else:
            await user.ban(reason=reason)
            await ctx.channel.send(f"User {user.mention} has been banned by {ctx.author.metion} for {reason}", delete_after=120)

    @cog_ext.cog_slash(name='kick',
                       description='kick an user',
                       options=[
                           create_option(
                               name='user',
                               description='choose user',
                               required=True,
                               option_type=6
                           ),
                           create_option(
                               name='reason',
                               description='say why you want ban this user',
                               required=True,
                               option_type=3,
                               choices=[
                                   create_choice(
                                       name="offending language",
                                       value="User used incorrect vocabullary"
                                   ),
                                   create_choice(
                                       name="spam",
                                       value='User was spamming links or incorrect words'
                                   ),
                                   create_choice(
                                       name="advertisement",
                                       value="user advertised websites, other servers or programs"
                                   ),
                                   create_choice(
                                       name="idiot",
                                       value='for being idiot'
                                   ),
                                   create_choice(
                                       name="for_fun",
                                       value="Just for fun"
                                   )
                               ]
                           )
                       ], guild_ids=[__main__.Config.guild_id]
    )
    @commands.has_permissions(kick_members=True)
    async def kick_user(self, ctx, user:discord.Member, reason:str):
        if user.id == ctx.author.id:
            await ctx.channel.send(f"You can not kick yourself, You idiot {ctx.author.metion} !!", delete_after=15)
        elif __main__.Config.owners_name in user.roles:
            await ctx.channel.send(f"You can not kick server's owner!!! You moron. 🤦‍♀️{ctx.author.metion}", delete_after=15)
        else:
            await user.kick(reason=reason)
            await ctx.channel.send(f"User {user.mention} has been banned by {ctx.author.metion} for {reason}", delete_after=120)


    @cog_ext.cog_slash(
        name='add_role',
        description='add role to user',
        options=[
            create_option(
                name='user',
                description='choose user',
                required=True,
                option_type=6
            ),
            create_option(
                name='roles',
                description='choose what role want you add to a member',
                required=True,
                option_type=3,
                choices=[
                    create_choice(
                        name='owner',
                        value='Owners'
                    ),
                    create_choice(
                        name='admin',
                        value="Admin",
                    ),
                    create_choice(
                        name='moderator',
                        value='Moderator'
                    ),
                    create_choice(
                        name='partner',
                        value='Partner'
                    ),
                ]
            )
        ], guild_ids=[__main__.Config.guild_id]
    )
    @commands.has_role(__main__.Config.owners_role_id)
    async def add_role(self, ctx, user:discord.Member, roles:str):
        if __main__.Config.owners_name not in ctx.author.roles:
            await ctx.channel.send(f'You dont have permissions to do add a role to someone {ctx.author.metion}', delete_after=15)
        elif user.roles == roles:
            await ctx.channel.send(f'{user.mention} has already this role!', delete_after=15)
        else:
            await user.add_roles(roles)


    @cog_ext.cog_slash(
        name='add_role',
        description='add role to user',
        options=[
            create_option(
                name='user',
                description='choose user',
                required=True,
                option_type=6
            ),
            create_option(
                name='roles',
                description='choose what role want you add to a member',
                required=True,
                option_type=3,
                choices=[
                    create_choice(
                        name='owner',
                        value='Owners'
                    ),
                    create_choice(
                        name='admin',
                        value="Admin",
                    ),
                    create_choice(
                        name='moderator',
                        value='Moderator'
                    ),
                    create_choice(
                        name='partner',
                        value='Partner'
                    ),
                ]
            )
        ], guild_ids=[__main__.Config.guild_id]
    )
    @commands.has_role(__main__.Config.owners_role_id)
    async def remove_role(self, ctx, user: discord.Member, roles: str):
        if __main__.Config.owners_name not in ctx.author.roles:
            await ctx.channel.send(f'You dont have permissions to do remove a role to someone {ctx.author.metion}',
                             delete_after=15)
        elif user.roles == __main__.Config.owners_name:
            await ctx.channel.send(f'You can not remove owner role from Owner', delete_after=15)
        else:
            await user.remove_roles(roles)


    @cog_ext.cog_slash(
        name='banned_users',
        description='show all banned users'
    )
    async def show_banned_users(self, ctx):
        embed = discord.Embed(title="Banned Users")
        banned = await discord.Guild.bans()
        for ban in banned:
            await embed.add_field(name=f'name: {ban.name}, id: {ban.id} ', value=f"{ban.reason}", inline=True)
        await ctx.send("Here is all banned users: \n")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Owner(bot))