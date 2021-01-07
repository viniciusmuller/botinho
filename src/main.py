from cogs.management import Management
from cogs.bonuses import Bonuses
from cogs.economy import Economy
from cogs.debug import Debug
from bot import Botinho
from secrets import TOKEN


cogs = [Management, Bonuses, Economy, Debug]
bot = Botinho(cogs, command_prefix='_')

bot.run(TOKEN)
