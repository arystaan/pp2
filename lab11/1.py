import psycopg2 as pgsql

def create_connection():
    try:
        connection = pgsql.connect(host="localhost", dbname="phonebook_db2", user="postgres",
                                   password="Moskatmalades_28012006", port="5432")
        return connection
    except pgsql.Error as e:
        print("Error connecting to the database:", e)
        return None

def create_pattern():
    query = """SELECT * FROM PhoneBook WHERE """
    print("Do you want to search by surname(0)/name(1)/break(any num) enter the number:")
    mode = int(input())
    if mode == 0:
        query += "surname"
        print("Enter string")
        substr = input()
        print("""Select option:
        1-surname is equal to string
        2-surname starts with the string
        3-surname ends with the string
        4-surname contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    elif mode == 1:
        query += "name"
        print("Enter string")
        substr = input()
        print("""Select option:
        1-name is equal to string
        2-name starts with the string
        3-name ends with the string
        4-name contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    else:
        return "error"
    return query

def insert(surname, name, phone):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT count(*) FROM phonebook WHERE surname='{}' AND name='{}'".format(surname, name))
            if cursor.fetchone()[0] == 0:
                cursor.execute("""INSERT INTO phonebook VALUES ('{}','{}', {})""".format(surname, name, phone))
            else:
                cursor.execute("""UPDATE phonebook SET number={} WHERE surname='{}' AND name='{}'""".format(phone, surname, name))
            connection.commit()
        except pgsql.Error as e:
            print("Error executing insert/update query:", e)
        finally:
            if cursor:
                cursor.close()
            connection.close()

def loop_insert():
    banned = []
    while True:
        print("Want to enter a person's data? yes/no")
        mode = input()
        if mode.lower() == "no":
            break
        person = input().split()
        if len(person) > 3:
            banned.append(person)
            continue
        if not person[2].isdigit():
            banned.append(person)
            continue
        insert(*person)
    if banned:
        print("This data were not added due to incorrect format:")
        for i in banned:
             print(i)

def pagination():
    query = create_pattern()
    if query == "error":
        return "error"
    print("Need offset? yes/no:")
    mode = input()
    if mode.lower() == "yes":
         print("Enter offset:")
         offset = int(input())
         query += " OFFSET {}".format(offset)
    print("Need limit? yes/no:")
    mode = input()
    if mode.lower() == "yes":
         print("Enter limit:")
         limit = int(input())
         query += " LIMIT {}".format(limit)
    query += ";"
    return query

def delete():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * from phonebook")
            print(cursor.fetchall())
            print("Do you wanna delete by surname(0)/name(1)/number(2) enter the number")
            mode = int(input())
            if mode == 0:
                print("Enter surname to delete:")
                surname = input()
                query = "DELETE FROM phonebook WHERE surname='{}'".format(surname)
            elif mode == 1:
                print("Enter name to delete:")
                name = input()
                query = "DELETE FROM phonebook WHERE name='{}'".format(name)
            else:
                print("Enter number to delete:")
                number = input()
                query = "DELETE FROM phonebook WHERE phone_number={}".format(number)
            cursor.execute(query)
            connection.commit()
        except pgsql.Error as e:
            print("Error executing delete query:", e)
        finally:
            if cursor:
                cursor.close()
            connection.close()

if __name__ == "__main__":
    loop_insert()
    s1 = pagination()
    if s1 != "error":
         connection = create_connection()
         if connection:
             try:
                 cursor = connection.cursor()
                 cursor.execute(s1)
                 print(cursor.fetchall())
             except pgsql.Error as e:
                 print("Error executing pagination query:", e)
             finally:
                 if cursor:
                     cursor.close()
                 connection.close()
    delete()