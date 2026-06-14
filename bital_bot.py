import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Your file_ids
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

# Links
REGISTER_LINK = 'https://app.bitai.app/h5/#/pages/sign/sign?invite=888'
DOWNLOAD_BITAL = 'https://fr.bitai.app/app.html'
BINANCE_REGISTER = 'https://accounts.binance.com/en/register?ref=1154159582'
BINANCE_DOWNLOAD = 'https://www.binance.com/en/download'
SUPPORT_WA = 'http://wa.me/6589691668'
WEBSITE = 'https://www.bitai.app'

# Simple start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    print(f"User {user_id} started the bot")
    
    # Send entry video
    try:
        await update.message.reply_video(
            video=VIDEOS['entry'],
            caption="🎯 *Welcome to BitAl!*\n\nSend /start to begin or /help for options.",
            parse_mode='Markdown'
        )
    except Exception as e:
        print(f"Error sending video: {e}")
        await update.message.reply_text("Welcome to BitAl Bot!")
    
    # Send buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Register", callback_data='register')],
        [InlineKeyboardButton("📱 Download", callback_data='download')],
        [InlineKeyboardButton("▶️ Begin Setup", callback_data='step1')],
        [InlineKeyboardButton("📞 Support", callback_data='support')]
    ])
    await update.message.reply_text("Choose an option:", reply_markup=keyboard)

# Simple help handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *BitAl Bot Help*\n\n"
        "Send /start to begin\n"
        "Use the buttons to navigate through the 7-step setup\n\n"
        "For support: " + SUPPORT_WA,
        parse_mode='Markdown'
    )

# Handle button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    action = query.data
    chat_id = query.message.chat.id
    
    print(f"Button clicked: {action}")
    
    if action == 'register':
        await query.edit_message_text(f"🔗 Register: {REGISTER_LINK}")
    
    elif action == 'download':
        await query.edit_message_text(f"📱 Download: {DOWNLOAD_BITAL}")
    
    elif action == 'support':
        await query.edit_message_text(f"📞 Support: {SUPPORT_WA}")
    
    elif action == 'step1':
        await context.bot.send_video(chat_id, VIDEOS['step1'], caption="📌 *Step 1/7: Register and download BitAl*", parse_mode='Markdown')
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Register", url=REGISTER_LINK)],
            [InlineKeyboardButton("📱 Download", url=DOWNLOAD_BITAL)],
            [InlineKeyboardButton("▶️ Next Step", callback_data='step2')],
            [InlineKeyboardButton("◀️ Back", callback_data='back')]
        ])
        await query.edit_message_text("Step 1/7 - Choose an option:", reply_markup=keyboard)
    
    elif action == 'step2':
        await context.bot.send_video(chat_id, VIDEOS['step2'], caption="📌 *Step 2/7: Setting up Binance Account*", parse_mode='Markdown')
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Create Binance", url=BINANCE_REGISTER)],
            [InlineKeyboardButton("📱 Download Binance", url=BINANCE_DOWNLOAD)],
            [InlineKeyboardButton("▶️ Next Step", callback_data='step3')],
            [InlineKeyboardButton("◀️ Back", callback_data='step1')]
        ])
        await query.edit_message_text("Step 2/7 - Choose an option:", reply_markup=keyboard)
    
    elif action == 'step3':
        await context.bot.send_video(chat_id, VIDEOS['step3'], caption="📌 *Step 3/7: License Activation*", parse_mode='Markdown')
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("▶️ Next Step", callback_data='step4')],
            [InlineKeyboardButton("◀️ Back", callback_data='step2')]
        ])
        await query.edit_message_text("Step 3/7 - Continue:", reply_markup=keyboard)
    
    elif action == 'step4':
        await context.bot.send_video(chat_id, VIDEOS['step4'], caption="📌 *Step 4/7: Enable Binance Futures*", parse_mode='Markdown')
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("▶️ Next Step", callback_data='step5')],
            [InlineKeyboardButton("◀️ Back", callback_data='step3')]
        ])
        await query.edit_message_text("Step 4/7 - Continue:", reply_markup=keyboard)
    
    elif action == 'step5':
        await context.bot.send_video(chat_id, VIDEOS['step5'], caption="📌 *Step 5/7: API Keys Setup*", parse_mode='Markdown')
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("▶️ Next Step", callback_data='step6')],
            [InlineKeyboardButton("◀️ Back", callback_data='step4')]
        ])
        await query.edit_message_text("Step 5/7 - Continue:", reply_markup=keyboard)
    
    elif action == 'step6':
        await context.bot.send_video(chat_id, VIDEOS['step6'], caption="📌 *Step 6/7: Transfer USDT to Futures*", parse_mode='Markdown')
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("▶️ Next Step", callback_data='step7')],
            [InlineKeyboardButton("◀️ Back", callback_data='step5')]
        ])
        await query.edit_message_text("Step 6/7 - Continue:", reply_markup=keyboard)
    
    elif action == 'step7':
        await context.bot.send_video(chat_id, VIDEOS['step7'], caption="📌 *Step 7/7: Select Risk Profile*\n\n✅ Setup Complete!", parse_mode='Markdown')
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🌐 Website", url=WEBSITE)],
            [InlineKeyboardButton("📞 Support", callback_data='support')],
            [InlineKeyboardButton("◀️ Back", callback_data='step6')]
        ])
        await query.edit_message_text("Step 7/7 - You're all set! 🎉", reply_markup=keyboard)
    
    elif action == 'back':
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("▶️ Begin Setup", callback_data='step1')],
            [InlineKeyboardButton("📞 Support", callback_data='support')]
        ])
        await query.edit_message_text("Return to main menu:", reply_markup=keyboard)

# Main function
def main():
    print("Starting BitAl Bot...")
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running! Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()
