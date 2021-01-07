from discord.ext import commands


class Debug(commands.Cog):
    """
    """
    async def cog_check(self, ctx):
        return commands.is_owner()

    @commands.command()
    async def drop_table(self, ctx, table: str):
        async with ctx.bot.user_repository._pool.acquire() as conn:
            await conn.execute(
                f'DROP TABLE {table}'
            )
        await ctx.send(f'Table {table} dropped.')

    @commands.command()
    async def add_funds(self, ctx, *, num: int):
        user = await ctx.bot.user_repository.find(ctx.author.id)
        user.balance += num
        await ctx.bot.user_repository.update(user)
