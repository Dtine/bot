from aiogram import Bot, Dispatcher, Router
from magic_filter import MagicFilter
TOKEN = "6512694498:AAF0C4bVIQ-h8xqyNcHBeEWTPYEsqdZoNt8"

bot = Bot(TOKEN)
dp = Dispatcher()
fatherId = "1371204466"
list_of_commands = ["/commands","/myid"]
F = MagicFilter