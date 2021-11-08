result = 0
print("Як перекладається слово apple?")
print("a) яблуко")
print("б) апельсин")
print("в) огірок")
print("г) помідор")
answer = input("Відповідь: ")
if answer == "а":
    result = result + 1
print("Як перекладається слово cucamber?")
print("a) яблуко")
print("б) апельсин")
print("в) огірок")
print("г) помідор")
answer = input("Відповідь: ")
if answer == "в":
    result = result + 1
print("Як перекладається слово orange?")
print("a) яблуко")
print("б) апельсин")
print("в) огірок")
print("г) помідор")
answer = input("Відповідь: ")
if answer == "б":
    result = result + 1
print("Як перекладається слово tomato?")
print("a) яблуко")
print("б) апельсин")
print("в) огірок")
print("г) помідор")
answer = input("Відповідь: ")
if answer == "г":
    result = result + 1
print("Як перекладається слово banana?")
print("a) яблуко")
print("б) банан")
print("в) огірок")
print("г) помідор")
answer = input("Відповідь: ")
if answer == "б":
    result = result + 1
print("Кількість правильних відповідей: ", result)
if result >= 3:
    print("Ви прийняті на роботу!")
else:
    print("Ви не прийняті на роботу!")

