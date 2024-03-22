# strings in python
# date : 22/2/2024
# name : wesley miruye

city = "nairobi"

print( city[0]) # n
print( city[1]) # a
print( city[2]) # i
print( city[3]) # r
print( city[4]) # o
print( city[5]) # b
print( city[6]) # i
print( city[-1])
print( city[-2])

# convert to upper case


print(city)
print("\n\n") # print a new line
print(city.upper())
name = "WESLEY MIRUYE"
print(name)
print(name.lower()) # convert name to lower case

town = "  Naivasha   "

print(town)
print("\t") # new tab
print(town.strip())

# add two strings

f_name = "ja"
s_name = "ba"
full_name = f_name + s_name

print(full_name)

#replacing a character

fruit = "orange"
print(fruit.replace("o","y"))

subject = "physical,sciences"
print(subject.split(","))

age = 18
height = 1.7
print("i am {0} years old and {1} meters tall".format (age , height))

activity = "dancing"
print("my hobby is %s" %(activity))

height = 1.23449499
print("my height is %5.4f " %(height))

#printing an integer
age = 18
print("my age is %d"%(age))

name = "wesley miruye"
print(len(name))

print(f"my full  name is {name} ")
school = "engineering"
course = "elecrical"
print("i am studying {course} in the school of {school}" . format (course = "medicine" , school = "human sciences"))