import asyncio

import discord
from discord.ext import commands


class HelpCommand(commands.MinimalHelpCommand):
    """
    TODO improve embed and fix registrated user error on help command
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Don't perform a check on each command
        # in order to send a help message
        self.verify_checks = False

    async def send_pages(self):
        destination = self.get_destination()

        e = discord.Embed(
            color=discord.Color(0x814bde),
            title='The commands!',
            description='\n'.join(self.paginator.pages)
        )
        await destination.send(embed=e)


async def confirm(ctx, message: str, emoji: str, timeout: float = 30.0) -> bool:
    """
    TODO add cancel option
    """
    confirm_msg = await ctx.send(message)
    await confirm_msg.add_reaction(emoji)

    def check(reaction, user):
        return user == ctx.author and \
            str(reaction.emoji) == emoji and \
            reaction.message == confirm_msg

    try:
        await ctx.bot.wait_for('reaction_add', timeout=timeout, check=check)
    except asyncio.TimeoutError:
        return False
    else:
        return True
