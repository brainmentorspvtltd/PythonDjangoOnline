Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello this is python and python is used for web development and machine learning"
>>> text[0]
'H'
>>> text[1]
'e'
>>> text[50]
'v'
>>> text[0:5]
'Hello'
>>> text[-1]
'g'
>>> text[-5]
'r'
>>> text[-10]
'e'
>>> text
'Hello this is python and python is used for web development and machine learning'
>>> text[0:30:2]
'Hloti spto n yh'
>>> text[20:0]
''
>>> text[0:20:1]
'Hello this is python'
>>> text[20:0:-1]
' nohtyp si siht olle'
>>> text[20::-1]
' nohtyp si siht olleH'
>>> 
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gninrael '
>>> text[-10:-1]
'e learnin'
>>> text[:]
'Hello this is python and python is used for web development and machine learning'
>>> text[0:]
'Hello this is python and python is used for web development and machine learning'
>>> text[10:]
' is python and python is used for web development and machine learning'
>>> text[:10]
'Hello this'
>>> text[::-1]
'gninrael enihcam dna tnempoleved bew rof desu si nohtyp dna nohtyp si siht olleH'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.capitalize()
'Hello this is python and python is used for web development and machine learning'
>>> text.title()
'Hello This Is Python And Python Is Used For Web Development And Machine Learning'
>>> text.lower()
'hello this is python and python is used for web development and machine learning'
>>> text.upper()
'HELLO THIS IS PYTHON AND PYTHON IS USED FOR WEB DEVELOPMENT AND MACHINE LEARNING'
>>> text.count('p')
3
>>> text.count('e')
8
>>> text.index('p')
14
>>> text.find('p')
14
>>> text.find('p',15)
25
>>> text.find('p',26)
54
>>> 
