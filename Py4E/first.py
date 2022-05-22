#A basic compounding interest calculator. :)
n=100
x=input('Present Value? ')
x=int(x)
interest= input("APR? ")
interest= float(interest)
while n > 1:
    x=x*interest
    n=n-1
if n == 1:
    print(x)
    n=0
#using the elif
x = input('choose a number between one and ten')
if x < 2 :
    print('Higher')
elif x = 2 :
    print('you found the elif')
else: x > 2 :
    print('lower')
#learning about try/except structure.  everthing inside of the try box will be run up until it crashes.
astr= 'bob'
try:
    print('hello')
    istr = int('astr')
    print('there')
except:
    istr=-1
print('done')

#playing with "def" functions
 x = x - 30000

#Loops and Iterations
input('')
