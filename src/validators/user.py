from discord.ext import commands


async def _is_registered(ctx):
    user = await ctx.bot.user_repository.find(ctx.author.id)
    if user is None:
        await ctx.send('You must be registered in order to use this command!')
        return False
    return True


async def _is_unregistered(ctx):
    user = await ctx.bot.user_repository.find(ctx.author.id)
    if user:
        await ctx.send("You can't use this command while registered.")
        return False
    return True


# API wrappers
def is_registered():
    return commands.check(_is_registered)

def is_unregistered():
    return commands.check(_is_unregistered)
