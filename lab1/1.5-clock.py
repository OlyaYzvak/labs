import sys
hours = int(input("введіть години: "))
if(hours > 24):
    sys.exit("НЕКОРЕКТНЕ ВВЕДЕННЯ!")


minutes =int(input("введіть хвилини: "))
if(minutes > 60 or hours == 24 and minutes > 0 ):
    sys.exit("НЕКОРЕКТНЕ ВВЕДЕННЯ!")
print("хвилини:")
print(hours * 60 + minutes)
print("секунди:")
print(hours * 60 * 60 + minutes * 60)




