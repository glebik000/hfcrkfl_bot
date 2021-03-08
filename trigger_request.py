import telebot
import sqlite3


conn = sqlite3.connect('trigger.db')
cur = conn.cursor()

TRIGGER_LIST = []
