'''
py

십진법의 이해 : 10개의 기호를 이용해서 숫자를 표현하는 체계

이진법의 이해 : 2개의 기호를 이용해서 ...

p 1
10 11
100-101 110 111
1000

팔진법 : 0 1 2 3 4 5 6 7

'''


number = 99

#  2진수
b_num = bin(number)

print(b_num)

# 8진수
o_num = oct(number)
print(o_num)
o_num = oct(int(b_num[2:], 2))
print(o_num)

#16진수
h_num = hex(number)
print(h_num)
h_num = hex(int(h_num[2:], 16))
print(h_num)