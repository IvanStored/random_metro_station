import random

from aiogram import Router
from aiogram.types import CallbackQuery

from config import bot, red_line, green_line, blue_line
from utils.helpers import stations_list

router = Router()


@router.callback_query(lambda callback: callback.data.startswith("for_list"))
async def all_stations_list(callback: CallbackQuery):
    if "red" in callback.data:
        await stations_list(
            message=callback.message,
            previous_message=callback.message,
            branch="red",
        )
    elif "green" in callback.data:
        await stations_list(
            message=callback.message,
            previous_message=callback.message,
            branch="green",
        )
    else:
        await stations_list(
            message=callback.message,
            previous_message=callback.message,
            branch="blue",
        )


@router.callback_query(lambda callback: callback.data.startswith("to"))
async def pagination_callback(callback: CallbackQuery):
    page = int(callback.data.split(" ")[1])
    branch = callback.data.split(" ")[-1]
    await stations_list(
        message=callback.message,
        page=page,
        previous_message=callback.message,
        branch=branch,
    )


@router.callback_query(lambda callback: callback.data.startswith("branch"))
async def not_full_random_station(callback: CallbackQuery) -> None:
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
    )
    if "red" in callback.data:
        station = random.choice(red_line)
        await bot.send_location(
            chat_id=callback.message.chat.id,
            latitude=station["lan"],
            longitude=station["lon"],
        )
        await bot.send_message(
            chat_id=callback.message.chat.id, text=station["name"]
        )
    elif "green" in callback.data:
        station = random.choice(green_line)
        await bot.send_location(
            chat_id=callback.message.chat.id,
            latitude=station["lan"],
            longitude=station["lon"],
        )
        await bot.send_message(
            chat_id=callback.message.chat.id, text=station["name"]
        )
    else:
        station = random.choice(blue_line)
        await bot.send_location(
            chat_id=callback.message.chat.id,
            latitude=station["lan"],
            longitude=station["lon"],
        )
        await bot.send_message(
            chat_id=callback.message.chat.id, text=station["name"]
        )
