numbers = []
squares = []
cubes = []


start = 1
end = 10


for count in range(start, end + 1):
    numbers.append(count)
    squares.append(count**2)
    cubes.append(count**3)


print("numbers: ", numbers)
print("squares: ", squares)
print("cubes  : ", cubes)
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)