import datetime


class User:
    """
    """
    def __init__(self,
        discord_id: str,
        balance: int,
        last_daily_bonus: datetime.datetime,
        last_hourly_bonus: datetime.datetime
    ):
        self.discord_id = discord_id
        self.balance = balance
        self.last_daily_bonus = last_daily_bonus
        self.last_hourly_bonus = last_hourly_bonus

