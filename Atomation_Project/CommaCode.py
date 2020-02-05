spam = ['apples', 'bananas', 'tofu', 'cats']
lst = []

def listTostr(inputlist):
    for element in range(len(inputlist)):
        print(inputlist[element], end = '')
        if element < (len(inputlist) - 1):
            print(', ', end = '')
    print('.')

#take the number of elements to be in list
n = int(input("enter the number of elements: "))

#iterate to get the list elements
for i in range(0,n):
    ele = input()
    lst.append(ele) # adding the element

listTostr(spam)

listTostr(lst)

