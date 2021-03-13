import telebot
import sqlite3

conn = sqlite3.connect('trigs.db')  # Initiating object of DB to connect DB
cur = conn.cursor()  # Initiating cursor for manipulating of DB connection

# Here program create DB with tables
# It should be used once
def create_db():
    global conn
    global cur

    cur.execute("""CREATE TABLE IF NOT EXISTS chats(
                chat_id int PRIMARY KEY,
                `name` varchar,
                count_of_asking int               
                );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS triggers(
                trigger_id int PRIMARY KEY,
                trigger_text varchar,
                answer varchar,
                reply smallint,
                count_of_asking int               
                );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS trigger_to_chat(
                trigger_id int PRIMARY KEY,
                chat_id int,
                status int               
                );""")
    conn.commit()


TRIGGER_LIST = []
