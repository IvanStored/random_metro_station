import logging
import random

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import all_lines, bot
from utils.helpers import find_closest_lat_lon
from utils.keyboards import make_branch_kb, make_main_kb

router = Router()


@router.message(
    lambda message: message.text in ["Обрати гілку", "Список станцій"]
)
async def choose_branch(message: Message) -> None:
    for_list = False
    if message.text == "Список станцій":
        for_list = True
    await message.answer(
        text="Обери бажану гілку:",
        reply_markup=make_branch_kb(for_list=for_list),
    )


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text="Привіт, цей бот допоможе тобі обрати станцію метро, якщо ти не знаєш, де погуляти.",
    )

    await message.answer(
        text="Для керування використовуй меню снизу. Також працює пошук за назвою.",
        reply_markup=make_main_kb(),
    )


@router.message(lambda message: message.text == "Повний рандом")
async def full_random_station(message: Message) -> None:
    random_station = random.choice(all_lines)
    await bot.send_location(
        chat_id=message.chat.id,
        latitude=random_station["lan"],
        longitude=random_station["lon"],
    )
    await message.answer(text=random_station["name"])


@router.message(lambda message: message.text == "Найближча станція метро")
async def handle_user_location(message: Message) -> None:
    await message.answer(
        text="Для пошуку найближчої станції надішліть своє місцезнаходження"
    )


@router.message(lambda message: message.content_type in ["location", "venue"])
async def nearest_metro_station(message: Message) -> None:
    lan = message.location.latitude
    lon = message.location.longitude
    all_stations = all_lines
    station = find_closest_lat_lon(
        data=all_stations, v={"lan": lan, "lon": lon}
    )
    await message.answer(
        text=f"Найближча до вас станція - {station['name']}",
    )
    await bot.send_location(
        chat_id=message.chat.id,
        latitude=station["lan"],
        longitude=station["lon"],
    )


@router.message()
async def echo_handler(message: Message) -> Message:
    try:
        for station in all_lines:
            if (
                message.text.lower()
                in "".join(
                    char
                    for char in station["name"]
                    if char.isalpha() or char == " "
                ).lower()
            ):
                await bot.send_location(
                    chat_id=message.chat.id,
                    latitude=station["lan"],
                    longitude=station["lon"],
                )
                return await message.answer(
                    text=station["name"],
                    reply_markup=make_main_kb(),
                )

    except Exception:
        logging.error(message.content_type)
        await message.answer("Nice try!")

    else:
        await message.answer(message.text)
