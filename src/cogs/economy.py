from discord.ext import commands

from validators.user import is_registered


class Economy(commands.Cog):

    @is_registered()
    @commands.command()
    async def balance(self, ctx):
        uid = ctx.author.id
        user = await ctx.bot.user_repository.find(uid)
        await ctx.channel.send(f'<@{uid}> Your balance is: {user.balance}')
