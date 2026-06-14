import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')

# ============ LINKS ============
LINKS = {
    'register': 'https://app.bitai.app/h5/#/pages/sign/sign?invite=888',
    'download': 'https://fr.bitai.app/app.html',
    'binance_register': 'https://accounts.binance.com/en/register?ref=1154159582',
    'binance_download': 'https://www.binance.com/en/download',
    'support': 'http://wa.me/6589691668',
    'email': 'info@bitai.app',
    'website': 'https://www.bitai.app'
}

# ============ TEMPORARY: Store file_ids as we capture them ============
# Send each video to this bot, it will show you the correct file_id
# Then replace these placeholders
VIDEOS = {
    'entry': 'WAITING_FOR_VIDEO_SEND_ENTRY_TO_BOT',
    'step1': 'WAITING_FOR_VIDEO_SEND_STEP1_TO_BOT',
    'step2': 'WAITING_FOR_VIDEO_SEND_STEP2_TO_BOT',
    'step3': 'WAITING_FOR_VIDEO_SEND_STEP3_TO_BOT',
    'step4': 'WAITING_FOR_VIDEO_SEND_STEP4_TO_BOT',
    'step5': 'WAITING_FOR_VIDEO_SEND_STEP5_TO_BOT',
    'step6': 'WAITING_FOR_VIDEO_SEND_STEP6_TO_BOT',
    'step7': 'WAITING_FOR_VIDEO_SEND_STEP7_TO_BOT'
}

# ============ MESSAGES ============
ENTRY_MSG = """Welcome to BitAl by Affinity AI 🚀

Most crypto traders don't lose because they lack knowledge.

They lose because manual trading is emotional, bot settings are messy, and execution comes too late.

It's time to upgrade to BitAl - built to analyze real-time market data and execute your trades automatically, 24/7."""

STEP1_MSG = """Step 1/7: Register and download BitAl

To start using BitAl, you need to register for your FREE BitAl account and download BitAl app. If you are referred by our BitAl user, please use their referral link to register."""

STEP2_MSG = """Step 2/7: Setting up Binance Account

To start using BitAl, you need a Binance account with KYC verification completed.

Already have a verified Binance account? You may skip this video and continue to BitAI License Activation."""

STEP3_MSG = """Step 3/7: BitAI License Activation

To unlock BitAI's full auto AI trading, activate your BitAI License inside your BitAI app. Once activated, you can proceed to activate & enable your Binance Futures."""

STEP4_MSG = """Step 4/7: Activate & Enable Binance Futures

Before BitAI can execute, you need to activate Binance Futures inside your Binance account.

Once Futures is enabled, you can continue to the next step and create your Binance API connection."""

STEP5_MSG = """Step 5/7: Set Up Your API Keys

Next, create your Binance API Keys and connect them to your BitAI account.

This allows BitAI to analyze real-time market data and execute based on your selected risk profile.

Make sure your API Keys are kept private and only connected inside the official BitAI platform."""

STEP6_MSG = """Step 6/7: Transfer USDT to Binance Futures

Before BitAI can execute, make sure your USDT is transferred into your own Binance Futures Wallet.

This will be the capital used for BitAI's AI-driven execution based on your selected risk profile.

Once completed, continue to Select Risk Profile."""

STEP7_MSG = """Step 7/7: Select Your Risk Profile

Choose your preferred BitAI Risk Profile based on your capital, goals, and risk appetite.

BitAI will execute according to the risk level you select.

Once done, BitAI will start to analyze real time market data and execute your trades automatically!"""

# ============ VIDEO SENDER ============
async def send_video(chat_id, context, step_key):
    """Send video directly - NO LINKS"""
    video_id = VIDEOS[step_key]
    
    if video_id.startswith('WAITING_FOR_VIDEO'):
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"⚠️ Video not configured yet. Please send the {step_key} video to this bot first."
        )
        return False
    
    try:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video_id,
            caption="🎥 Video loaded successfully!",
            supports_streaming=True
        )
        logger.info(f"✅ Sent video {step_key}")
        return True
    except Exception as e:
        logger.error(f"Failed to send video {step_key}: {e}")
        await context.bot.send_message(chat_id=chat_id, text=f"Error loading video. Please contact support.")
        return False

# ============ COMMAND HANDLERS ============
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Entry point - shows video and 4 buttons"""
    chat_id = update.effective_chat.id
    
    # Send video first (NO LINK)
    await send_video(chat_id, context, 'entry')
    
    # Then send message with buttons
    await context.bot.send_message(chat_id=chat_id, text=ENTRY_MSG, parse_mode='Markdown')
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Register my FREE BitAl account", callback_data='register')],
        [InlineKeyboardButton("Download BitAl (iOS & Android)", callback_data='download')],
        [InlineKeyboardButton("BitAl Setup Video", callback_data='step1')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ])
    await context.bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

async def show_step(update: Update, context: ContextTypes.DEFAULT_TYPE, step_num, message, buttons):
    """Generic function to show a step with video"""
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    # Delete old message
    try:
        await query.message.delete()
    except:
        pass
    
    # Send video for this step (NO LINK)
    await send_video(chat_id, context, f'step{step_num}')
    
    # Send message
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
    
    # Send buttons
    keyboard = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(chat_id=chat_id, text=f"Step {step_num}/7:", reply_markup=keyboard)

# ============ STEP HANDLERS ============
async def step1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Register FREE BitAl account", url=LINKS['register'])],
        [InlineKeyboardButton("Download BitAl", url=LINKS['download'])],
        [InlineKeyboardButton("Skip to Setting up Binance Account", callback_data='step2')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ]
    await show_step(update, context, 1, STEP1_MSG, buttons)

async def step2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Create a FREE Binance account", url=LINKS['binance_register'])],
        [InlineKeyboardButton("Download Binance (iOS & Android)", url=LINKS['binance_download'])],
        [InlineKeyboardButton("Skip to License Activation", callback_data='step3')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ]
    await show_step(update, context, 2, STEP2_MSG, buttons)

async def step3_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Skip to Activate & Enable Binance Futures", callback_data='step4')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ]
    await show_step(update, context, 3, STEP3_MSG, buttons)

async def step4_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Skip to setting API Keys", callback_data='step5')],
        [InlineKeyboardButton("Back to previous step", callback_data='step3')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ]
    await show_step(update, context, 4, STEP4_MSG, buttons)

async def step5_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Skip to Transferring USDT to Binance Futures", callback_data='step6')],
        [InlineKeyboardButton("Back to previous step", callback_data='step4')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ]
    await show_step(update, context, 5, STEP5_MSG, buttons)

async def step6_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Skip to Select Risk Profile", callback_data='step7')],
        [InlineKeyboardButton("Back to previous step", callback_data='step5')],
        [InlineKeyboardButton("Contact support", callback_data='support')]
    ]
    await show_step(update, context, 6, STEP6_MSG, buttons)

async def step7_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Back to previous step", callback_data='step6')],
        [InlineKeyboardButton("Website", url=LINKS['website'])],
        [InlineKeyboardButton("Email support", url=f"mailto:{LINKS['email']}")],
        [InlineKeyboardButton("Contact support", url=LINKS['support'])],
        [InlineKeyboardButton("Exit Conversation", callback_data='exit')]
    ]
    await show_step(update, context, 7, STEP7_MSG, buttons)

# ============ SIMPLE BUTTON HANDLERS ============
async def handle_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"🔗 Register here:\n{LINKS['register']}")

async def handle_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"📱 Download BitAl:\n{LINKS['download']}")

async def handle_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"📞 Contact support:\n{LINKS['support']}")

async def handle_exit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("👋 Conversation ended. Send /start to begin again.")

# ============ VIDEO CAPTURE - SEND VIDEOS HERE TO GET FILE_IDS ============
async def capture_video_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """When you send a video to this bot, it tells you the file_id"""
    if update.message.video:
        file_id = update.message.video.file_id
        file_size = update.message.video.file_size / (1024 * 1024)
        
        await update.message.reply_text(
            f"✅ *VIDEO CAPTURED!*\n\n"
            f"📹 *file_id:*\n"
            f"`{file_id}`\n\n"
            f"📊 Size: {file_size:.1f}MB\n\n"
            f"*Copy this file_id and paste it into the VIDEOS dictionary in your code.*",
            parse_mode='Markdown'
        )
        logger.info(f"Captured file_id: {file_id[:50]}...")

# ============ MAIN ============
def main():
    logger.info("🚀 Starting BitAl Bot...")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command
    app.add_handler(CommandHandler("start", start))
    
    # Video capture (REMOVE THIS AFTER GETTING FILE_IDS)
    app.add_handler(MessageHandler(filters.VIDEO, capture_video_file_id))
    
    # Callback handlers
    app.add_handler(CallbackQueryHandler(handle_register, pattern='^register$'))
    app.add_handler(CallbackQueryHandler(handle_download, pattern='^download$'))
    app.add_handler(CallbackQueryHandler(handle_support, pattern='^support$'))
    app.add_handler(CallbackQueryHandler(handle_exit, pattern='^exit$'))
    app.add_handler(CallbackQueryHandler(step1_handler, pattern='^step1$'))
    app.add_handler(CallbackQueryHandler(step2_handler, pattern='^step2$'))
    app.add_handler(CallbackQueryHandler(step3_handler, pattern='^step3$'))
    app.add_handler(CallbackQueryHandler(step4_handler, pattern='^step4$'))
    app.add_handler(CallbackQueryHandler(step5_handler, pattern='^step5$'))
    app.add_handler(CallbackQueryHandler(step6_handler, pattern='^step6$'))
    app.add_handler(CallbackQueryHandler(step7_handler, pattern='^step7$'))
    
    logger.info("✅ Bot is ready!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
