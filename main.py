import python_weather
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5725252257:AAGNpypmBrFoCju_aXsKd7HWvjSgVsEUA6o')
dp = Dispatcher(bot)
client = python_weather.Client(unit=python_weather.IMPERIAL)


@dp.message_handler()
async def get_weather(message: types.Message):
    weather = await client.get(message.text)
    celcius = round((weather.current.temperature - 32) / 1.8)

    answer = f"The temperature is: {celcius}\n"
    answer += f"Outside is: {weather.current.description}"

    await message.answer(answer)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)