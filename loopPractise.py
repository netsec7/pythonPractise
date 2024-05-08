#!usr/bin/env python3
#Loop Exercise


#https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

import math

def pattern1():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j, end=" ")
        print("")

def sum_of_all():
    z=0
    x=int(input("Enter the number you want to sum the range"))
    for i in range(x+1):
        z=z+i
    print(z)

def print_multi():
    x=int(input("Enter the number for multiplication table: "))
    for y in range(1,x+1):
        z=y*x
        op="{0} x {1} = {2}"
        print(op.format(y,x,z))

def display_list():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    z=[x for x in numbers if x%5==0]
    for y in z:
        print(y, end="\n")

def count_digits():
    x=1000
    cnt=0
    while x!=0:
        x=x//10
        cnt+=1
    print(cnt)

def pattern2():
    for x in range(5,0,-1):
        for y in range(x,0,-1):
            print(y, end=" ")
        print("")

def reverse_list():
    lst=[10,11,12,13]
    x=len(lst)
    newList=[]
    while x!=0:
        x-=1
        newList.append(lst[x])
    print("reverse list is ",newList)

def display_prime():
    primeNumber=[]
    for x in range(1,100):
        if x>1:
            for i in range(2,x):
                if x%i==0:
                    break
            else:
                primeNumber.append(x)
    print("The Prime Numbers are:", primeNumber )

def print_fibo():
    x=0
    y=1
    cnt=0
    try:
        inp=int(input("How may number of fibonacci series do you require? :"))
        while cnt!=inp:
            print(x, end=" ")
            z=x+y
            x=y
            y=z
            cnt+=1
           
    except:
        print("Enter only integer value")
    print("")#EOL
def print_factorial():
    x=1
    fact=int(input("factorial value? "))
    
    for i in range(1,fact+1):
        x=i*x
    print(f"the Factorial value of {fact} is: ", x)

def reverse_number():
    x=765432
    z=str(x)
    length=len(z)
    lst=[None]*length
    for i in z:
        length=length-1
        lst[length]=i
    res=int("".join(lst))
    print(res)

    #another method
    rev=0
    while x!=0:
        rem=x%10
        rev=rev*10+rem
        x=x//10
        
    print("another method to reverse a number done and the result is: ", rev)

def odd_list_print():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    cnt=0
    newList=[]
    for x in my_list:
        if cnt%2!=0:
            newList.append(x)
        cnt+=1
    print(newList)

def calc_cube():
    inp=int(input("what number do you require to print? "))
    for i in range(inp+1):
        result=int(math.pow(i,3))
        print(f"/n The Cube of {i} is {result}")

def sum_series():
    inp= int(input("Enter the n term: "))
    sum=0
    res=0
    for i in range(inp):
        sum=sum*10+2
        res=sum+res
    print(res)
    
def print_pattern2():
    y=0
    r=10
    for x in range(r):
        if x<=int(r/2):
            for y in range(x):
                
                print("*", end="")
        else:
            for z in range(y,0, -1):
                print("*", end="")
            y=y-1
        print("")

print("Exercise 2: Print the following pattern")
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
pattern1()

print("Calculate the sum of all numbers from 1 to a given number")
sum_of_all()

print("Excersie 4: Write a program to print multiplication table of a given number")
print_multi()

print("Exercise 5: Display numbers from a list using loop. Write a program to display only those numbers from a list that satisfy the following conditions")
    # The number must be divisible by five
display_list()

print("Count the total number of digits in a number")
count_digits()

print("Exercise 7: Print the following pattern")
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
pattern2()

print("Exercise 8: Print list in reverse order using a loop")
reverse_list()

print("Exercise 11: Write a program to display all prime numbers within a range")
display_prime()

print("Display Fibonacci series up to 10 terms")
print_fibo()

print("Exercise 13: Find the factorial of a given number")
print_factorial()

print("Exercise 14: Reverse a given integer number")
reverse_number()

print("Exercise 15: Use a loop to display elements from a given list present at odd index positions")
odd_list_print()

print("Exercise 16: Calculate the cube of all numbers from 1 to a given number")
calc_cube()

print("Exercise 17: Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690")
sum_series()

print("Exercise 18: Write a program to print the following start pattern using the for loop")
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
print_pattern2()