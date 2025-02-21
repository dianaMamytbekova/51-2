import sqlite3

connect = sqlite3.connect('User.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

connect.commit()

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

def get_all_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()
    
    print("\nСписок всех пользователей:")
    for user in users:
        print(f"NAME: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")

def get_user_by_name(name):
    cursor.execute('SELECT name, age, hobby FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()
    
    if user:
        print(f"\nNAME: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    else:
        print(f"\nПользователь с именем {name} не найден.")

add_user("Ardager", 26, "Гонки")
add_user("Alex", 30, "Футбол")

get_all_users()

print("\nПроверяем поиск:")
get_user_by_name("Ardager")
get_user_by_name("Noname")
