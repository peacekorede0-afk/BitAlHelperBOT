import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# ============ GET BOT TOKEN ============
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN not found!")
    exit(1)

logger.info(f"✅ Bot token loaded")

# ============ YOUR FILE_IDS ============
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

# ============ HANDLERS ============
def start(bot, update):
    chat_id = update.message.chat_id
    
    bot.send_video(
        chat_id=chat_id,
        video=VIDEOS['entry'],
        caption=ENTRY_MSG,
        parse_mode='Markdown'
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Register my FREE BitAl account", url=REGISTER_LINK)],
        [InlineKeyboardButton("Download BitAl (iOS & Android)", url=DOWNLOAD_BITAL)],
        [InlineKeyboardButton("➡️ NEXT", callback_data='step1')],
        [InlineKeyboardButton("Contact support", url=SUPPORT_WA)]
    ])
    bot.send_message(chat_id=chat_id, text="Choose an option:", reply_markup=keyboard)

def button_handler(bot, update):
    query = update.callback_query
    query.answer()
    chat_id = query.message.chat_id
    data = query.data
    
    try:
        query.message.delete()
    except:
        pass
    
    if data == 'step1':
        bot.send_video(
            chat_id=chat_id,
            video=VIDEOS['step1'],
            caption=STEP1_MSG,
            parse_mode='Markdown'
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Register FREE BitAl account", url=REGISTER_LINK)],
            [InlineKeyboardButton("Download BitAl", url=DOWNLOAD_BITAL)],
            [InlineKeyboardButton("➡️ NEXT", callback_data='step2')],
            [InlineKeyboardButton("Contact support", url=SUPPORT_WA)]
        ])
        bot.send_message(chat_id=chat_id, text="Step 1/7", reply_markup=keyboard)
        
    elif data == 'step2':
        bot.send_video(
            chat_id=chat_id,
            video=VIDEOS['step2'],
            caption=STEP2_MSG,
            parse_mode='Markdown'
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Create FREE Binance account", url=BINANCE_REGISTER)],
            [InlineKeyboardButton("Download Binance (iOS & Android)", url=BINANCE_DOWNLOAD)],
            [InlineKeyboardButton("➡️ NEXT", callback_data='step3')],
            [InlineKeyboardButton("◀️ BACK", callback_data='step1')],
            [InlineKeyboardButton("Contact support", url=SUPPORT_WA)]
        ])
        bot.send_message(chat_id=chat_id, text="Step 2/7", reply_markup=keyboard)
        
    elif data == 'step3':
        bot.send_video(
            chat_id=chat_id,
            video=VIDEOS['step3'],
            caption=STEP3_MSG,
            parse_mode='Markdown'
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➡️ NEXT", callback_data='step4')],
            [InlineKeyboardButton("◀️ BACK", callback_data='step2')],
            [InlineKeyboardButton("Contact support", url=SUPPORT_WA)]
        ])
        bot.send_message(chat_id=chat_id, text="Step 3/7", reply_markup=keyboard)
        
    elif data == 'step4':
        bot.send_video(
            chat_id=chat_id,
            video=VIDEOS['step4'],
            caption=STEP4_MSG,
            parse_mode='Markdown'
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➡️ NEXT", callback_data='step5')],
            [InlineKeyboardButton("◀️ BACK", callback_data='step3')],
            [InlineKeyboardButton("Contact support", url=SUPPORT_WA)]
        ])
        bot.send_message(chat_id=chat_id, text="Step 4/7", reply_markup=keyboard)
        
    elif data == 'step5':
        bot.send_video(
            chat_id=chat_id,
            video=VIDEOS['step5'],
            caption=STEP5_MSG,
            parse_mode='Markdown'
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➡️ NEXT", callback_data='step6')],
            [InlineKeyboardButton("◀️ BACK", callback_data='step4')],
            [InlineKeyboardButton("Contact support", url=SUPPORT_WA)]
        ])
        bot.send_message(chat_id=chat_id, text="Step 5/7", reply_markup=keyboard)
        
    elif data == 'step6':
        bot.send_video(
            chat_id=chat_id,
            video=VIDEOS['step6'],
            caption=STEP6_MSG,
            parse_mode='Markdown'
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("➡️ NEXT", callback_data='step7')],
            [InlineKeyboardButton("◀️ BACK", callback_data='step5')],
            [InlineKeyboardButton("Contact support", url=SUPPORT_WA)]
        ])
        bot.send_message(chat_id=chat_id, text="Step 6/7", reply_markup=keyboard)
        
    elif data == 'step7':
        bot.send_video(
            chat_id=chat_id,
            video=VIDEOS['step7'],
            caption=STEP7_MSG,
            parse_mode='Markdown'
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("◀️ Back to Step 6", callback_data='step6')],
            [InlineKeyboardButton("🌐 Website", url=WEBSITE)],
            [InlineKeyboardButton("✉️ Email", url=f"mailto:{EMAIL_SUPPORT}")],
            [InlineKeyboardButton("📞 WhatsApp", url=SUPPORT_WA)],
            [InlineKeyboardButton("❌ Exit", callback_data='exit')]
        ])
        bot.send_message(
            chat_id=chat_id,
            text="✅ Step 7/7 - Setup Complete!\n\n"
                 "5 Buttons:\n"
                 "1. Back to previous step (Transferring USDT to Binance Futures)\n"
                 "2. Website https://www.bitai.app\n"
                 "3. Email support: info@bitai.app\n"
                 "4. Contact support http://wa.me/6589691668\n"
                 "5. Exit Conversation (close bot)",
            reply_markup=keyboard
        )
        
    elif data == 'exit':
        bot.send_message(chat_id=chat_id, text="👋 Conversation ended. Send /start to begin again.")

# ============ MAIN ============
def main():
    logger.info("🚀 Starting BitAl Bot...")
    
    try:
        # Simple Updater without any arguments
        updater = Updater(BOT_TOKEN)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CallbackQueryHandler(button_handler))
        
        logger.info("✅ Bot is ready! Waiting for messages...")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"❌ Bot failed to start: {e}")
        raise

if __name__ == '__main__':
    main()
