from django.shortcuts import render
from django.http import JsonResponse
import pymysql

connection = pymysql.connect(host='localhost',user='root',port=3306,
                database='ust_db',autocommit=True)
cursor = connection.cursor()

# emails = ['ram@gmail.com', 'ram12@gmail.com','ram122@gmail.com']

# Create your views here.
def index(req):
    return render(req, 'index.html')

def register(req):
    emp_id = req.POST['emp_id']
    emp_name = req.POST['emp_name']
    emp_dept = req.POST['emp_dept']
    emp_city = req.POST['emp_city']
    emp_sal = req.POST['emp_sal']
    query = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query,(emp_id, emp_name, emp_dept, emp_city, emp_sal))
    return render(req, 'register.html')

# def validateEmail(req):
#     useremail = req.GET['usermail']
#     print("Email Recieved", useremail)
#     for email in emails:
#         if email == useremail:
#             msg = "User Already Exist"
#             break
#         else:
#             msg = ""
#     return JsonResponse(msg, safe=False)

def validateId(req):
    emp_id = req.GET['emp_id']
    # print("Emp Id", emp_id)
    query = 'SELECT * FROM employees'
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data)
    for emp in data:
        if int(emp_id) in emp:
            msg = "Emp Already Exist"
            break
        else:
            msg = "Valid"
    return JsonResponse(msg, safe=False)