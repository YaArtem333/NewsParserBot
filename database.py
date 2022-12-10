import sqlite3

# Устанавливаем соединение с базой данных и используем курсор для работы с ней
connection = sqlite3.connect("user_database.db", check_same_thread=False)
cursor = connection.cursor()

# Функция добавления пользователя в БД
def add_user(user_id: int,  username: str):
	cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
	return connection.commit()

# Функция проверки пользователя в БД по user_id
def check_user_in_db(user_id: int):
	cursor.execute(f"SELECT id FROM users WHERE user_id = {user_id}")
	return len(cursor.fetchall())

# Функция удаления пользователя из БД
def delete_user(user_id: int):
	cursor.execute(f"DELETE FROM users WHERE user_id = {user_id}")
	return connection.commit()

# Функция закрытия соединения с БД
def close_connection():
	connection.close()
