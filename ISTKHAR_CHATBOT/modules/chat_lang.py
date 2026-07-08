from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from ISTKHAR_CHATBOT import ISTKHAR_CHATBOT as app, mongo, db
import asyncio
from ISTKHAR_CHATBOT.modules.helpers import chatai, CHATBOT_ON, languages

# V2 AI Engine Import karein
from ISTKHAR_CHATBOT.modules.Chatgpt import call_openrouter

lang_db = db.ChatLangDb.LangCollection
message_cache = {}

async def get_chat_language(chat_id):
    chat_lang = await lang_db.find_one({"chat_id": chat_id})
    return chat_lang["language"] if chat_lang and "language" in chat_lang else None

@app.on_message(filters.text, group=2)
async def store_messages(client, message: Message):
    global message_cache

    chat_id = message.chat.id
    chat_lang = await get_chat_language(chat_id)

    # Agar language set nahi hai, tabhi AI detect karega
    if not chat_lang or chat_lang == "nolang":
        if message.from_user and message.from_user.is_bot:
            return

        if chat_id not in message_cache:
            message_cache[chat_id] = []

        message_cache[chat_id].append(message)

        # Jab 30 messages ho jayein
        if len(message_cache[chat_id]) >= 30:
            history = "\n\n".join(
                [f"Text: {msg.text}..." for msg in message_cache[chat_id]]
            )
            user_input = f"""
            sentences list :-
            [
            {history}
            ]

            Above is a list of sentences. Each sentence could be in different languages. Analyze the language of each sentence separately and identify the dominant language used for each sentence. and then Consider the language that appears the most, ignoring any commands like sentence start with /. 
            Provide only the official language name with language code (like 'en' for English, 'hi' for Hindi). in this format :-
            Lang Name :- ""
            Lang code :- ""
            ok so provideo me only overall [ Lang Name and Lang Code ] in above format Do not provide anything else.
            """
            
            # Cache ko turant clear karna zaroori hai taaki jab tak AI soche, doosre messages cache na bhar dein
            message_cache[chat_id].clear()
            
            # Aapne yahan 60 sec ka sleep lagaya tha MukeshAPI ki limit se bachne ke liye
            # Ab OpenRouter ke saath hum isey hata sakte hain ya chota kar sakte hain. Main 5 seconds de raha hoon.
            await asyncio.sleep(5)
            
            try:
                # Naya OpenRouter Call (Jo automatically 3 keys ke beech switch hota hai)
                ai_response = await call_openrouter([{"role": "user", "content": user_input}])
                
                reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("sᴇʟᴇᴄᴛ ʟᴀɴɢᴜᴀɢᴇ", callback_data="choose_lang")]])    
                await message.reply_text(f"**Chat language detected for this chat:**\n\n{ai_response}\n\n**You can set my lang by /lang**", reply_markup=reply_markup)
            except Exception as e:
                print(f"[LOG] Language Detection Failed: {e}")

@app.on_message(filters.command("chatlang", prefixes=[".", "/"]))
async def fetch_chat_lang(client, message):
    chat_id = message.chat.id
    chat_lang = await get_chat_language(chat_id)
    await message.reply_text(f"The language code using for this chat is: {chat_lang}")
