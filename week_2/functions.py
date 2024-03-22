def print_name() :
    print("my name is wesley miruye")


# calling the function
print_name()


def print_details(name, age, id ,gender):
    print("i am {0}, i am {1} years old, my id no is {2}, and my gender is {3} " . format(name, age, id ,gender))
print_details("wesley","18","21998048","male")
print_details("esley","19","200000048","female")

def sum_nums(x,y):
    return x + y

def prod_nums(x,y):
    return x * y

z= sum_nums(10,20)
print(z)
print(prod_nums(3,2))

def print_odds(first_no, last_no):
    for i in range(first_no,last_no):
        print(i % 2)

print_odds(0,15)

