import psycopg2
import csv

# Функция для подключения к базе данных PostgreSQL
def connect():
    conn = psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    return conn

# Функция для загрузки данных из CSV-файла
def upload_from_csv(file_path):
    conn = connect()
    cursor = conn.cursor()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовок, если присутствует
        for row in reader:
            cursor.execute("INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    conn.close()

# Функция для вставки данных из консоли
def insert_from_console():
    user_name = input("Введите имя пользователя: ")
    phone_number = input("Введите номер телефона: ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)", (user_name, phone_number))
    conn.commit()
    conn.close()

# Функция для обновления данных в таблице
def update_data():
    user_name = input("Введите имя пользователя: ")
    phone_number = input("Введите номер телефона: ")
    new_user_name = input("Введите новое имя пользователя: ")
    new_phone_number = input("Введите новый номер телефона: ")
    conn = connect()
    cursor = conn.cursor()
    if new_user_name:
        cursor.execute("UPDATE phonebook SET user_name = %s WHERE user_name = %s", (new_user_name, user_name))
        cursor.execute("UPDATE phonebook SET phone_number = %s WHERE user_name = %s", (new_phone_number, new_user_name))
    conn.commit()
    conn.close()

# Функция для запроса данных из таблицы с фильтрами
def query_data():
    conn = connect()
    cursor = conn.cursor()
    user_name = input("Введите имя пользователя: ")
    phone_number = input("Введите номер телефона: ")
    if user_name:
        cursor.execute("SELECT * FROM phonebook WHERE user_name = %s", (user_name,))
    elif phone_number:
        cursor.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone_number,))
    else:
        cursor.execute("SELECT * FROM phonebook")
    rows = cursor.fetchall()
    conn.close()
    for i in rows:
        print(i)

# Функция для удаления данных из таблицы по имени пользователя или номеру телефона
def delete_data():
    conn = connect()
    cursor = conn.cursor()
    user_name = input("Введите имя пользователя: ")
    phone_number = input("Введите номер телефона: ")
    if user_name and phone_number:
        cursor.execute("DELETE FROM phonebook WHERE user_name = %s AND phone_number = %s", (user_name, phone_number))
    elif user_name and not phone_number:
        cursor.execute("DELETE FROM phonebook WHERE user_name = %s", (user_name,))
    elif not user_name and phone_number:
        print(123)
        cursor.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone_number,))
    conn.commit()
    conn.close()

temp = ""
# Пример использования
while temp != "exit":
    temp = input("выбери режим([insert], [update], [query], [delete], [exit]): ")
    
    # Загрузка из CSV
    upload_from_csv('pb.csv')
    
    # Вставка из консоли
    if temp == "insert": insert_from_console()
    
    # Обновление данных
    if temp == "update": update_data()

    #запрос данных
    if temp == "query": query_data()

    #удаление данных
    if temp == "delete": delete_data()
