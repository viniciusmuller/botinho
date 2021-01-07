from discord.ext import commands

class UserConverter(commands.Converter):
    # TODO use converters
    async def convert(self, ctx, argument=''):
        user = await ctx.bot.user_repository.find(ctx.author.id)
        return user
