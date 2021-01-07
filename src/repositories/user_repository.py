import typing

from .irepository import IRepository
from models.user import User


class UserRepository(IRepository):
    """
    """
    def __init__(self, pool):
        self._pool = pool

    async def create(self, discord_id: int) -> None:
        async with self._pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO users(discord_id) VALUES($1)", discord_id
            )

    async def find(self, discord_id: int) -> typing.Optional[User]:
        async with self._pool.acquire() as conn:
            result = await conn.fetchrow(
                """
                SELECT discord_id,
                       balance,
                       last_hourly_bonus,
                       last_daily_bonus
                FROM users
                WHERE discord_id = $1
                """,
                discord_id
            )

        if result:
            return User(**result)

    async def update(self, user: User) -> None:
        async with self._pool.acquire() as conn:
            await conn.fetchrow(
                """
                UPDATE users
                SET balance = $2,
                    last_daily_bonus = $3,
                    last_hourly_bonus = $4
                WHERE discord_id = $1
                """,
                *vars(user).values()
            )

    async def delete(self, discord_id: str) -> None:
        async with self._pool.acquire() as conn:
            await conn.execute(
                'DELETE FROM users WHERE discord_id = $1', discord_id
            )
