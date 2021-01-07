import datetime
import random
import os

from discord.ext import commands

from validators.user import is_registered


class Bonuses(commands.Cog):
    """ """

    async def cog_check(self, _ctx):
        return is_registered()

    @commands.command()
    async def daily(self, ctx):
        bonus = random.randint(400, 500)
        one_day = datetime.timedelta(days=1)
        await parse_bonus(ctx, 'last_daily_bonus', one_day, bonus)

    @commands.command()
    async def hourly(self, ctx):
        bonus = random.randint(40, 70)
        one_hour = datetime.timedelta(hours=1)
        await parse_bonus(ctx, 'last_hourly_bonus', one_hour, bonus)


async def parse_bonus(ctx, field: str, delay: datetime.datetime, bonus: int):
    """ """
    uid = ctx.author.id
    user = await ctx.bot.user_repository.find(uid)
    user_last_bonus = getattr(user, field)

    if is_bonus_available(user_last_bonus, delay):
        await available_bonus_msg(ctx, user, field, bonus)
    else:
        await unavailable_bonus_msg(ctx, user_last_bonus, delay)


def is_bonus_available(
    last_time: datetime.datetime,
    delay: datetime.datetime
) -> bool:
    """ """
    now = datetime.datetime.utcnow()
    return last_time is None or (now - delay) > last_time


async def available_bonus_msg(ctx, user, field: str, bonus: int) -> None:
    """ """
    now = datetime.datetime.utcnow()
    user.balance += bonus
    setattr(user, field, now)
    await ctx.bot.user_repository.update(user)
    await ctx.send(f'{ctx.author.name} redeemed {bonus} coins!')


async def unavailable_bonus_msg(
    ctx,
    last_time: datetime.datetime,
    delay: datetime.datetime
) -> None:
    """ """
    now = datetime.datetime.utcnow()
    remaining_time = last_time - now + delay
    await ctx.send(
        f'<@{ctx.author.id}>, you need to wait '
        f'{remaining_time} until the next bonus!'
    )
