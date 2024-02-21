# program to  solve a quadratic equation
# date : 20/2/2024
# name : wesley miruye
a = float(input(" enter the coefficient of first term :"))
b =float (input(" enter the coefficient of second term :"))
c =float(input("enter the constant :"))




d = (float (b)**2) - 4 *float(a) * float(c))


x_1 = (-b + sqrt (d) ) / 2 * a
x_2 =(-b - sqrt (d) ) / 2 * a

print("the solution of the quadtratic equation is :",x_1)
print("the solution of the quadtratic equation is :",x_2)