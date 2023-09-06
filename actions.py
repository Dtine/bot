from aiogram import types
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from settings import dp, fatherId, list_of_commands



@dp.message(CommandStart())
async def command_start_handler(message: Message,) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    user = message.from_user
    if user.id == fatherId: 
        try:
            await message.answer("Ьуа")
        except TypeError:
            await message.answer("Не тот тип")
    else:
        await message.answer("Иди нахуй")
##@dp.message(text="/commands")
##async def echo_commands_list(message: types.Message) -> None:
    for i in list_of_commands:
        await message.answer(i)