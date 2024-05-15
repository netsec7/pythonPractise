#!usr/bin/env python3
#https://pynative.com/python-list-exercise-with-solutions/#h-exercise-9-replace-list-s-item-with-new-value-if-found

def concatinate_list():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    newList1=[]
    newList2=[]
    for i,x in enumerate(list1) :
        newList1.append(list1[i]+list2[i])
    print("Method 1: ", newList1)

    for x, y in zip(list1, list2):
        newList2.append(x+y)
    print("Method 2: Using Zip method",newList2)

    z=list(zip(list1[3], list2[3], "xyza"))
    print(z)

def iterate_both_list():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    for x, y in zip(list1, list2[::-1]):
        print(x, y)

def remove_empty_list():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    z=[x for x in list1 if x!=""]
    print(z)
    
    result=list(filter(None,list1))
    print(result)

def add_between_list():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    j=0
    try:
        for i,x in enumerate(list1,start=0):
        
            try: 
                for y in x:
                    try: 
                        for z in y:
                            if z==6000:
                                print(z)
                                list1[i][j].append(7000)
                    except:
                        pass
                    j=j+1
            except:
                pass
    except:
        pass
    print(list1)

def extend_list():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

    # sub list to add
    sub_list = ["h", "i", "j"]
    res=list1[2][1][2].extend(sub_list)
    print(list1, "***", res)

def replace_item():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    i=list1.index(20)
    list1[i]=200
    print (list1)

print("Exercise 2: Concatenate two lists index-wise")
concatinate_list()

print("Exercise 5: Iterate both lists simultaneously")
iterate_both_list()

print("Exercise 6: Remove empty strings from the list of strings")
remove_empty_list()

print("Write a program to add item 7000 after 6000 in the following Python List")
add_between_list()

print("Exercise 8: Extend nested list by adding the sublist")
extend_list()

print("Exercise 9: Replace list’s item with new value if found")
replace_item()