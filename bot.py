import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5631979252:AAGn16G2Cr7AXL708FNrt3fLaFuQ7FCenBw")

API_ID = int(os.environ.get("API_ID", '27884084'))

API_HASH = os.environ.get("API_HASH", "f41ef10f7e283ba0b6b18fac6fbe8226")

STRING = os.environ.get("STRING", "1BVtsOKkBu0vXWW_-fj5WJyBH9SQSNCM84PU2P37sXJPV2SrSbp97XqPUwKB4LMdxzNYvujRRpJFCPsnhRWI1seqf4Jx38u4I2B9AfXcjlsSdeJlHeWgyG_94MYlDFLkpGqwfu22ylHJCxSMq_iHRbz8ZSOS7ousx8pkE3bCS0UFAgu8rGtWRYQbMpaV7Kp0aI2nVeNJP7OFRZ5k6Cr-Q3hOyJO213iGTPLOHhMi1-E6dQc4YrVzHU-VxGiF-mLdoYSSsH4BrO5rdSxA_Josg--zWygfTKtahqTloTeVOn48wqGUQax1zYAzr-W8grGEW7VUtlO4Of4pV5-cn_sZKoWtFN-wuhw8=")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
