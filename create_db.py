"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
from faker import Faker
import sqlite3
import os
import inspect
from datetime import datetime
from pprint import pprint

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    con = sqlite3.connect('social_network.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS people (name TEXT NOT NULL, age INTEGER, updated_at DATETIME NOT NULL, created_at DATETIME NOT NULL);""")
    
    return 

def populate_people_table():
    conn = sqlite3.connect('social_network.db')
    c = conn.cursor()
    fake = Faker()
    for i in range(200):
        name = fake.name()
        age = fake.random_int(min=1,max=100)
        created = datetime.now()
        updated = datetime.now()
        c.execute(f"INSERT INTO people (name, age, updated_at, created_at) VALUES (?,?,?,?);",(name ,age, updated,created))
   
    return

def get_script_dir():
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()