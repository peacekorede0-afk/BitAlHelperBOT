import os
import logging
import requests
import json
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# ============ GET BOT TOKEN ============
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN not found!")
    exit(1)

logger.info(f"✅ Bot token loaded")

# ============ TELEGRAM API URL ============
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

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

# ============ HELPER FUNCTIONS ============
def send_video(chat_id, video_id, caption):
    url = f"{API_URL}/sendVideo"
    data = {
        'chat_id': chat_id,
        'video': video_id,
        'caption': caption,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, data=data, timeout=30)
        return response.json()
    except Exception as e:
        logger.error(f"Error sending video: {e}")
        return None

def send_message_with_buttons(chat_id, text, buttons):
    url = f"{API_URL}/sendMessage"
    keyboard = {'inline_keyboard': buttons}
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown',
        'reply_markup': json.dumps(keyboard)
    }
    try:
        response = requests.post(url, data=data, timeout=30)
        logger.info(f"Sent message with buttons to {chat_id}")
        return response.json()
    except Exception as e:
        logger.error(f"Error sending message with buttons: {e}")
        return None

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, data=data, timeout=30)
        return response.json()
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        return None

def delete_message(chat_id, message_id):
    url = f"{API_URL}/deleteMessage"
    data = {'chat_id': chat_id, 'message_id': message_id}
    try:
        requests.post(url, data=data, timeout=30)
    except Exception as e:
        logger.error(f"Error deleting message: {e}")

def answer_callback(callback_id):
    url = f"{API_URL}/answerCallbackQuery"
    data = {'callback_query_id': callback_id}
    try:
        requests.post(url, data=data, timeout=30)
    except Exception as e:
        logger.error(f"Error answering callback: {e}")

# ============ HANDLE UPDATES ============
def handle_update(update):
    try:
        if 'message' in update and 'text' in update['message']:
            chat_id = update['message']['chat']['id']
            text = update['message']['text']
            
            if text == '/start':
                send_video(chat_id, VIDEOS['entry'], ENTRY_MSG)
                buttons = [
                    [{"text": "Register my FREE BitAl account", "url": REGISTER_LINK}],
                    [{"text": "Download BitAl (iOS & Android)", "url": DOWNLOAD_BITAL}],
                    [{"text": "➡️ NEXT", "callback_data": "step1"}],
                    [{"text": "Contact support", "url": SUPPORT_WA}]
                ]
                send_message_with_buttons(chat_id, "Choose an option:", buttons)
        
        elif 'callback_query' in update:
            query = update['callback_query']
            chat_id = query['message']['chat']['id']
            data = query['data']
            message_id = query['message']['message_id']
            callback_id = query['id']
            
            answer_callback(callback_id)
            delete_message(chat_id, message_id)
            
            if data == 'step1':
                send_video(chat_id, VIDEOS['step1'], STEP1_MSG)
                buttons = [
                    [{"text": "Register FREE BitAl account", "url": REGISTER_LINK}],
                    [{"text": "Download BitAl", "url": DOWNLOAD_BITAL}],
                    [{"text": "➡️ NEXT", "callback_data": "step2"}],
                    [{"text": "Contact support", "url": SUPPORT_WA}]
                ]
                send_message_with_buttons(chat_id, "Step 1/7", buttons)
                
            elif data == 'step2':
                send_video(chat_id, VIDEOS['step2'], STEP2_MSG)
                buttons = [
                    [{"text": "Create FREE Binance account", "url": BINANCE_REGISTER}],
                    [{"text": "Download Binance", "url": BINANCE_DOWNLOAD}],
                    [{"text": "➡️ NEXT", "callback_data": "step3"}],
                    [{"text": "◀️ BACK", "callback_data": "step1"}],
                    [{"text": "Contact support", "url": SUPPORT_WA}]
                ]
                send_message_with_buttons(chat_id, "Step 2/7", buttons)
                
            elif data == 'step3':
                send_video(chat_id, VIDEOS['step3'], STEP3_MSG)
                buttons = [
                    [{"text": "➡️ NEXT", "callback_data": "step4"}],
                    [{"text": "◀️ BACK", "callback_data": "step2"}],
                    [{"text": "Contact support", "url": SUPPORT_WA}]
                ]
                send_message_with_buttons(chat_id, "Step 3/7", buttons)
                
            elif data == 'step4':
                send_video(chat_id, VIDEOS['step4'], STEP4_MSG)
                buttons = [
                    [{"text": "➡️ NEXT", "callback_data": "step5"}],
                    [{"text": "◀️ BACK", "callback_data": "step3"}],
                    [{"text": "Contact support", "url": SUPPORT_WA}]
                ]
                send_message_with_buttons(chat_id, "Step 4/7", buttons)
                
            elif data == 'step5':
                send_video(chat_id, VIDEOS['step5'], STEP5_MSG)
                buttons = [
                    [{"text": "➡️ NEXT", "callback_data": "step6"}],
                    [{"text": "◀️ BACK", "callback_data": "step4"}],
                    [{"text": "Contact support", "url": SUPPORT_WA}]
                ]
                send_message_with_buttons(chat_id, "Step 5/7", buttons)
                
            elif data == 'step6':
                send_video(chat_id, VIDEOS['step6'], STEP6_MSG)
                buttons = [
                    [{"text": "➡️ NEXT", "callback_data": "step7"}],
                    [{"text": "◀️ BACK", "callback_data": "step5"}],
                    [{"text": "Contact support", "url": SUPPORT_WA}]
                ]
                send_message_with_buttons(chat_id, "Step 6/7", buttons)
                
            elif data == 'step7':
                # Send Step 7 video
                send_video(chat_id, VIDEOS['step7'], STEP7_MSG)
                
                # SHORT BUTTONS (under 64 characters) with full text in message above
                buttons = [
                    [{"text": "◀️ Back", "callback_data": "step6"}],
                    [{"text": "🌐 Website", "url": WEBSITE}],
                    [{"text": "✉️ Email", "url": f"mailto:{EMAIL_SUPPORT}"}],
                    [{"text": "📞 WhatsApp", "url": SUPPORT_WA}],
                    [{"text": "❌ Exit", "callback_data": "exit"}]
                ]
                
                send_message_with_buttons(
                    chat_id,
                    "✅ Step 7/7 - Setup Complete!\n\n"
                    "🔹 Back to previous step (Transferring USDT to Binance Futures)\n"
                    "🔹 Website: https://www.bitai.app\n"
                    "🔹 Email support: info@bitai.app\n"
                    "🔹 Contact support: http://wa.me/6589691668\n"
                    "🔹 Exit Conversation (close bot)\n\n"
                    "Click a button below:",
                    buttons
                )
                
            elif data == 'exit':
                send_message(chat_id, "👋 Conversation ended. Send /start to begin again.")
    
    except Exception as e:
        logger.error(f"Error handling update: {e}")

# ============ MAIN ============
def main():
    logger.info("🚀 Starting BitAl Bot...")
    
    last_update_id = 0
    logger.info("✅ Bot is ready! Waiting for messages...")
    
    while True:
        try:
            url = f"{API_URL}/getUpdates"
            params = {
                'offset': last_update_id + 1,
                'timeout': 30
            }
            response = requests.get(url, params=params, timeout=35)
            data = response.json()
            
            if data.get('ok'):
                for update in data.get('result', []):
                    last_update_id = update['update_id']
                    handle_update(update)
            
            time.sleep(1)
            
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
            time.sleep(5)

if __name__ == '__main__':
    main()
