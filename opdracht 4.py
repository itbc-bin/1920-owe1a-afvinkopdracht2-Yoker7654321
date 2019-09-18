item1 = float( input ('Please enter the price of the first item: '))
item2 = float( input('Please enter the price of the second item: '))
item3 = float( input('Please enter the price of the third item: '))
item4 = float( input('Please enter the price of the fourth item: '))
item5 = float(input('Please enter the price of the fifth item: '))

subtotal = item1 + item2 + item3 + item4 + item5

tax = 0.07 * subtotal

totalpurchase = subtotal + tax

print('subtotal is' , subtotal)
print('tax amount is' , tax)
print('total purchase is' , totalpurchase)