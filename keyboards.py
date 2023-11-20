from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def make_main_kb() -> ReplyKeyboardMarkup:
    full_random = KeyboardButton(text="Повний рандом")
    choose_branch = KeyboardButton(text="Обрати гілку")
    nearest_station = KeyboardButton(text="Найближча станція метро")
    list_station = KeyboardButton(text="Список станцій")  # TODO list station
    main_keyboard = ReplyKeyboardMarkup(
        keyboard=[[full_random], [choose_branch], [nearest_station]],
        resize_keyboard=True,
    )
    return main_keyboard


def make_branch_kb() -> InlineKeyboardMarkup:
    red_branch = InlineKeyboardButton(callback_data="branch_red", text="🔴🔴🔴")
    green_branch = InlineKeyboardButton(
        callback_data="branch_green", text="🟢🟢🟢"
    )
    blue_branch = InlineKeyboardButton(callback_data="branch_blue", text="🔵🔵🔵")
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[red_branch], [green_branch], [blue_branch]]
    )
    return kb
