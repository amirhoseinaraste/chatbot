import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from nltk.chat.util import Chat, reflections

# Define the chatbot conversation pairs
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today?"]],
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    [r"(.*) relationship (.*)", ["It seems like you're talking about relationships. Can you tell me more?"]],
    [r"how are you?", ["I'm good, how about you?"]],
    [r"sorry (.*)", ["It's okay, no problem at all."]],
    [r"quit", ["Bye! Take care. See you soon!"]],
]

# Create a chatbot instance using nltk
chatbot = Chat(pairs, reflections)

# Define a function to handle user messages
async def handle_message(update: Update, context):
    user_message = update.message.text
    logging.info(f"Received message: {user_message}")  # Log the received message
    reply = chatbot.respond(user_message)
    if reply:
        await update.message.reply_text(reply)
    else:
        await update.message.reply_text("Sorry, I didn't understand that.")

# Define a function for the /start command
async def start(update: Update, context):
    await update.message.reply_text("Hi! I'm your chatbot. Type your message to start a conversation!")

# Error handler function
async def error_handler(update: Update, context):
    logging.error(f"An error occurred: {context.error}")

# Main function to run the Telegram bot
def main():
    # Insert your token from BotFather here
    TOKEN = "6439487075:AAHq3pNOIpZlnI0ZMw_XspW0Yj-Nfv2mtf8"

    # Create the application
    application = ApplicationBuilder().token(TOKEN).build()

    # Log all errors
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

    # Add handlers one by one
    application.add_handler(CommandHandler("start", start))  # Command handler for /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Message handler for text

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
