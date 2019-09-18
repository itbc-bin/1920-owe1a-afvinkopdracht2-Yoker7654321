#Base value 48
#1.5 sugar
#1 butter
#2.75 flour

ac = float(input('What is the amount of cookies that you want to bake? : '))

bsugar = 1.5/48
bbutter = 1/48
bflour = 2.75/48

fsugar = bsugar * ac
fbutter = bbutter * ac
fflour = bflour * ac

print('You will need', fsugar, 'cup(s) of sugar')
print('You will need', fbutter, 'cup(s) of butter')
print('You will need', fflour , 'cup(s) of flour')