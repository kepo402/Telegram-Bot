import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters, ApplicationBuilder
import sys

if sys.platform.startswith('win'):
      asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

nest_asyncio.apply()     
async def start(update: Update, _) -> None:
        await update.message.reply_text(f"Hello {update.effective_user.first_name}, how can i help you today?")

async def handle_message(update: Update, context) -> None:
      await update.message.reply_text("Wait, my boss will attend to you shortly")
      user_message = update.message.text
              
async def main():
     app = ApplicationBuilder().token(API-KEY).build()

     app.add_handler(CommandHandler("start", start))
     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
     await app.run_polling()
    
if __name__ == "__main__":
      asyncio.run(main())


 