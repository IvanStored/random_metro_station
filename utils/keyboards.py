from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import all_lines


def make_main_kb() -> ReplyKeyboardMarkup:
    full_random = KeyboardButton(text="Повний рандом")
    choose_branch = KeyboardButton(text="Обрати гілку")
    nearest_station = KeyboardButton(text="Найближча станція метро")
    list_station = KeyboardButton(text="Список станцій")  # TODO list station
    main_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [full_random],
            [choose_branch],
            [nearest_station],
            [list_station],
        ],
        resize_keyboard=True,
    )
    return main_keyboard


def make_branch_kb(for_list: bool = False) -> InlineKeyboardMarkup:
    red_branch = InlineKeyboardButton(
        callback_data="branch_red" if not for_list else "for_list_red",
        text="🔴🔴🔴",
    )
    green_branch = InlineKeyboardButton(
        callback_data="branch_green" if not for_list else "for_list_green",
        text="🟢🟢🟢",
    )
    blue_branch = InlineKeyboardButton(
        callback_data="branch_blue" if not for_list else "for_list_blue",
        text="🔵🔵🔵",
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[red_branch], [green_branch], [blue_branch]]
    )
    return kb


def pagination_keyboard(
    page_number: int, pages_count: int, branch: str
) -> InlineKeyboardMarkup:
    left = page_number - 1 if page_number != 1 else pages_count
    right = page_number + 1 if page_number != pages_count else 1
    left_button = InlineKeyboardButton(
        text="←", callback_data=f"to {left} {branch}"
    )
    page_button = InlineKeyboardButton(
        text=f"{page_number}/{pages_count}", callback_data=" "
    )
    right_button = InlineKeyboardButton(
        text="→", callback_data=f"to {right} {branch}"
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[left_button], [page_button], [right_button]]
    )
    return kb
