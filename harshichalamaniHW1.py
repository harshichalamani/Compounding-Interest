#Harshi Chalamani 
print('How far would you run?')
run = input()
print('How fast will you run (please enter decimal, like 7.5 for 7:30 pace)?')
pace = input()
cal = float(run) * float(pace)
print('It will take you ' + str(cal) + 'minutes to run ' + run)



print('Now lets calculate the future value of a investment')

print('Please enter principle:')
p = float(input())

print('Please enter annual interest rate (example 5.2 for 5.2%):')
r = float(input())


print('Please enter the term in years:')
n = float(input())


print('Please enter number of times the interest will compound per year:')
t = float(input())


a = p*(((1+(r/100)/n))**(n*t))

print('in ' + str(n) + 'years, at the interest rate of ' + str(r) +
    '% compunded' + str(t) + 'times per year, the initial amount of $' + str(p) + 'will be worth $' + str(a) + ' . ')


print('Now lets do some negotiation')

spend = 500

print('How much are you asking?')
price = float(input())

if price > spend:
    print('Sorry, that price u=is too high for me.')
elif price < spend or price == spend:
    print('Ok, I would like to purchase it.')



print('Welcome to the currency calculator!')

yd = 0.0012
ye = 0.0067
yp = 0.0057
de = 0.93
dp = 0.80
ep = 0.86

dy = 139.54
ey = 150.25

result = 0
curr1 = ""
curr2 = ""

print('Enter the amount:')
amount = float(input())

print('Enter the original currency:')
currency = input()

print('Enter the new currency:')
newCurrency = input()

rateType = currency + newCurrency

if rateType == 'yd':
    result = amount * yd
    curr1 = 'Yen'
    curr2 = 'Dollar'
    #print("%.2f" % result)
    #print(result)
elif rateType == 'ye':
    result = amount * ye
    curr1 = 'Yen'
    curr2 = 'Euro'
    #print(result)
elif rateType == 'yp':
    result = amount * yp
    curr1 = 'Yen'
    curr2 = 'Pound'
    #print(result)
elif rateType == 'de':
    result = amount * de
    curr1 = 'Dollar'
    curr2 = 'Euro'
    #print(result)
elif rateType == 'dp':
    result = amount * dp
    curr1 = 'Dollar'
    curr2 = 'Pound'
    #print(result)
elif rateType == 'ep':
    result = amount * ep
    curr1 = 'Euro'
    curr2 = 'Pound'
    #print(result)
elif rateType == 'dy':
    result = amount * dy
    curr1 = 'Dollar'
    curr2 = 'Yen'
    #print(result)
elif rateType == 'ey':
    result = amount * ey
    curr1 = 'Euro'
    curr2 = 'Yen'
    #print(result)

print(str(amount) + ' ' + curr1 + '(s) is worth ' + str(result) + ' ' + curr2 + '(s)')


