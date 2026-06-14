import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')

# ============ YOUR FILE_IDS ============
# These are the file_ids you collected - they should work!
VIDEOS = {
    'entry': 'BAACAgQAAxkBAAMnai32fmpBzqWFqQaD7cFfI3a52ccAAuAjAALUZnBR2W98zMsAAXJ8PAQ',
    'step1': 'BAACAgQAAxkBAAMZai3zqEWadKfy4DjbmOMBh1tUD6wAAtgjAALUZnBRVVSQJ61WguU8BA',
    'step2': 'BAACAgQAAxkBAAMbai3z1Af9uhhPdiCI1iGvAdzcb7YAAtkjAALUZnBRjLpc3uTcW7s8BA',
    'step3': 'BAACAgQAAxkBAAMdai3z8yHdOu-uewuYv5-jcOfDcucAAtojAALUZnBRlX6uOtEs1Co8BA',
    'step4': 'BAACAgQAAxkBAAMlai31GVmyuRTERUy7d9GRjqXLka4AAt4jAALUZnBRoK27GBTKr4w8BA',
    'step5': 'BAACAgQAAxkBAAMfai30GX9U3rJF3lrgOZoy1T1BIj0AAtsjAALUZnBRYjQpLJcy_a88BA',
    'step6': 'BAACAgQAAxkBAAMhai30lZ-uosg1_qG02voU_MHo22cAAtwjAALUZnBRm9nSaa3w3fw8BA',
    'step7': 'BAACAgQAAxkBAAMjai30s4CfTZy5TTaH6-It5hnxoIYAAt0jAALUZnBRrU3r0z8EY1U8BA'
}

LINKS = {
    'register': 'https://app.bitai.app/h5/#/pages/sign/sign?invite=888',
    'download': 'https://fr.bitai.app/app.html',
    'binance_register': 'https://accounts.binance.com/en/register?ref=1154159582',
    'binance_download': 'https://www.binance.com/en/download',
    'support': 'http://wa.me/6589691668',
    'email': 'info@bitai.app',
    'website': 'https://www.bitai.app'
}

# Messages
ENTRY_MSG = """Welcome to BitAl by Affinity AI

Most crypto traders don't lose because they lack knowledge.

They lose because manual trading is emotional, bot settings are messy, and execution comes too late.

It's time to upgrade to BitAl - built to analyze real-time market data and execute your trades automatically, 24/7."""

STEP1_MSG = """Step 1/7: Register and download BitAl

To start using BitAl, you need to register for your FREE BitAl account and download BitAl app."""

STEP2_MSG = """Step 2/7: Setting up Binance Account

To start using BitAl, you need a Binance account with KYC verification completed."""

STEP3_MSG = """Step 3/7: BitAI License Activation

To unlock BitAI's full auto AI trading, activate your BitAI License inside your BitAI app."""

STEP4_MSG = """Step 4/7: Activate & Enable Binance Futures

Before BitAI can execute, you need to activate Binance Futures inside your Binance account."""

STEP5_MSG = """Step 5/7: Set Up Your API Keys

Create your Binance API Keys and connect them to your BitAI account."""

STEP6_MSG = """Step 6/7: Transfer USDT to Binance Futures

Transfer USDT into your Binance Futures Wallet for trading."""

STEP7_MSG = """Step 7/7: Select Your Risk Profile

Choose your preferred BitAI Risk Profile based on your capital and goals.

🎯 BitAI will now trade automatically 24/7!"""

async def send_video_safe(chat_id, context, step_key, caption):
    """Safely send video with error handling"""
    try:
        video_id = VIDEOS[step_key]
        logger.info(f"Attempting to send video {step_key} with ID: {video_id[:20]}...")
        
        await context.bot.send_video(
            chat_id=chat_id,
            video=video_id,
            caption=caption,
            parse_mode='Markdown'
        )
        logger.info(f"✅ Video {step_key} sent successfully")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to send video {step_key}: {e}")
        # Send just the text as fallback
        await context.bot.send_message(chat_id=chat_id, text=caption)
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Entry point"""
    chat_id = update.effective_chat.id
    logger.info(f"User {chat_id} started the bot")
    
    # Send video first
    await send_video_safe(chat_id, context, 'entry', ENTRY_MSG)
    
    # Then buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Register my FREE BitAl account", callback_data='register')],
        [InlineKeyboardButton("Download BitAl (iOS & Android)", callback_data='download')],
        [InlineKeyboardButton("BitAl Setup Video", callback_data='step1')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

async def step1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video_safe(chat_id, context, 'step1', STEP1_MSG)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Register FREE BitAl account", url=LINKS['register'])],
        [InlineKeyboardButton("Download BitAl", url=LINKS['download'])],
        [InlineKeyboardButton("Skip to Setting up Binance Account", callback_data='step2')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Step 1/7:", reply_markup=keyboard)

async def step2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video_safe(chat_id, context, 'step2', STEP2_MSG)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Create a FREE Binance account", url=LINKS['binance_register'])],
        [InlineKeyboardButton("Download Binance", url=LINKS['binance_download'])],
        [InlineKeyboardButton("Skip to License Activation", callback_data='step3')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Step 2/7:", reply_markup=keyboard)

async def step3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video_safe(chat_id, context, 'step3', STEP3_MSG)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to Activate & Enable Binance Futures", callback_data='step4')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Step 3/7:", reply_markup=keyboard)

async def step4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video_safe(chat_id, context, 'step4', STEP4_MSG)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to setting API Keys", callback_data='step5')],
        [InlineKeyboardButton("Back to previous step", callback_data='step3')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Step 4/7:", reply_markup=keyboard)

async def step5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video_safe(chat_id, context, 'step5', STEP5_MSG)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to Transferring USDT", callback_data='step6')],
        [InlineKeyboardButton("Back to previous step", callback_data='step4')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Step 5/7:", reply_markup=keyboard)

async def step6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video_safe(chat_id, context, 'step6', STEP6_MSG)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to Select Risk Profile", callback_data='step7')],
        [InlineKeyboardButton("Back to previous step", callback_data='step5')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Step 6/7:", reply_markup=keyboard)

async def step7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video_safe(chat_id, context, 'step7', STEP7_MSG)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Back to previous step", callback_data='step6')],
        [InlineKeyboardButton("Website", url=LINKS['website'])],
        [InlineKeyboardButton("Email support", url=f"mailto:{LINKS['email']}")],
        [InlineKeyboardButton("Contact support", url=LINKS['support'])],
        [InlineKeyboardButton("Exit Conversation", callback_data='exit')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Step 7/7 - Setup Complete!", reply_markup=keyboard)

async def handle_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Register here: {LINKS['register']}")

async def handle_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Download BitAl: {LINKS['download']}")

async def handle_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Contact support: {LINKS['support']}")

async def handle_exit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Conversation ended. Send /start to begin again.")

def main():
    logger.info("🚀 Starting BitAl Bot...")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start))
    
    # Callbacks
    app.add_handler(CallbackQueryHandler(handle_register, pattern='^register$'))
    app.add_handler(CallbackQueryHandler(handle_download, pattern='^download$'))
    app.add_handler(CallbackQueryHandler(handle_support, pattern='^support$'))
    app.add_handler(CallbackQueryHandler(handle_exit, pattern='^exit$'))
    app.add_handler(CallbackQueryHandler(step1, pattern='^step1$'))
    app.add_handler(CallbackQueryHandler(step2, pattern='^step2$'))
    app.add_handler(CallbackQueryHandler(step3, pattern='^step3$'))
    app.add_handler(CallbackQueryHandler(step4, pattern='^step4$'))
    app.add_handler(CallbackQueryHandler(step5, pattern='^step5$'))
    app.add_handler(CallbackQueryHandler(step6, pattern='^step6$'))
    app.add_handler(CallbackQueryHandler(step7, pattern='^step7$'))
    
    logger.info("✅ Bot handlers registered. Starting polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
