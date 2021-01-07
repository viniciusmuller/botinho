import functools

from discord.ext import commands


class LockedBot(commands.Bot):
    """Class used for preventing the bot from running more than
    a command from the same user at time.

    The bot will still asynchronously respond to multiple commands.
    This class was meant for working with cogs.
    """
    _lock = set()

    def __init__(self, lock_debug=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO use logger
        self._lock_debug = lock_debug
        self.add_check(_lock_check)
        self.before_invoke(_lock_user)
        self.after_invoke(_release_user)


async def _lock_user(ctx):
    ctx.bot._lock.add(ctx.author.id)

    if ctx.bot._lock_debug:
        print(
            f'{ctx.author} locked after casting '
            f'{ctx.command.name}. lock: {ctx.bot._lock}'
        )


async def _release_user(ctx):
    ctx.bot._lock.remove(ctx.author.id)
    if ctx.bot._lock_debug:
        print(
            f'lock released from {ctx.author} after '
            f'{ctx.command.name}. lock: {ctx.bot._lock}'
        )


async def _lock_check(ctx):
    flag = ctx.author.id not in ctx.bot._lock

    if not flag and ctx.bot._lock_debug:
        print(f'command from {ctx.author} was blocked by the lock.')

    return flag
