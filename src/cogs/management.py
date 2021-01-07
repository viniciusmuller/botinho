import random
import os

import discord
from discord.ext import commands

from validators.user import is_registered, is_unregistered
from utils.commands import confirm


class Management(commands.Cog):

    @is_unregistered()
    @commands.command()
    async def register(self, ctx):
        await ctx.bot.user_repository.create(ctx.author.id)
        await ctx.send(f'<@{ctx.author.id}> succesfully registered!')

    @is_registered()
    @commands.command()
    async def unregister(self, ctx):
        confirm_emoji = '💀'
        confirm_msg = (
            'Are you sure? You will lose all your progress. '
            f'React with a \{confirm_emoji} to confirm.'
        )

        confirmation = await confirm(ctx, confirm_msg, confirm_emoji)

        if confirmation:
            await ctx.bot.user_repository.delete(ctx.message.author.id)
            await ctx.send(f'<@{ctx.author.id}> succesfully unregistered.')
