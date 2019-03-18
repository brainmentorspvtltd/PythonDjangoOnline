#!C:/Python36/python.exe

import cgi
import pymysql

# first we make connection with database where,
# username is root, database name is ust_db
# mysql runs on port 3306
# host is by default localhost
connection = pymysql.connect(host='localhost', user='root', database='ust_db',port=3306,autocommit=True)

# for each connection mysql builds a cursor object (which means a connection per user)
cursor = connection.cursor()

form = cgi.FieldStorage()

emp_id = form.getvalue("emp_id")
emp_name = form.getvalue("emp_name")
emp_dept = form.getvalue("emp_dept")
emp_city = form.getvalue("emp_city")
emp_sal = form.getvalue("emp_sal")

query = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s)"
cursor.execute(query, (emp_id, emp_name, emp_dept, emp_city, emp_sal))

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Registered Successfully...</h1>
    <h1>Welcome {}</h1>
</body>
</html>
""".format(emp_name))