a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == b and a == c:
    print("3 numbers are the same")
elif a == b or a == c or b == c:
    print("2 numbers are the same")
else:
    print("no same numbers")