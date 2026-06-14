import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')

# ============ YOUR FILE_IDS (Already captured from your bot) ============
VIDEOS = {
    'entry': 'BAACAgQAAxkBAAMYai3-z5ZB7JVZa9przLZIZX5rjUIAArwhAAJdNnBRRGw2cWcHYMA8BA',
    'step1': 'BAACAgQAAxkBAAMaai3_GuiDvvO1PpJlFlZpUro9yj0AAr0hAAJdNnBRd5_eEgx7yLA8BA',
    'step2': 'BAACAgQAAxkBAAMcai3_QFVXTCnldA_vUQNWVmhH8csAAr4hAAJdNnBRC4W2zTZTRRg8BA',
    'step3': 'BAACAgQAAxkBAAMeai3_Tozjn7lPqIpT0anRYep-uDUAAr8hAAJdNnBRpLVsK7JLfZ48BA',
    'step4': 'BAACAgQAAxkBAAMgai3_X76fPHfZK13m9wqlDpEp728AAsEhAAJdNnBRtmVky1-zBKY8BA',
    'step5': 'BAACAgQAAxkBAAMiai3_dW99shMtSBh9pM9x9WA-LqkAAsIhAAJdNnBRGlzR_hVQSO08BA',
    'step6': 'BAACAgQAAxkBAAMkai3_iBEsrC3T2-JqEtXb0eKQrL8AAsMhAAJdNnBRvhqvjSHZlag8BA',
    'step7': 'BAACAgQAAxkBAAMmai3_vwlSsuChBpj6ZSw1rw8tpQUAAsQhAAJdNnBRAAEC-ApFvpvMPAQ'
}

# ============ LINKS ============
REGISTER_LINK = 'https://app.bitai.app/h5/#/pages/sign/sign?invite=888'
DOWNLOAD_BITAL = 'https://fr.bitai.app/app.html'
BINANCE_REGISTER = 'https://accounts.binance.com/en/register?ref=1154159582'
BINANCE_DOWNLOAD = 'https://www.binance.com/en/download'
SUPPORT_WA = 'http://wa.me/6589691668'
EMAIL_SUPPORT = 'info@bitai.app'
WEBSITE = 'https://www.bitai.app'

# ============ MESSAGES WITH THEIR BUTTONS ============
# ENTRY MESSAGE
ENTRY_MESSAGE = """Welcome to BitAl by Affinity AI 🚀

Most crypto traders don't lose because they lack knowledge.

They lose because manual trading is emotional, bot settings are messy, and execution comes too late.

It's time to upgrade to BitAl - built to analyze real-time market data and execute your trades automatically, 24/7."""

ENTRY_BUTTONS = [
    [InlineKeyboardButton("Register my FREE BitAl account", callback_data='register')],
    [InlineKeyboardButton("Download BitAl (iOS & Android)", callback_data='download')],
    [InlineKeyboardButton("BitAl Setup Video", callback_data='step1')],
    [InlineKeyboardButton("Contact support", callback_data='support')]
]

# STEP 1
STEP1_MESSAGE = """Step 1/7: Register and download BitAl

To start using BitAl, you need to register for your FREE BitAl account and download BitAl app. If you are referred by our BitAl user, please use their referral link to register."""

STEP1_BUTTONS = [
    [InlineKeyboardButton("Register FREE BitAl account", url=REGISTER_LINK)],
    [InlineKeyboardButton("Download BitAl", url=DOWNLOAD_BITAL)],
    [InlineKeyboardButton("Skip to Setting up Binance Account", callback_data='step2')],
    [InlineKeyboardButton("Contact support", callback_data='support')]
]

# STEP 2
STEP2_MESSAGE = """Step 2/7: Setting up Binance Account

To start using BitAl, you need a Binance account with KYC verification completed.

Already have a verified Binance account? You may skip this video and continue to BitAI License Activation."""

STEP2_BUTTONS = [
    [InlineKeyboardButton("Create a FREE Binance account", url=BINANCE_REGISTER)],
    [InlineKeyboardButton("Download Binance (iOS & Android)", url=BINANCE_DOWNLOAD)],
    [InlineKeyboardButton("Skip to License Activation", callback_data='step3')],
    [InlineKeyboardButton("Contact support", callback_data='support')]
]

# STEP 3
STEP3_MESSAGE = """Step 3/7: BitAI License Activation

To unlock BitAI's full auto AI trading, activate your BitAI License inside your BitAI app. Once activated, you can proceed to activate & enable your Binance Futures."""

STEP3_BUTTONS = [
    [InlineKeyboardButton("Skip to Activate & Enable Binance Futures", callback_data='step4')],
    [InlineKeyboardButton("Contact support", callback_data='support')]
]

# STEP 4
STEP4_MESSAGE = """Step 4/7: Activate & Enable Binance Futures

Before BitAI can execute, you need to activate Binance Futures inside your Binance account.

Once Futures is enabled, you can continue to the next step and create your Binance API connection."""

STEP4_BUTTONS = [
    [InlineKeyboardButton("Skip to setting API Keys", callback_data='step5')],
    [InlineKeyboardButton("Back to previous step", callback_data='step3')],
    [InlineKeyboardButton("Contact support", callback_data='support')]
]

# STEP 5
STEP5_MESSAGE = """Step 5/7: Set Up Your API Keys

Next, create your Binance API Keys and connect them to your BitAI account.

This allows BitAI to analyze real-time market data and execute based on your selected risk profile.

Make sure your API Keys are kept private and only connected inside the official BitAI platform."""

STEP5_BUTTONS = [
    [InlineKeyboardButton("Skip to Transferring USDT to Binance Futures", callback_data='step6')],
    [InlineKeyboardButton("Back to previous step", callback_data='step4')],
    [InlineKeyboardButton("Contact support", callback_data='support')]
]

# STEP 6
STEP6_MESSAGE = """Step 6/7: Transfer USDT to Binance Futures

Before BitAI can execute, make sure your USDT is transferred into your own Binance Futures Wallet.

This will be the capital used for BitAI's AI-driven execution based on your selected risk profile.

Once completed, continue to Select Risk Profile."""

STEP6_BUTTONS = [
    [InlineKeyboardButton("Skip to Select Risk Profile", callback_data='step7')],
    [InlineKeyboardButton("Back to previous step", callback_data='step5')],
    [InlineKeyboardButton("Contact support", callback_data='support')]
]

# STEP 7
STEP7_MESSAGE = """Step 7/7: Select Your Risk Profile

Choose your preferred BitAI Risk Profile based on your capital, goals, and risk appetite.

BitAI will execute according to the risk level you select.

Once done, BitAI will start to analyze real time market data and execute your trades automatically!"""

STEP7_BUTTONS = [
    [InlineKeyboardButton("Back to previous step", callback_data='step6')],
    [InlineKeyboardButton("Website", url=WEBSITE)],
    [InlineKeyboardButton("Email support", url=f"mailto:{EMAIL_SUPPORT}")],
    [InlineKeyboardButton("Contact support", url=SUPPORT_WA)],
    [InlineKeyboardButton("Exit Conversation", callback_data='exit')]
]

# ============ HELPER FUNCTION ============
async def send_message_with_video(chat_id, context, step_key, message, buttons):
    """Send video with message as caption, then buttons"""
    try:
        await context.bot.send_video(
            chat_id=chat_id,
            video=VIDEOS[step_key],
            caption=message,
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Failed to send video {step_key}: {e}")
        await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
    
    reply_markup = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(
        chat_id=chat_id,
        text="Select an option:",
        reply_markup=reply_markup
    )

# ============ COMMAND HANDLERS ============
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await send_message_with_video(chat_id, context, 'entry', ENTRY_MESSAGE, ENTRY_BUTTONS)

async def step1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    try:
        await query.message.delete()
    except:
        pass
    
    await send_message_with_video(chat_id, context, 'step1', STEP1_MESSAGE, STEP1_BUTTONS)

async def step2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    try:
        await query.message.delete()
    except:
        pass
    
    await send_message_with_video(chat_id, context, 'step2', STEP2_MESSAGE, STEP2_BUTTONS)

async def step3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    try:
        await query.message.delete()
    except:
        pass
    
    await send_message_with_video(chat_id, context, 'step3', STEP3_MESSAGE, STEP3_BUTTONS)

async def step4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    try:
        await query.message.delete()
    except:
        pass
    
    await send_message_with_video(chat_id, context, 'step4', STEP4_MESSAGE, STEP4_BUTTONS)

async def step5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    try:
        await query.message.delete()
    except:
        pass
    
    await send_message_with_video(chat_id, context, 'step5', STEP5_MESSAGE, STEP5_BUTTONS)

async def step6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    try:
        await query.message.delete()
    except:
        pass
    
    await send_message_with_video(chat_id, context, 'step6', STEP6_MESSAGE, STEP6_BUTTONS)

async def step7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    
    try:
        await query.message.delete()
    except:
        pass
    
    await send_message_with_video(chat_id, context, 'step7', STEP7_MESSAGE, STEP7_BUTTONS)

# ============ UTILITY HANDLERS ============
async def handle_register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"🔗 Register here:\n{REGISTER_LINK}")

async def handle_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"📱 Download BitAl:\n{DOWNLOAD_BITAL}")

async def handle_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"📞 Contact support:\n{SUPPORT_WA}")

async def handle_exit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("👋 Conversation ended. Send /start to begin again.")

# ============ MAIN ============
def main():
    logger.info("🚀 Starting BitAl Bot...")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
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
    
    logger.info("✅ Bot is ready! Videos will play directly.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
