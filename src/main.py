from cogs.management import Management
from cogs.bonuses import Bonuses
from cogs.economy import Economy
from cogs.debug import Debug
from bot import Apostador
from secrets import TOKEN


cogs = [Management, Bonuses, Economy, Debug]
bot = Apostador(cogs, command_prefix='_')

bot.run(TOKEN)
