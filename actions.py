from aiogram.types import Message
from config import dp, fatherUsername, list_of_commands
from aiogram.filters.command import Command

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Приветик,{message.from_user.full_name}.")

@dp.message(Command("commands"))
async def command_commands_list(message: Message) -> None:
    for i in list_of_commands:
        await message.answer(i)

@dp.message(Command("myid"))
async def command_user_id(message: Message) -> None:
    user = message.from_user
    await message.answer(f"Твой ID: {str(user.id)}")


@dp.message()
async def message_handler(message: Message) -> None:
    user = message.from_user
    if str(user.id) == fatherUsername: 
        try:
            await message.answer("Ьуа")
        except TypeError:
            await message.answer("Не тот тип")
    else:
        await message.answer("Иди нахуй")