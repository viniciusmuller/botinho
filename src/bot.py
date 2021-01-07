import typing
import random
import ssl
import os

from discord.ext import tasks, commands
import discord

from repositories.user_repository import UserRepository
from database import pg_connection
from utils.commands import HelpCommand
from errors.handler import handle
from secrets import DATABASE_URL
from locked import LockedBot


class Apostador(LockedBot):
    """
    """
    def __init__(self, cogs: typing.List[commands.Cog], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.on_command_error = handle
        self.help_command = HelpCommand()

        for cog in cogs:
            self.add_cog(cog())

    async def setup(self):
        ctx = pg_connection.get_ssl_ctx()
        pool = await pg_connection.get_pool(DATABASE_URL, max_size=20, ssl=ctx)
        self.user_repository = UserRepository(pool)
        self.rotate_status.start()

    async def on_ready(self):
        """
        """
        await self.setup()
        print(f'Online! Currently serving {len(self.guilds)} servers.')

    @tasks.loop(seconds=60.0)
    async def rotate_status(self):
        pesos = ['status1', 'status2', 'status3', 'status4']
        pesado = random.choice(pesos)
        await self.change_presence(activity=discord.Game(name=pesado))
