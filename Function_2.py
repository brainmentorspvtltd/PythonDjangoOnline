# default arguments
def calc(x=0,y=0):
    z = x + y
    print(z)

#calc(4,5)
#calc(5)
calc(x=5,y=10)

# *args and **kwargs
# Dynamic Arguments
def emp(id,name,dept,*address):
    print(id,name,dept,address)

emp(101,'Ram','IT','pune')
emp(101,'Ram','IT','pune','delhi')
emp(101,'Ram','IT','pune','chennai','delhi')

def emp(**details):
    print(details)

emp(name='ram',dept='IT',sal=45000)
emp(id=102,name='shyam',dept='HR')
emp(id=103,name='raman',dept='IT',sal=40000)
