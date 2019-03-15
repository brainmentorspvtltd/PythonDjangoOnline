#Filter
'''
def even(num):
    return num % 2 == 0
'''
#e = even(7)
#print(e)
numbers = [i for i in range(100)]
'''
e = []
for n in numbers:
    if even(n):
        e.append(n)
print(e)
'''

'''
e = list(filter(even, numbers))
print(e)
'''

e = list(filter(lambda num : num % 2 == 0, numbers))
print(e)



