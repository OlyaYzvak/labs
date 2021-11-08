a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
D = pow(b, 2) - 4 * a * c
print("дискримінант: ", D)
if D > 0:
    print("квадратне рівнянн має два корені")
elif D == 0:
    print("квадратне рівняння має один корінь")
else:
    print("кввадратне рівняння не має коренів")