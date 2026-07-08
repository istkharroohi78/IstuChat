from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

CHAT_STORAGE = [
    "mongodb+srv://chatbot1:a@cluster0.pxbu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot2:b@cluster0.9i8as.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot3:c@cluster0.0ak9k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot4:d@cluster0.4i428.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot5:e@cluster0.pmaap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot6:f@cluster0.u63li.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot7:g@cluster0.mhzef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot8:h@cluster0.okxao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot9:i@cluster0.yausb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot10:j@cluster0.9esnn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
]

# Saare 10 clusters ko ek saath connect karke list bana lo
db_clients = [MongoCli(url) for url in CHAT_STORAGE]

def get_user_db_client(user_id: int):
    """
    Yeh function Random ki jagah User ID calculate karke hamesha
    us user ke liye wahi same database return karega.
    """
    # 10 DBs me load balance karna
    db_index = user_id % len(db_clients)
    return db_clients[db_index]

# Aapke purane variables (Agar existing bot logic me directly inko use kar rahe the)
# Note: Agar global variables chahiye hi chahiye, toh by default Cluster 1 assign kar diya hai
ISTKHARBOY = db_clients[0] 
chatdb = ISTKHARBOY.Anonymous
chatai = chatdb.Word.WordDb
storeai = ISTKHARBOY.Anonymous.Word.NewWordDb
