a = int(input('enter number: '))
b = int(input('enter number: '))
c = int(input('enter number: '))
if a == b and a == c and b == c:
    print('yes')
elif a == b or a == c or b == c:
    print('yes')
else:
    print('error')