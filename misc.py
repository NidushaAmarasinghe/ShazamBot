import logging
from aiogram import Bot, Dispatcher
from shazamio import Shazam

API_TOKEN = '5109606479:AAGCKgG4NXD2XYW_9H_2fmn8JzBpXyvrY7o'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
shazam = Shazam()
