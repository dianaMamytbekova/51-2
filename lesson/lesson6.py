import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        hobby TEXT
    )
''')

conn.commit()

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    conn.commit()
    print(f"Пользователь {name} дoбавлен")


add_user("John", 18, "плавание")    
add_user("John", 17, "плавание")    
add_user("John", 19, "плавание")    
add_user("John", 15, "плавание")    

def get_all_users():

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)

    for i in users:
        print(f'NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}')

get_all_users()      


#UPDATE

def update_user(row_id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?,'new_name,  row_id
    )
    conn.commit()






