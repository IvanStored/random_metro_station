import asyncio
import logging
import random
import sys
from handlers import callback_handlers, message_handlers
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import dp, bot, red_line, green_line, blue_line, all_lines
from utils.keyboards import make_main_kb, make_branch_kb

# from utils import find_closest_lat_lon


# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(
#         text="Привіт, цей бот допоможе тобі обрати станцію метро, якщо ти не знаєш, де погуляти.",
#     )
#
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text="Для керування використовуй меню снизу. Також працює пошук за назвою.",
#         reply_markup=make_main_kb(),
#     )
#
#
# @dp.message(lambda message: message.text == "Повний рандом")
# async def full_random_station(message: Message) -> None:
#     random_station = random.choice(all_lines)
#     await bot.send_location(
#         chat_id=message.chat.id,
#         latitude=random_station["lan"],
#         longitude=random_station["lon"],
#     )
#     await bot.send_message(
#         chat_id=message.chat.id, text=random_station["name"]
#     )
#
#
# @dp.message(lambda message: message.text == "Найближча станція метро")
# async def handle_user_location(message: Message) -> None:
#     await message.answer(
#         text="Для пошуку найближчої станції надішліть своє місцезнаходження"
#     )
#
#
# @dp.message(lambda message: message.content_type in ["location", "venue"])
# async def nearest_metro_station(message: Message) -> None:
#     lan = message.location.latitude
#     lon = message.location.longitude
#     all_stations = all_lines
#     station = find_closest_lat_lon(
#         data=all_stations, v={"lan": lan, "lon": lon}
#     )
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text=f"Найближча до вас станція - {station['name']}",
#     )
#     await bot.send_location(
#         chat_id=message.chat.id,
#         latitude=station["lan"],
#         longitude=station["lon"],
#     )


# @dp.message(lambda message: message.text in ["Обрати гілку", "Список станцій"])
# async def choose_branch(message: Message) -> None:
#     for_list = False
#     if message.text == "Список станцій":
#         for_list = True
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text="Обери бажану гілку:",
#         reply_markup=make_branch_kb(for_list=for_list),
#     )

# @dp.callback_query(lambda callback: callback.data.startswith("branch"))
# async def not_full_random_station(callback: CallbackQuery) -> None:
#     await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
#     if "red" in callback.data:
#         station = random.choice(red_line)
#         await bot.send_location(
#             chat_id=callback.message.chat.id,
#             latitude=station["lan"],
#             longitude=station["lon"],
#         )
#         await bot.send_message(
#             chat_id=callback.message.chat.id, text=station["name"]
#         )
#     elif "green" in callback.data:
#         station = random.choice(green_line)
#         await bot.send_location(
#             chat_id=callback.message.chat.id,
#             latitude=station["lan"],
#             longitude=station["lon"],
#         )
#         await bot.send_message(
#             chat_id=callback.message.chat.id, text=station["name"]
#         )
#     else:
#         station = random.choice(blue_line)
#         await bot.send_location(
#             chat_id=callback.message.chat.id,
#             latitude=station["lan"],
#             longitude=station["lon"],
#         )
#         await bot.send_message(
#             chat_id=callback.message.chat.id, text=station["name"]
#         )


# async def stations_list(
#     message: Message, page: int = 1, previous_message: Message = None, branch: str = None
# ) -> None:
#     lines = None
#     if branch == "red":
#         lines = red_line
#     if branch == "green":
#         lines = green_line
#     if branch == "blue":
#         lines = blue_line
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text=f'{lines[page-1]["name"]}',
#         reply_markup=pagination_keyboard(page_number=page, pages_count=len(lines), branch=branch),
#     )
#     try:
#         await bot.delete_message(chat_id=message.chat.id, message_id=previous_message.message_id)
#     except Exception as e :
#         logging.error(e)
#         pass
# @dp.callback_query(lambda callback: callback.data.startswith("for_list"))
# async def all_stations_list(callback: CallbackQuery):
#     if "red" in callback.data:
#         await stations_list(message=callback.message, previous_message=callback.message, branch="red")
#     elif "green" in callback.data:
#         await stations_list(message=callback.message, previous_message=callback.message, branch="green")
#     else:
#         await stations_list(message=callback.message, previous_message=callback.message, branch="blue")
#
# @dp.callback_query(lambda callback: callback.data.startswith("to"))
# async def pagination_callback(callback: CallbackQuery):
#     page = int(callback.data.split(" ")[1])
#     branch = callback.data.split(" ")[-1]
#     await stations_list(
#         message=callback.message, page=page, previous_message=callback.message, branch=branch
#     )


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         for station in all_lines:
#             if (
#                 message.text.lower()
#                 in "".join(
#                     char
#                     for char in station["name"]
#                     if char.isalpha() or char == " "
#                 ).lower()
#             ):
#                 await bot.send_location(
#                     chat_id=message.chat.id,
#                     latitude=station["lan"],
#                     longitude=station["lon"],
#                 )
#                 return await bot.send_message(
#                     chat_id=message.chat.id,
#                     text=station["name"],
#                     reply_markup=make_main_kb(),
#                 )
#
#     except Exception:
#         logging.error(message.content_type)
#         await message.answer("Nice try!")
#
#     else:
#         await message.answer(message.text)


async def main():
    dp.include_routers(callback_handlers.router, message_handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
