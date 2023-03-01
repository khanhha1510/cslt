x = float(input('x='))
y = float(input('y='))
a = input('Phep toan:')

if a == '+':
    print(x,'+',y,'=',x+y)
elif a == '-':
    print(x,'-',y,'=',x-y)
elif a == '*':
    print(x,'*',y,'=',x*y)
elif a == '/':
    print(x,'/',y,'=',x/y)
else:
    print('Khong hop le')