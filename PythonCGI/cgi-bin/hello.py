#!C:/Python36/python.exe

import cgi
form = cgi.FieldStorage()

name = form.getvalue('u_name')
email = form.getvalue('u_email')
pwd = form.getvalue('u_pwd')
country = form.getvalue('country')
gender = form.getvalue('gender')

print("Content-type:text/html\r\n\r\n")
'''
print("<html>")
print("<head><title>Login Page</title></head>")
print("<body>")
print("<h1>Hello User</h1>")
print("</body></html>")
'''

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Welcome {}</h1>
    <h2>Email : {}</h2>
    <h2>Country : {}</h2>
    <h2>Gender : {}</h2>
</body>
</html>
""".format(name,email,country,gender))