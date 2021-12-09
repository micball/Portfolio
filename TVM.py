pv = 'potato' #"pv" represents the present value
n2 = 'potato' #"n2" represents the number of compounding periods or the duraiton of the investment
APR = 'potato' #Annual Percentage Rate - expressed as a percent
pmt = 'potato' #Payment per compounding period
cpd = 'potato' #Number of times the interest compounds per period
fv = 0
n = 0
n3 = 0
print('Welcome to the TVM Calculator - this is just a project for me to figure out a slightly more complex program.')
print('As it currently stands, this program exclusively calculates interest growth on funds, no debt payment calculator.')
print('This TVM Calculator was built by Michael.')
while pv == 'potato' :
    try:
        pv = float(input('Principal Value? '))
    except:
        print('Invalid input, please enter a number. ')
print('PV =', pv)
while n2 == 'potato' :
    try:
        n2 = float(input('Time? '))
    except:
        print('Invalid input, please enter a number. ')
print('Time =', n2)
while APR == 'potato' :
    try:
        APR =float(input('APR? '))
    except:
        print('Invalid input, please enter a number. ')
print('APR =', APR)
while pmt == 'potato':
    try:
        pmt = float(input('How much is each payment? '))
    except:
        print('Invalid input, please enter a number.')
print('Payment =', pmt)
while cpd == 'potato' :
    try:
        cpd = float(input('How many times does interest compound per period? '))
    except:
        print('Invalid input, please enter a number.')
print('There are', cpd, 'compounding periods per interest period.')
print()
print()
x = pv
x2 = pv
while n < n2 :
    x = x*(1+APR/100) + pmt
    n = n+1
fv = x
while n3 < n2 :
    x2=(pmt+x2)*(1+APR/100)
    n3 = n3+1
fv2 = x2
print()
print('Assuming payments at the end of each period, your future value will be:')
print()
print('$ '), print(fv)
print()
print('Assuming payments at the beginning of each period, your future value will be:')
print()
print('$ '), print(fv2)
