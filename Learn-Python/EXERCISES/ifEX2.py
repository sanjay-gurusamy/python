tax = 0
honda = int(input('Enter the price of the bike'))
if honda >100000:
    tax = 15/100*honda
elif honda >50000 and honda <=100000:
    tax = 10/100*honda
else :
    tax = 5/100*honda
print('Tax to be paid',tax)