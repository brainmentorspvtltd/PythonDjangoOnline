#Map
def temp_conv(c):return 9/5 * c + 32

#f = temp_conv(45.3)
#print(f)

temp = [34.3,35.5,32.1,36.7,38.8]
#temp_conv(temp)

'''
f = []
for t in temp:
    f.append(temp_conv(t))

print(f)
'''

'''
f = list(map(temp_conv,temp))
print(f)
'''

def myMap(func, iterable):
    data = []
    for i in range(len(iterable)):
        data.append(func(iterable[i]))
    return data

f = myMap(temp_conv, temp)
print(f)



