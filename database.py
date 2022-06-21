import sqlite3
con = sqlite3.connect('database.db')
cursor = con.cursor()

def fill_with_list(records):
    cursor.execute('DELETE FROM followers')
    for record in records:
        cursor.execute(f'INSERT INTO followers(user_id) VALUES("{record}")')
    con.commit()

def read_all():
    cursor.execute('SELECT * FROM followers')
    return cursor.fetchall()
