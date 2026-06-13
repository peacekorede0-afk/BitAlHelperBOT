import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token
BOT_TOKEN = os.getenv('BITAL_BOT_TOKEN')

# ============ CONFIGURATION ============
# Links
REGISTER_LINK = 'https://app.bitai.app/h5/#/pages/sign/sign?invite=888'
DOWNLOAD_BITAL = 'https://fr.bitai.app/app.html'
BINANCE_REGISTER = 'https://accounts.binance.com/en/register?ref=1154159582'
BINANCE_DOWNLOAD = 'https://www.binance.com/en/download'
SUPPORT_WA = 'http://wa.me/6589691668'
EMAIL_SUPPORT = 'info@bitai.app'
WEBSITE = 'https://www.bitai.app'

# ==============================================
# REPLACE THESE WITH YOUR ACTUAL FILE_IDS
# After getting them from the File ID Bot
# ==============================================
VIDEOS = {
    'entry': 'REPLACE_WITH_FILE_ID_FROM_IVlL9mus1vk',
    'step1': 'REPLACE_WITH_FILE_ID_FROM_-FOS2Vp9g2k',
    'step2': 'REPLACE_WITH_FILE_ID_FROM_51S50bjeit8',
    'step3': 'REPLACE_WITH_FILE_ID_FROM_fDmnibIgefs',
    'step4': 'REPLACE_WITH_FILE_ID_FROM_4sc6C_jt3Xg',
    'step5': 'REPLACE_WITH_FILE_ID_FROM_BzBoXzPuwlg',
    'step6': 'REPLACE_WITH_FILE_ID_FROM_M8XAcPEvYtQ',
    'step7': 'REPLACE_WITH_FILE_ID_FROM_aY8r4J3OJSY'
}

# YouTube backup links (in case video fails)
YOUTUBE_BACKUP = {
    'entry': 'https://youtu.be/IVlL9mus1vk',
    'step1': 'https://youtu.be/-FOS2Vp9g2k',
    'step2': 'https://youtu.be/51S50bjeit8',
    'step3': 'https://youtu.be/fDmnibIgefs',
    'step4': 'https://youtu.be/4sc6C_jt3Xg',
    'step5': 'https://youtu.be/BzBoXzPuwlg',
    'step6': 'https://youtu.be/M8XAcPEvYtQ',
    'step7': 'https://youtu.be/aY8r4J3OJSY'
}

# ============ MESSAGES ============
MESSAGES = {
    'entry': """
🤖 *Welcome to BitAl by Affinity AI*

Most crypto traders don't lose because they lack knowledge.

They lose because manual trading is emotional, bot settings are messy, and execution comes too late.

⏰ It's time to upgrade to *BitAl* - built to analyze real-time market data and execute your trades automatically, 24/7.
    """,
    'step1': """
📌 *Step 1/7: Register and download BitAl*

To start using BitAl, you need to register for your FREE BitAl account and download the BitAl app.
    """,
    'step2': """
📌 *Step 2/7: Setting up Binance Account*

To start using BitAl, you need a Binance account with KYC verification completed.
    """,
    'step3': """
📌 *Step 3/7: BitAI License Activation*

To unlock BitAI's full auto AI trading, activate your BitAI License inside your BitAI app.
    """,
    'step4': """
📌 *Step 4/7: Activate & Enable Binance Futures*

Before BitAI can execute, you need to activate Binance Futures inside your Binance account.
    """,
    'step5': """
📌 *Step 5/7: Set Up Your API Keys*

Create your Binance API Keys and connect them to your BitAI account.
⚠️ Keep your API Keys private!
    """,
    'step6': """
📌 *Step 6/7: Transfer USDT to Binance Futures*

Transfer USDT into your Binance Futures Wallet for trading.
    """,
    'step7': """
📌 *Step 7/7: Select Your Risk Profile*

Choose your preferred BitAI Risk Profile based on your capital and goals.

🎯 *BitAI will now trade automatically 24/7!*
    """
}

# Store user states (in production, use Redis or database)
user_states = {}

# ============ HELPER FUNCTIONS ============
async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE, step: str):
    """Send video to user with fallback to YouTube link."""
    try:
        # Try to send video using file_id
        await update.message.reply_video(
            video=VIDEOS[step],
            caption=MESSAGES[step],
            parse_mode='Markdown',
            supports_streaming=True
        )
    except Exception as e:
        logger.error(f"Video error for {step}: {e}")
        # Fallback: Send message and YouTube link
        await update.message.reply_text(MESSAGES[step], parse_mode='Markdown')
        await update.message.reply_text(
            f"⚠️ *Video couldn't load directly. Watch it here:*\n{YOUTUBE_BACKUP[step]}",
            parse_mode='Markdown'
        )

async def show_step(update: Update, context: ContextTypes.DEFAULT_TYPE, step: str):
    """Show a specific step with its video and buttons."""
    user_id = update.effective_user.id
    user_states[user_id] = step
    
    await send_video(update, context, step)
    
    # Show appropriate buttons based on step
    if step == 'entry':
        keyboard = [
            [InlineKeyboardButton("✅ Register FREE Account", callback_data='register')],
            [InlineKeyboardButton("📱 Download BitAl", callback_data='download')],
            [InlineKeyboardButton("▶️ Start Setup Guide (7 Steps)", callback_data='start_setup')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step1':
        keyboard = [
            [InlineKeyboardButton("✅ Register BitAl", url=REGISTER_LINK)],
            [InlineKeyboardButton("📱 Download App", url=DOWNLOAD_BITAL)],
            [InlineKeyboardButton("▶️ Next: Binance Setup", callback_data='step2')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step2':
        keyboard = [
            [InlineKeyboardButton("✅ Create Binance Account", url=BINANCE_REGISTER)],
            [InlineKeyboardButton("📱 Download Binance", url=BINANCE_DOWNLOAD)],
            [InlineKeyboardButton("▶️ Next: License Activation", callback_data='step3')],
            [InlineKeyboardButton("◀️ Back", callback_data='back_to_step1')]
        ]
    elif step == 'step3':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: Enable Futures", callback_data='step4')],
            [InlineKeyboardButton("◀️ Back", callback_data='back_to_step2')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step4':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: API Keys", callback_data='step5')],
            [InlineKeyboardButton("◀️ Back", callback_data='back_to_step3')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step5':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: Transfer USDT", callback_data='step6')],
            [InlineKeyboardButton("◀️ Back", callback_data='back_to_step4')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step6':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: Risk Profile", callback_data='step7')],
            [InlineKeyboardButton("◀️ Back", callback_data='back_to_step5')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step7':
        keyboard = [
            [InlineKeyboardButton("🌐 Website", url=WEBSITE)],
            [InlineKeyboardButton("✉️ Email Support", url=f"mailto:{EMAIL_SUPPORT}")],
            [InlineKeyboardButton("📞 WhatsApp", url=SUPPORT_WA)],
            [InlineKeyboardButton("◀️ Back to Step 6", callback_data='back_to_step6')],
            [InlineKeyboardButton("❌ Exit", callback_data='exit')]
        ]
    else:
        return
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔽 *Choose an option:* 🔽", reply_markup=reply_markup, parse_mode='Markdown')

# ============ COMMAND HANDLERS ============
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    await show_step(update, context, 'entry')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    action = query.data
    user_id = query.from_user.id
    
    if action == 'register':
        await query.edit_message_text(f"🔗 Register here: {REGISTER_LINK}")
    elif action == 'download':
        await query.edit_message_text(f"📱 Download BitAl: {DOWNLOAD_BITAL}")
    elif action == 'start_setup':
        await show_step(update, context, 'step1')
    elif action == 'step2':
        await show_step(update, context, 'step2')
    elif action == 'step3':
        await show_step(update, context, 'step3')
    elif action == 'step4':
        await show_step(update, context, 'step4')
    elif action == 'step5':
        await show_step(update, context, 'step5')
    elif action == 'step6':
        await show_step(update, context, 'step6')
    elif action == 'step7':
        await show_step(update, context, 'step7')
    elif action == 'back_to_step1':
        await show_step(update, context, 'step1')
    elif action == 'back_to_step2':
        await show_step(update, context, 'step2')
    elif action == 'back_to_step3':
        await show_step(update, context, 'step3')
    elif action == 'back_to_step4':
        await show_step(update, context, 'step4')
    elif action == 'back_to_step5':
        await show_step(update, context, 'step5')
    elif action == 'back_to_step6':
        await show_step(update, context, 'step6')
    elif action == 'support':
        await query.edit_message_text(
            f"📞 *Support Options:*\n\nWhatsApp: {SUPPORT_WA}\nEmail: {EMAIL_SUPPORT}\nWebsite: {WEBSITE}",
            parse_mode='Markdown'
        )
    elif action == 'exit':
        await query.edit_message_text("👋 Thank you! Type /start to begin again.")
        if user_id in user_states:
            del user_states[user_id]

def main():
    """Start the bot."""
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Start bot
    print("🤖 BitAl Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
