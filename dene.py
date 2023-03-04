import asyncio
import telegram

async def main():
    bot = telegram.Bot(token='6238865786:AAHVx63r7uVI2PZ5s2GBMiSDekOdynXjrw4')
    chat_id = '1318815790'
    message_text = 'Merhaba! Bu bir test mesajıdır.'

    async with bot:
        await bot.send_message(chat_id=chat_id, text=message_text)

if __name__ == '__main__':
    asyncio.run(main())
print("Sa")