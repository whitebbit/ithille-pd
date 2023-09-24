import sqlite3
from random import random

from faker import Faker

fake = Faker()


def create_customers_table():
    conn = sqlite3.connect('instance/music.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      first_name TEXT,
                      last_name TEXT,
                      email TEXT
                    )''')


def add_customers(count=100):
    conn = sqlite3.connect('instance/music.db')
    cursor = conn.cursor()
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        cursor.execute("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)",
                       (first_name, last_name, email))
    conn.commit()
    conn.close()


def create_tracks_table():
    conn = sqlite3.connect('instance/music.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tracks (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      artist TEXT,
                      duration_seconds INTEGER,
                      release_date DATE
                    )''')


def add_tracks(count=100):
    conn = sqlite3.connect('instance/music.db')
    cursor = conn.cursor()
    for _ in range(100):
        artist = fake.name()
        duration_seconds = random.randint(180, 600)
        release_date = fake.date_of_birth(minimum_age=18, maximum_age=50).strftime('%Y-%m-%d')
        cursor.execute("INSERT INTO tracks (artist, duration_seconds, release_date) VALUES (?, ?, ?)",
                       (artist, duration_seconds, release_date))
    conn.commit()
    conn.close()
