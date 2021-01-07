from discord.ext.commands import errors


IGNORED_EXCEPTIONS = (errors.CommandNotFound, errors.CheckFailure)

async def handle(ctx, error):
    if isinstance(error, IGNORED_EXCEPTIONS):
        return
    else:
        raise error
