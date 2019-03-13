'''
range(5) - start = 0, stop = 5, step = 1
range(2,10) - start = 2, stop = 10, step = 1
range(1,20,2) - start = 1, stop = 20, step = 2
range(20,1,-1) - start = 20, stop = 1, step = -1
'''
for var in range(8):
    print(var)
    print("Inside Loop")
print("Outside Loop")

for i in range(2,20,2):
    print(i, end='')
