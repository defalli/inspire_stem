friends = ["tom"," jerry", "alan", "sandy ","kate "]

for  friend in friends:
    print(friends)

enemies = friends[:] # to copy one list into another
print (enemies)

fruits = ["jerr" "gum" "fofo" "loop"]
#slice the list to get part of the list
print(fruits[0:3])

del fruits[0]
print(fruits)
squares = [] #initialize an empty list

for x in range(0,11):
    squares.append(x**2)
print(squares)