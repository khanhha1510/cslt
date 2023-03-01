a = float(input())
b = float(input())
c = float(input())

TB = ((a*2)+(b*3)+c)/6

if TB < 3:
    print('Kém')
elif 3 <= TB < 5:
    print('Yếu')
elif 5 <= TB < 6:
    print('Trung bình')
elif 6 <= TB < 7:
    print('Trung bình khá')
elif 7 <= TB < 8:
    print('Khá')
elif 8 <= TB < 9:
    print('Giỏi')
else: 
    print('Xuất sắc')