import requests
import json
import os
from flask import Flask, request

# ==================== CONFIGURATION ====================
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')

# ==================== VIDEO FILE IDs ====================
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

# ==================== LINKS ====================
LINKS = {
    'register': 'https://app.bitai.app/h5/#/pages/sign/sign?invite=888',
    'download_bital': 'https://fr.bitai.app/app.html',
    'binance_register': 'https://accounts.binance.com/en/register?ref=1154159582',
    'binance_download': 'https://www.binance.com/en/download',
    'support_whatsapp': 'http://wa.me/6589691668',
    'email': 'info@bitai.app',
    'website': 'https://www.bitai.app'
}

# ==================== MESSAGES ====================
MESSAGES = {
    'entry': 'Welcome to BitAl Helper Bot!\n\nI\'m here to guide you through setting up your BitAl AI Trading Bot in 7 simple steps.\n\nWatch the welcome video above, then click the buttons below to get started!',
    'step1': 'Step 1/7: Register and Download BitAl\n\n1. Click Register to create your FREE BitAl account\n2. Click Download to install BitAl on iOS or Android\n\nWatch the video above for a visual guide!',
    'step2': 'Step 2/7: Setting Up Your Binance Account\n\n1. Click Create Binance to register your account\n2. Click Download Binance to install the app\n\nWatch the video above for detailed instructions!',
    'step3': 'Step 3/7: BitAl License Activation\n\nActivate your BitAl license to unlock full trading capabilities.\n\nWatch the video above to see how it is done!',
    'step4': 'Step 4/7: Activate & Enable Binance Futures\n\nEnable Futures trading on your Binance account.\n\nWatch the video above for the step-by-step process!',
    'step5': 'Step 5/7: Set Up Your API Keys\n\nConnect BitAl to Binance using API keys for secure trading.\n\nWatch the video above to learn how to generate and configure your API keys!',
    'step6': 'Step 6/7: Transfer USDT to Binance Futures\n\nFund your Binance Futures wallet with USDT to start trading.\n\nWatch the video above for the transfer process!',
    'step7': 'Step 7/7 - Setup Complete!\n\nCongratulations! You have completed all 7 setup steps!\n\nYour BitAl bot is now ready to trade. Use the buttons below:'
}

# ==================== TELEGRAM API HELPERS ====================

def send_message(chat_id, text, reply_markup=None, parse_mode='Markdown'):
    url = f'{BASE_URL}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode
    }
    if reply_markup:
        payload['reply_markup'] = json.dumps(reply_markup)
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error sending message: {e}')
        if hasattr(e, 'response') and e.response is not None:
            print(f'Response: {e.response.text}')
        return None


def send_video(chat_id, video_file_id, caption=None, reply_markup=None, parse_mode='Markdown'):
    url = f'{BASE_URL}/sendVideo'
    payload = {
        'chat_id': chat_id,
        'video': video_file_id,
        'parse_mode': parse_mode
    }
    if caption:
        payload['caption'] = caption
    if reply_markup:
        payload['reply_markup'] = json.dumps(reply_markup)
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error sending video: {e}')
        if hasattr(e, 'response') and e.response is not None:
            print(f'Response: {e.response.text}')
        return None


def answer_callback_query(callback_query_id, text=None):
    url = f'{BASE_URL}/answerCallbackQuery'
    payload = {'callback_query_id': callback_query_id}
    if text:
        payload['text'] = text
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error answering callback: {e}')
        return None


# ==================== KEYBOARD BUILDERS ====================

def build_entry_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'Register FREE', 'url': LINKS['register']},
                {'text': 'Download BitAl', 'url': LINKS['download_bital']}
            ],
            [
                {'text': 'NEXT', 'callback_data': 'step1'}
            ],
            [
                {'text': 'Contact Support', 'url': LINKS['support_whatsapp']}
            ]
        ]
    }


def build_step1_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'Register', 'url': LINKS['register']},
                {'text': 'Download', 'url': LINKS['download_bital']}
            ],
            [
                {'text': 'NEXT', 'callback_data': 'step2'}
            ],
            [
                {'text': 'Contact Support', 'url': LINKS['support_whatsapp']}
            ]
        ]
    }


def build_step2_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'Create Binance', 'url': LINKS['binance_register']},
                {'text': 'Download Binance', 'url': LINKS['binance_download']}
            ],
            [
                {'text': 'BACK', 'callback_data': 'step1'},
                {'text': 'NEXT', 'callback_data': 'step3'}
            ],
            [
                {'text': 'Contact Support', 'url': LINKS['support_whatsapp']}
            ]
        ]
    }


def build_step3_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'BACK', 'callback_data': 'step2'},
                {'text': 'NEXT', 'callback_data': 'step4'}
            ],
            [
                {'text': 'Contact Support', 'url': LINKS['support_whatsapp']}
            ]
        ]
    }


def build_step4_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'BACK', 'callback_data': 'step3'},
                {'text': 'NEXT', 'callback_data': 'step5'}
            ],
            [
                {'text': 'Contact Support', 'url': LINKS['support_whatsapp']}
            ]
        ]
    }


def build_step5_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'BACK', 'callback_data': 'step4'},
                {'text': 'NEXT', 'callback_data': 'step6'}
            ],
            [
                {'text': 'Contact Support', 'url': LINKS['support_whatsapp']}
            ]
        ]
    }


def build_step6_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'BACK', 'callback_data': 'step5'},
                {'text': 'NEXT', 'callback_data': 'step7'}
            ],
            [
                {'text': 'Contact Support', 'url': LINKS['support_whatsapp']}
            ]
        ]
    }


def build_step7_keyboard():
    return {
        'inline_keyboard': [
            [
                {'text': 'BACK', 'callback_data': 'step6'}
            ],
            [
                {'text': 'WEBSITE', 'url': LINKS['website']}
            ],
            [
                {'text': 'EMAIL SUPPORT', 'url': 'https://t.me/share/url?url=&text=Contact%20BitAl%20Support:%20info@bitai.app'}
            ],
            [
                {'text': 'CONTACT SUPPORT', 'url': LINKS['support_whatsapp']}
            ],
            [
                {'text': 'EXIT', 'callback_data': 'exit'}
            ]
        ]
    }


# ==================== STEP HANDLERS ====================

def handle_entry(chat_id):
    send_video(chat_id, VIDEOS['entry'])
    send_message(chat_id, MESSAGES['entry'], build_entry_keyboard())


def handle_step1(chat_id):
    send_video(chat_id, VIDEOS['step1'])
    send_message(chat_id, MESSAGES['step1'], build_step1_keyboard())


def handle_step2(chat_id):
    send_video(chat_id, VIDEOS['step2'])
    send_message(chat_id, MESSAGES['step2'], build_step2_keyboard())


def handle_step3(chat_id):
    send_video(chat_id, VIDEOS['step3'])
    send_message(chat_id, MESSAGES['step3'], build_step3_keyboard())


def handle_step4(chat_id):
    send_video(chat_id, VIDEOS['step4'])
    send_message(chat_id, MESSAGES['step4'], build_step4_keyboard())


def handle_step5(chat_id):
    send_video(chat_id, VIDEOS['step5'])
    send_message(chat_id, MESSAGES['step5'], build_step5_keyboard())


def handle_step6(chat_id):
    send_video(chat_id, VIDEOS['step6'])
    send_message(chat_id, MESSAGES['step6'], build_step6_keyboard())


def handle_step7(chat_id):
    send_video(chat_id, VIDEOS['step7'])
    send_message(chat_id, MESSAGES['step7'], build_step7_keyboard())


def handle_exit(chat_id):
    send_message(
        chat_id,
        'Thank you for using BitAl Helper Bot!\n\nIf you need help again, just send /start.\n\nHappy trading!',
        parse_mode='Markdown'
    )


# ==================== WEBHOOK HANDLER ====================

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return 'OK', 200

    if 'callback_query' in data:
        callback = data['callback_query']
        chat_id = callback['message']['chat']['id']
        callback_query_id = callback['id']
        callback_data = callback['data']
        answer_callback_query(callback_query_id)

        if callback_data == 'step1':
            handle_step1(chat_id)
        elif callback_data == 'step2':
            handle_step2(chat_id)
        elif callback_data == 'step3':
            handle_step3(chat_id)
        elif callback_data == 'step4':
            handle_step4(chat_id)
        elif callback_data == 'step5':
            handle_step5(chat_id)
        elif callback_data == 'step6':
            handle_step6(chat_id)
        elif callback_data == 'step7':
            handle_step7(chat_id)
        elif callback_data == 'exit':
            handle_exit(chat_id)
        return 'OK', 200

    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')
        if text.startswith('/start'):
            handle_entry(chat_id)
        else:
            send_message(chat_id, 'Send /start to begin the BitAl setup guide!', parse_mode='Markdown')
        return 'OK', 200

    return 'OK', 200


@app.route('/', methods=['GET'])
def health_check():
    return 'BitAl Helper Bot is running!', 200


# ==================== SETUP ====================

def set_webhook():
    if not WEBHOOK_URL:
        print('WARNING: WEBHOOK_URL not set. Skipping webhook setup.')
        return
    url = f'{BASE_URL}/setWebhook'
    payload = {
        'url': WEBHOOK_URL,
        'max_connections': 40,
        'allowed_updates': ['message', 'callback_query']
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
        result = response.json()
        if result.get('ok'):
            print(f'Webhook set successfully: {WEBHOOK_URL}')
        else:
            print(f'Failed to set webhook: {result}')
    except requests.exceptions.RequestException as e:
        print(f'Error setting webhook: {e}')


# ==================== MAIN ====================

if __name__ == '__main__':
    set_webhook()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
