import asyncio
import logging
import sys
from handlers import callback_handlers, message_handlers

from config import dp, bot


async def main():
    dp.include_routers(callback_handlers.router, message_handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
