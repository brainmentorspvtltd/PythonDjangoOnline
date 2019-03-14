Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> emp = {"id":101,"name":}
SyntaxError: invalid syntax
>>> 
>>> emp = {"id":101,"name":"ram","dept":"IT","sal":25000}
>>> emp
{'id': 101, 'name': 'ram', 'dept': 'IT', 'sal': 25000}
>>> emp[2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    emp[2]
KeyError: 2
>>> emp['name']
'ram'
>>> emp.keys()
dict_keys(['id', 'name', 'dept', 'sal'])
>>> emp.values()
dict_values([101, 'ram', 'IT', 25000])
>>> for data in emp:
	print(data)

	
id
name
dept
sal
>>> for data in emp.values():
	print(data)

	
101
ram
IT
25000
>>> for data in emp.items():
	print(data)

	
('id', 101)
('name', 'ram')
('dept', 'IT')
('sal', 25000)
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonOnline/Dict_1.py ===========
{'p_id': 101, 'p_name': 'Apple', 'p_price': 56000, 'p_color': 'white'}
{'p_id': 102, 'p_name': 'Samsung', 'p_price': 46000, 'p_color': 'silver'}
{'p_id': 103, 'p_name': 'Vivo', 'p_price': 25000, 'p_color': 'white'}
{'p_id': 104, 'p_name': 'Apple', 'p_price': 65000, 'p_color': 'golden'}
{'p_id': 105, 'p_name': 'Vivo', 'p_price': 20000, 'p_color': 'black'}
{'p_id': 106, 'p_name': 'Samsung', 'p_price': 50000, 'p_color': 'black'}
{'p_id': 107, 'p_name': 'Samsung', 'p_price': 60000, 'p_color': 'white'}
{'p_id': 108, 'p_name': 'Apple', 'p_price': 80000, 'p_color': 'silver'}
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonOnline/Dict_1.py ===========
{'p_id': 101, 'p_name': 'Apple', 'p_price': 56000, 'p_color': 'white'}
{'p_id': 104, 'p_name': 'Apple', 'p_price': 65000, 'p_color': 'golden'}
{'p_id': 108, 'p_name': 'Apple', 'p_price': 80000, 'p_color': 'silver'}
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonOnline/Dict_1.py ===========
{'p_id': 103, 'p_name': 'Vivo', 'p_price': 25000, 'p_color': 'white'}
{'p_id': 105, 'p_name': 'Vivo', 'p_price': 20000, 'p_color': 'black'}
>>> s1 = {1,2,6,8,23,45,7,2,67,3,9,0,5,2,3,6,7,8,2,12}
>>> s1
{0, 1, 2, 67, 3, 5, 6, 7, 8, 9, 12, 45, 23}
>>> s2 = {10,20,30,40,50,21,3,5,7,23,45}
>>> s1
{0, 1, 2, 67, 3, 5, 6, 7, 8, 9, 12, 45, 23}
>>> s3
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s3
NameError: name 's3' is not defined
>>> s2
{3, 5, 7, 40, 10, 45, 50, 20, 21, 23, 30}
>>> s1.intersection(s2)
{3, 5, 7, 45, 23}
>>> s1.union(s2)
{0, 1, 2, 67, 3, 5, 6, 7, 8, 9, 10, 12, 20, 21, 23, 30, 40, 45, 50}
>>> s1 & s2
{3, 5, 7, 45, 23}
>>> s1 | s2
{0, 1, 2, 67, 3, 5, 6, 7, 8, 9, 10, 12, 20, 21, 23, 30, 40, 45, 50}
>>> s1 - s2
{0, 1, 2, 67, 6, 8, 9, 12}
>>> 
============ RESTART: C:/Users/asus/Desktop/PythonOnline/Sets.py ============
66.66666666666667
>>> 
============ RESTART: C:/Users/asus/Desktop/PythonOnline/Sets.py ============
Similar Movies are {'robot', 'ironman', 'baahubali', 'batman', 'fukrey'}
66.66666666666667
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_1.py =========
33
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_1.py =========
44
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_1.py =========
44
Outside function 44
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
9
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/PythonOnline/Function_2.py", line 6, in <module>
    calc(5)
TypeError: calc() missing 1 required positional argument: 'y'
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
5
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
15
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
15
101 Ram IT pune
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
15
101 Ram IT pune
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/PythonOnline/Function_2.py", line 16, in <module>
    emp(101,'Ram','IT','pune','delhi')
TypeError: emp() takes 4 positional arguments but 5 were given
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
15
101 Ram IT ('pune',)
101 Ram IT ('pune', 'delhi')
101 Ram IT ('pune', 'chennai', 'delhi')
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
15
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/PythonOnline/Function_2.py", line 15, in <module>
    emp(101,'Ram','IT','pune')
TypeError: emp() missing 1 required keyword-only argument: 'address'
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
15
101 Ram IT ('pune',)
101 Ram IT ('pune', 'delhi')
101 Ram IT ('pune', 'chennai', 'delhi')
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_2.py =========
15
101 Ram IT ('pune',)
101 Ram IT ('pune', 'delhi')
101 Ram IT ('pune', 'chennai', 'delhi')
{'name': 'ram', 'dept': 'IT', 'sal': 45000}
{'id': 102, 'name': 'shyam', 'dept': 'HR'}
{'id': 103, 'name': 'raman', 'dept': 'IT', 'sal': 40000}
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
None
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
None
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
9
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
(9, -1, 0.8, 20)
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
(9, -1, 0.8, 20)
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
(9, -1, 0.8, 20)
9 -1 0.8 20
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
(9, -1, 0.8, 20)
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/PythonOnline/Function_3.py", line 16, in <module>
    a,b,c = calc(4,5)
ValueError: too many values to unpack (expected 3)
>>> 
========= RESTART: C:/Users/asus/Desktop/PythonOnline/Function_3.py =========
(9, -1, 0.8, 20)
9 -1 [0.8, 20]
>>> x = []
>>> for i in range(1000):
	x.append(i)

	
>>> x = []
>>> for i in range(1000):
	if x % 2 == 0:
		x.append(i)

		
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    if x % 2 == 0:
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> for i in range(1000):
	if i % 2 == 0:
		x.append(i)

		
>>> x = [i for i in range(10)]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = [i for i in range(31) if i % 2 == 0]
>>> x
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
>>> x = [i**2 for i in range(31) if i % 2 == 0]
>>> x
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900]
>>> d = {i:i for i in range(1,31) if i % 2 == 0}
>>> d
{2: 2, 4: 4, 6: 6, 8: 8, 10: 10, 12: 12, 14: 14, 16: 16, 18: 18, 20: 20, 22: 22, 24: 24, 26: 26, 28: 28, 30: 30}
>>> d = {i:i**2 for i in range(1,31) if i % 2 == 0}
>>> d
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324, 20: 400, 22: 484, 24: 576, 26: 676, 28: 784, 30: 900}
>>> 
