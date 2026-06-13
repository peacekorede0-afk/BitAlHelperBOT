import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment
BOT_TOKEN = os.getenv('FILE_ID_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when /start is issued."""
    welcome_message = """
🎥 *Video File ID Bot Ready!*

Simply send me any video file, and I will reply with its `file_id`.

You can send the video as:
- Regular video
- Video as document/file

*How to use:*
1. Send me a video
2. Copy the `file_id` from my reply
3. Paste it into your main bot's code

Made for BitAl Bot Setup
    """
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle video messages and return the file_id."""
    video = update.message.video
    if video:
        file_id = video.file_id
        file_unique_id = video.file_unique_id
        
        response = f"""
✅ *Video Received!*

📹 *file_id:* 
`{file_id}`

🆔 *file_unique_id:* 
`{file_unique_id}`

---
*Copy the first `file_id`* and paste it into your main bot's code.
        """
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"Sent file_id for video to user {update.effective_user.id}")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle document messages that are videos."""
    document = update.message.document
    if document and document.mime_type and document.mime_type.startswith('video/'):
        file_id = document.file_id
        file_unique_id = document.file_unique_id
        
        response = f"""
✅ *Video Document Received!*

📹 *file_id:* 
`{file_id}`

🆔 *file_unique_id:* 
`{file_unique_id}`

---
*Copy the first `file_id`* and paste it into your main bot's code.
        """
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"Sent file_id for video document to user {update.effective_user.id}")
    else:
        await update.message.reply_text("📄 Document received, but it's not a video file.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message."""
    help_text = """
*How to use this bot:*

1. Send me a video (as video or file)
2. I'll reply with the `file_id`
3. Copy that ID to use in your main bot

*Commands:*
/start - Welcome message
/help - This help message
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Add message handlers
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Start the bot
    print("🤖 File ID Bot is running...")
    print("Send videos to get their file_id")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
