#!usr/env/bin python3

#https://bbookman.github.io/Python-list-comprehension1/

def div_by_7(x):
    print(x)
    
    z=[y for y in x if y%7==0]
    print(z)

def include_3(x):
    z=[y for y in x if str(y).count("3")>0]
    print(z)

def count_spaces():
    #using the count method
    str1=input("Enter the String to count the number of spaces:\t")
    cntSpc1=str1.count(" ")
    print("The number of spaces in the string is: ", cntSpc1)

    #using the list comprehension
    z=[x for x in str1 if x==" "]
    print ("the number os spaces using list comprehension is: ",len(z))

def list_all_consonants():
    inp="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
    z=([x for x in inp if x not in "aeiou"])
    print("".join(z))

def index_value():
    
    tup=["hi",4,8.99,"apple",("t,b","n")]
    z=((i,x) for i, x in enumerate(tup))
    print(tuple(z))

def find_common_numbers():
    list_a = [1, 2, 3, 4]
    list_b = [2, 3, 4, 5]

    z=[x for x in list_a for y in list_b if x==y]
    # another method
    y=[x for x in list_a if x in list_b]
    print(z, y)

def get_numbers():
    str="In 1984 there were 13 instances of a protest with over 1000 people attending"
    str1=str.split(" ")
    z=[x for x in str1 if x.isdigit()]
    print(z)

def even_or_odd():
    inp=list(range(1,20)) 
    z=["even" if x%2==0 else "odd" for x in inp]
    print(z)

def matching_number():
    list_a=[1,2,3,4,5,6,7,8,9]
    list_b=[2,7,1,12]

    z=[(x,x) for x in list_a if x in list_b]

    for x in z:
        print (x, end=" ")

def words_four():
    inp="\nHello my world. Be proud!"
    inpVar=inp.split(" ")
    z=[x for x in inpVar if len(x)<=4]
    print ("The words less than letters are: ", z)

def div_by():
    inp=list(range(1,100))
    z=[x for x in inp if any([True for y in list(range(2,10)) if x%y==0])]
    print(z)


print("Find all of the numbers from 1-1000 that have a 3 in them.\n")
include_3(range(1,1000))

print("Count the number of spaces in a string\n")
count_spaces()

print("Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams\n")
list_all_consonants()

print("Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)")
index_value()

print("Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5")
find_common_numbers()

print("Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending'")
get_numbers()

print("Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even'")
even_or_odd()

print("Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)")
matching_number()

print("Find all of the words in a string that are less than 4 letters")
words_four()

print("Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)")
div_by()