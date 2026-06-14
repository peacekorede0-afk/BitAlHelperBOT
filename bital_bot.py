import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')

# ============ YOUR FILE_IDS (Direct video playback) ============
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

# ============ LINKS ============
REGISTER_LINK = 'https://app.bitai.app/h5/#/pages/sign/sign?invite=888'
DOWNLOAD_BITAL = 'https://fr.bitai.app/app.html'
BINANCE_REGISTER = 'https://accounts.binance.com/en/register?ref=1154159582'
BINANCE_DOWNLOAD = 'https://www.binance.com/en/download'
SUPPORT_WA = 'http://wa.me/6589691668'
EMAIL_SUPPORT = 'info@bitai.app'
WEBSITE = 'https://www.bitai.app'

# ============ MESSAGES (Exactly from PDF) ============
ENTRY_MESSAGE = """Welcome to BitAl by Affinity AI

Most crypto traders don't lose because they lack knowledge.

They lose because manual trading is emotional, bot settings are messy, and execution comes too late.

It's time to upgrade to BitAl - built to analyze real-time market data and execute your trades automatically, 24/7."""

STEP1_MESSAGE = """Step 1/7: Register and download BitAl

To start using BitAl, you need to register for your FREE BitAl account and download BitAl app. If you are referred by our BitAl user, please use their referral link to register."""

STEP2_MESSAGE = """Step 2/7: Setting up Binance Account

To start using BitAl, you need a Binance account with KYC verification completed.

Already have a verified Binance account? You may skip this video and continue to BitAI License Activation."""

STEP3_MESSAGE = """Step 3/7: BitAI License Activation

To unlock BitAI's full auto AI trading, activate your BitAI License inside your BitAI app. Once activated, you can proceed to activate & enable your Binance Futures."""

STEP4_MESSAGE = """Step 4/7: Activate & Enable Binance Futures

Before BitAI can execute, you need to activate Binance Futures inside your Binance account.

Once Futures is enabled, you can continue to the next step and create your Binance API connection."""

STEP5_MESSAGE = """Step 5/7: Set Up Your API Keys

Next, create your Binance API Keys and connect them to your BitAI account.

This allows BitAI to analyze real-time market data and execute based on your selected risk profile.

Make sure your API Keys are kept private and only connected inside the official BitAI platform."""

STEP6_MESSAGE = """Step 6/7: Transfer USDT to Binance Futures

Before BitAI can execute, make sure your USDT is transferred into your own Binance Futures Wallet.

This will be the capital used for BitAI's AI-driven execution based on your selected risk profile.

Once completed, continue to Select Risk Profile."""

STEP7_MESSAGE = """Step 7/7: Select Your Risk Profile

Choose your preferred BitAI Risk Profile based on your capital, goals, and risk appetite.

BitAI will execute according to the risk level you select.

Once done, BitAI will start to analyze real time market data and execute your trades automatically!"""

# ============ BOT HANDLERS ============

async def send_video(chat_id, context, step, message):
    """Helper to send video with caption"""
    try:
        await context.bot.send_video(
            chat_id=chat_id,
            video=VIDEOS[step],
            caption=message,
            parse_mode='Markdown'
        )
        logger.info(f"Sent video for {step}")
    except Exception as e:
        logger.error(f"Failed to send video {step}: {e}")
        await context.bot.send_message(chat_id=chat_id, text=message)

# Entry Message Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Entry message with 4 buttons"""
    chat_id = update.effective_chat.id
    
    await send_video(chat_id, context, 'entry', ENTRY_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Register my FREE BitAl account", callback_data='register')],
        [InlineKeyboardButton("Download BitAl (iOS & Android)", callback_data='download')],
        [InlineKeyboardButton("BitAl Setup Video", callback_data='step1')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Step 1 Handler
async def step1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Step 1/7 with 4 buttons"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video(chat_id, context, 'step1', STEP1_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Register FREE BitAl account", url=REGISTER_LINK)],
        [InlineKeyboardButton("Download BitAl", url=DOWNLOAD_BITAL)],
        [InlineKeyboardButton("Skip to Setting up Binance Account", callback_data='step2')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Step 2 Handler
async def step2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Step 2/7 with 4 buttons"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video(chat_id, context, 'step2', STEP2_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Create a FREE Binance account", url=BINANCE_REGISTER)],
        [InlineKeyboardButton("Download Binance (iOS & Android)", url=BINANCE_DOWNLOAD)],
        [InlineKeyboardButton("Skip to License Activation", callback_data='step3')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Step 3 Handler
async def step3_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Step 3/7 with 2 buttons"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video(chat_id, context, 'step3', STEP3_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to Activate & Enable Binance Futures", callback_data='step4')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Step 4 Handler
async def step4_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Step 4/7 with 3 buttons (including Back)"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video(chat_id, context, 'step4', STEP4_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to setting API Keys", callback_data='step5')],
        [InlineKeyboardButton("Back to previous step", callback_data='step3')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Step 5 Handler
async def step5_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Step 5/7 with 3 buttons"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video(chat_id, context, 'step5', STEP5_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to Transferring USDT to Binance Futures", callback_data='step6')],
        [InlineKeyboardButton("Back to previous step", callback_data='step4')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Step 6 Handler
async def step6_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Step 6/7 with 3 buttons"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video(chat_id, context, 'step6', STEP6_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Skip to Select Risk Profile", callback_data='step7')],
        [InlineKeyboardButton("Back to previous step", callback_data='step5')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Step 7 Handler
async def step7_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Step 7/7 with 5 buttons (including Exit)"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await send_video(chat_id, context, 'step7', STEP7_MESSAGE)
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Back to previous step", callback_data='step6')],
        [InlineKeyboardButton("Website", url=WEBSITE)],
        [InlineKeyboardButton("Email support", url=f"mailto:{EMAIL_SUPPORT}")],
        [InlineKeyboardButton("Contact support", url=SUPPORT_WA)],
        [InlineKeyboardButton("Exit Conversation", callback_data='exit')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

# Support Handler
async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Contact support button"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"Contact support via WhatsApp: {SUPPORT_WA}\n\nOr email: {EMAIL_SUPPORT}"
    )

# Register Handler
async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Register button"""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Register here: {REGISTER_LINK}")

# Download Handler
async def download_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Download button"""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"Download BitAl: {DOWNLOAD_BITAL}")

# Exit Handler
async def exit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Exit conversation"""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Conversation ended. Type /start to begin again.")

# Main function
def main():
    logger.info("Starting BitAl Bot...")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command handler
    app.add_handler(CommandHandler("start", start))
    
    # Callback handlers (matches PDF buttons exactly)
    app.add_handler(CallbackQueryHandler(register_handler, pattern='^register$'))
    app.add_handler(CallbackQueryHandler(download_handler, pattern='^download$'))
    app.add_handler(CallbackQueryHandler(support_handler, pattern='^support$'))
    app.add_handler(CallbackQueryHandler(exit_handler, pattern='^exit$'))
    app.add_handler(CallbackQueryHandler(step1_handler, pattern='^step1$'))
    app.add_handler(CallbackQueryHandler(step2_handler, pattern='^step2$'))
    app.add_handler(CallbackQueryHandler(step3_handler, pattern='^step3$'))
    app.add_handler(CallbackQueryHandler(step4_handler, pattern='^step4$'))
    app.add_handler(CallbackQueryHandler(step5_handler, pattern='^step5$'))
    app.add_handler(CallbackQueryHandler(step6_handler, pattern='^step6$'))
    app.add_handler(CallbackQueryHandler(step7_handler, pattern='^step7$'))
    
    logger.info("Bot is ready! Starting polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
