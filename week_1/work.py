# program to show how to perform volume  annd suface area of a cylinderand sphere
# date: 20/2/2024
# name : wesley miruye

# cylinder
pi = 3.142
r= float(input("enter the radius"))
h = float(input("enter the height"))
r_sq = (r ** 2)

v = (pi * r_sq * h)
sa = ((2 * pi * r_sq * h)) + ( 2 * pi * r_sq)
print("volume of cylinder is" , v)
print("the surface area of the cylinder is", sa)

# sphere
pi = 3.142
r = float(input("enter the radius"))
r_sq = (r** 2)
r_cd = (r**8)
a = ( 4/3)
v = a * pi * r_cd
sa = ( 4 * pi * r_sq)

print(" the volume of the sphere is" , v)
print("the surface area of the sphere is ", sa)



