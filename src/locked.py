import functools

from discord.ext import commands


class LockedBot(commands.Bot):
    """Class used for preventing the bot from running more than
    a command from the same user at time.

    The bot will still asynchronously respond to multiple commands.
    This class was meant for working with cogs.
    """
    _lock = set()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_check(_lock_check)
        self.after_invoke(_remove_user)


async def _remove_user(ctx):
    ctx.bot._lock.remove(ctx.author.id)
    print(f'lock released from {ctx.author} after {ctx.command.name}. lock: {ctx.bot._lock}')


async def _lock_check(ctx):
    flag = ctx.author.id not in ctx.bot._lock

    if flag:
        ctx.bot._lock.add(ctx.author.id)
        print(f'{ctx.author} locked after casting {ctx.command.name}. lock: {ctx.bot._lock}')
    else:
        print(f'command from {ctx.author} was blocked by the lock.')

    return flag
