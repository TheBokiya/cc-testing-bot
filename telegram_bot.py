import json
import random
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load messages from JSON file
def load_messages(filename):
    with open(filename, 'r') as f:
        return json.load(f)

messages = load_messages('messages.json')

# Command handler for /random_sales
async def random_sales_message(update, context: ContextTypes.DEFAULT_TYPE):
    sales_list = messages.get('sales', [])
    if sales_list:
        msg = random.choice(sales_list)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No sales messages available.")

# Command handler for /shift_handover
async def shift_handover_message(update, context: ContextTypes.DEFAULT_TYPE):
    msg = messages.get('shift_handover', "No shift handover message available.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

# Main function to start the bot
def main():
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("Error: BOT_TOKEN not found in .env file.")
        return
    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler('random_sales', random_sales_message))
    app.add_handler(CommandHandler('shift_handover', shift_handover_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
