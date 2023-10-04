import asyncio,logging,GoogleDoc,config
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO, filename="bot.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")
# Объект бота
bot = Bot(config.token)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message()
async def msg(message: types.Message):
    GoogleDoc.add_data(message.chat.username,str(message.date),message.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())