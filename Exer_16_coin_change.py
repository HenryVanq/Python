# Exercise 16
import cmath

payment = float(input('Please insert Money: '))

# timi eisitiriou
price = 1.20

# coins
coins = [2.00, 1.00, 0.50, 0.20, 0.10]

# resta
changes = payment - price

if changes == 0:
    print('Take your ticket you have no changes')

elif changes < 0:
    re_money = price - payment
    print 'Remaining money ',round(re_money, 0) # h round voithaei sth morfopoihsh

else:
    #diaperasi sta kermata
    for i in coins:
        times = int(changes/i)
        if  times > 0:
            changes = changes - times*i
            print('{} x {} coin '.format(times, i))


