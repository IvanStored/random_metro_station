from aiogram.types import Message

from config import red_line, blue_line, green_line, bot
from utils.keyboards import pagination_keyboard


def dist_between_two_lat_lon(*args) -> float:
    from math import asin, cos, radians, sin, sqrt

    lat1, lat2, long1, long2 = map(radians, args)

    dist_lats = abs(lat2 - lat1)
    dist_longs = abs(long2 - long1)
    a = (
        sin(dist_lats / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dist_longs / 2) ** 2
    )
    c = asin(sqrt(a)) * 2
    radius_earth = 6378
    return c * radius_earth


def find_closest_lat_lon(data, v) -> dict:
    try:
        return min(
            data,
            key=lambda p: dist_between_two_lat_lon(
                v["lan"], p["lan"], v["lon"], p["lon"]
            ),
        )
    except TypeError:
        print("Not a list or not a number.")


async def stations_list(
    message: Message,
    page: int = 1,
    previous_message: Message = None,
    branch: str = None,
) -> None:
    lines = None
    if branch == "red":
        lines = red_line
    if branch == "green":
        lines = green_line
    if branch == "blue":
        lines = blue_line
    await message.answer(
        text=f'{lines[page-1]["name"]}',
        reply_markup=pagination_keyboard(
            page_number=page, pages_count=len(lines), branch=branch
        ),
    )
    try:
        await bot.delete_message(
            chat_id=message.chat.id, message_id=previous_message.message_id
        )
    except Exception as e:  # noqa
        pass
