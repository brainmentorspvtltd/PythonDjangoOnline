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

query = "SELECT * FROM employees"
cursor.execute(query)
data = cursor.fetchall()
empCount = cursor.rowcount

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
    <h1>Employees Data</h1>
    <h2>Number of Employees : {}</h2>
""".format(empCount))

print("""
<table border=2 width='100%' cellpadding=10>
<tr>
    <th>Emp ID</th>
    <th>Emp Name</th>
    <th>Emp Department</th>
    <th>Emp City</th>
    <th>Emp Salary</th>
</tr>
""")
for i in range(empCount):
    print("""
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
    """.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))

print("""
</table>
</body>
</html>
""")