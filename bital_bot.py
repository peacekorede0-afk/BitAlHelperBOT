import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv('BOT_TOKEN')

# ============ YOUR FILE_IDS (Pasted from above) ============
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

# ============ MESSAGES ============
MESSAGES = {
    'entry': """🤖 *Welcome to BitAl by Affinity AI*

Most crypto traders don't lose because they lack knowledge.

They lose because manual trading is emotional, bot settings are messy, and execution comes too late.

⏰ It's time to upgrade to *BitAl* - built to analyze real-time market data and execute your trades automatically, 24/7.""",

    'step1': """📌 *Step 1/7: Register and download BitAl*

To start using BitAl, you need to register for your FREE BitAl account and download the BitAl app.""",

    'step2': """📌 *Step 2/7: Setting up Binance Account*

To start using BitAl, you need a Binance account with KYC verification completed.""",

    'step3': """📌 *Step 3/7: BitAI License Activation*

To unlock BitAI's full auto AI trading, activate your BitAI License inside your BitAI app.""",

    'step4': """📌 *Step 4/7: Activate & Enable Binance Futures*

Before BitAI can execute, you need to activate Binance Futures inside your Binance account.""",

    'step5': """📌 *Step 5/7: Set Up Your API Keys*

Create your Binance API Keys and connect them to your BitAI account.
⚠️ Keep your API Keys private!""",

    'step6': """📌 *Step 6/7: Transfer USDT to Binance Futures*

Transfer USDT into your Binance Futures Wallet for trading.""",

    'step7': """📌 *Step 7/7: Select Your Risk Profile*

Choose your preferred BitAI Risk Profile based on your capital and goals.

🎯 *BitAI will now trade automatically 24/7!"""
}

# ============ BOT HANDLERS ============

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with entry video"""
    await update.message.reply_video(
        video=VIDEOS['entry'],
        caption=MESSAGES['entry'],
        parse_mode='Markdown'
    )
    
    keyboard = [
        [InlineKeyboardButton("✅ Register FREE Account", callback_data='register')],
        [InlineKeyboardButton("📱 Download BitAl", callback_data='download')],
        [InlineKeyboardButton("▶️ Start Setup Guide (7 Steps)", callback_data='step1')],
        [InlineKeyboardButton("📞 Contact Support", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔽 *Choose an option:* 🔽", reply_markup=reply_markup, parse_mode='Markdown')

async def show_step(update, context, step):
    """Show a specific step with video and buttons"""
    query = update.callback_query
    if query:
        await query.answer()
        chat_id = query.message.chat.id
        message_id = query.message.message_id
        await query.message.delete()
    else:
        chat_id = update.effective_chat.id
        message_id = None
    
    # Send video for the step
    if step == 'entry':
        await context.bot.send_video(chat_id, VIDEOS['entry'], caption=MESSAGES['entry'], parse_mode='Markdown')
    elif step == 'step1':
        await context.bot.send_video(chat_id, VIDEOS['step1'], caption=MESSAGES['step1'], parse_mode='Markdown')
    elif step == 'step2':
        await context.bot.send_video(chat_id, VIDEOS['step2'], caption=MESSAGES['step2'], parse_mode='Markdown')
    elif step == 'step3':
        await context.bot.send_video(chat_id, VIDEOS['step3'], caption=MESSAGES['step3'], parse_mode='Markdown')
    elif step == 'step4':
        await context.bot.send_video(chat_id, VIDEOS['step4'], caption=MESSAGES['step4'], parse_mode='Markdown')
    elif step == 'step5':
        await context.bot.send_video(chat_id, VIDEOS['step5'], caption=MESSAGES['step5'], parse_mode='Markdown')
    elif step == 'step6':
        await context.bot.send_video(chat_id, VIDEOS['step6'], caption=MESSAGES['step6'], parse_mode='Markdown')
    elif step == 'step7':
        await context.bot.send_video(chat_id, VIDEOS['step7'], caption=MESSAGES['step7'], parse_mode='Markdown')
    
    # Show appropriate keyboard
    if step == 'entry':
        keyboard = [
            [InlineKeyboardButton("✅ Register FREE Account", callback_data='register')],
            [InlineKeyboardButton("📱 Download BitAl", callback_data='download')],
            [InlineKeyboardButton("▶️ Start Setup Guide (7 Steps)", callback_data='step1')],
            [InlineKeyboardButton("📞 Contact Support", callback_data='support')]
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
            [InlineKeyboardButton("◀️ Back", callback_data='step1')]
        ]
    elif step == 'step3':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: Enable Futures", callback_data='step4')],
            [InlineKeyboardButton("◀️ Back", callback_data='step2')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step4':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: API Keys", callback_data='step5')],
            [InlineKeyboardButton("◀️ Back", callback_data='step3')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step5':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: Transfer USDT", callback_data='step6')],
            [InlineKeyboardButton("◀️ Back", callback_data='step4')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step6':
        keyboard = [
            [InlineKeyboardButton("▶️ Next: Risk Profile", callback_data='step7')],
            [InlineKeyboardButton("◀️ Back", callback_data='step5')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ]
    elif step == 'step7':
        keyboard = [
            [InlineKeyboardButton("🌐 Website", url=WEBSITE)],
            [InlineKeyboardButton("✉️ Email Support", url=f"mailto:{EMAIL_SUPPORT}")],
            [InlineKeyboardButton("📞 WhatsApp", url=SUPPORT_WA)],
            [InlineKeyboardButton("◀️ Back", callback_data='step6')],
            [InlineKeyboardButton("❌ Exit", callback_data='exit')]
        ]
    else:
        return
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id, "🔽 *Choose an option:* 🔽", reply_markup=reply_markup, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()
    
    action = query.data
    
    if action == 'register':
        await query.edit_message_text(f"🔗 Register here: {REGISTER_LINK}")
    elif action == 'download':
        await query.edit_message_text(f"📱 Download BitAl: {DOWNLOAD_BITAL}")
    elif action == 'support':
        await query.edit_message_text(
            f"📞 *Support Options:*\n\nWhatsApp: {SUPPORT_WA}\nEmail: {EMAIL_SUPPORT}\nWebsite: {WEBSITE}",
            parse_mode='Markdown'
        )
    elif action == 'exit':
        await query.edit_message_text("👋 Thank you! Type /start to begin again.")
    elif action in ['step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 'entry']:
        await show_step(update, context, action)

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 BitAl Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
