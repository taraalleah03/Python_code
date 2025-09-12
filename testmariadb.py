import mariadb

connection = mariadb.connect(
host ='127.0.0.1',
port = 3306,
user = 'root',
password = 'taRamart!n2003thirty',
database = 'people1',
autocommit = True
)

print("Connected to Maria db!")

def get_employees_by_last_name(connection, last_name):
    sql = "SELECT number, last_name, first_name ,salary FROM employee1 WHERE last_name = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (last_name,))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    else:
        print(f"No employees with last name {last_name} found.")

    cursor.close()

ln = input("Enter the last name of the employee whose salary you wish to check: ")
get_employees_by_last_name(connection, ln)

connection.close()

print("Connection closed.")

