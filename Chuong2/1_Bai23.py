import math 

print('Nhap hai canh ke cua tam giac vuong:')
a = int(input())
b = int(input())
print('Canh ke thu nhat la: ', a,', canh ke thu hai: ', b,', co canh huyen =', round(math.sqrt(a**2+b**2), 2), sep='')