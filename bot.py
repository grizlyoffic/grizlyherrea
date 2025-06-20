import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Apna Bot Token daalo yahan:
TOKEN = '7650319498:AAG2ifHshwYdgiDlREbHV_1tu6hUtzOpr9s'

# Galiyon ke smart regex patterns
BAD_WORD_PATTERNS = [
    r'\bg[\W_]*a[\W_]*n[\W_]*d[\W_]*u\b',
    r'\bc[\W_]*h[\W_]*u[\W_]*t[\W_]*i[\W_]*y[\W_]*a\b',
    r'\bb[\W_]*c\b',
    r'\bm[\W_]*c\b',
    r'\bb[\W_]*s[\W_]*d[\W_]*k\b',
    r'\bb[\W_]*s[\W_]*d[\W_]*l\b',
    r'\bf[\W_]*u[\W_]*c[\W_]*k\b',
    r'\bm[\W_]*a[\W_]*d[\W_]*a[\W_]*r[\W_]*c[\W_]*h[\W_]*o[\W_]*d\b',
    r'\bb[\W_]*h[\W_]*o[\W_]*s[\W_]*d[\W_]*i[\W_]*k[\W_]*e\b',
    r'\bl[\W_]*u[\W_]*n[\W_]*d\b',
    r'\bch[\W_]*u[\W_]*t[\W_]*\b',
    r'\bc[\W_]*h[\W_]*o[\W_]*d\b',
    r'\bsa[\W_]*l[\W_]*a\b',
    r'\bhar[\W_]*a[\W_]*m[\W_]*i\b',
    r'\bn[\W_]*u[\W_]*n[\W_]*i\b',
]

# Gali detect karne ka function
def contains_bad_word(text):
    for pattern in BAD_WORD_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

# Telegram par message receive hone pe handle karna
async def check_for_bad_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    text = update.message.text
    if contains_bad_word(text):
        try:
            await update.message.delete()
            await update.effective_chat.send_message("⚠️ Gali Detected!")
        except Exception as e:
            print("Error:", e)

# Bot start karne ka main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), check_for_bad_words))
    print("🚀 Gali Filter Bot is running...")
    app.run_polling()