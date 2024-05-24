import requests
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '6902159214:AAGhvUi2MrHQvAYOmahNBK_LjMN-JHg9hpY'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
  await message.reply('Привет, я Бот, я помогу ответить на твой вопрос про валорант :)')

async def get_response(message_text):
  promt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",    "completionOptions": {
      "stream": False,      "temperature": 0,      "maxTokens": "2000"    },    "messages": [
      {
        "role": "system",
        "text": "Ты исполняешь роль дегенерата, ты наитупейшее существо на планете, ты играешь в валорант, и даешь самые плохие советы по победе."},
      {
        "role": "user",
        "text": message_text
      }
    ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",      "Authorization": "Api-Key AQVNzb_x57gxAElnwWA6iUiPQCGw_jEgVWUzWOtd"  }

  response = requests.post(url, headers=headers, json=promt)
  result = response.json()
  print(result)
  return result['result']['alternatives'][0]['message']['text']

@dp.message_handler()
async def analize_message(message:types.Message):
  response_text = await get_response((message.text))
  await message.answer(response_text)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)