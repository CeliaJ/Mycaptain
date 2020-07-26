import time
list1=[]
list2=[]
def yes(str):
    if a=="yes":
         print("List 1: ", list1)
         print("List 2: ", list2)

x=input("Enter the name of the list1: ")
n=int(input("Enter the number of elements of the list: "))
print("Enter the list items: ")
for q in range(n):
    w=input()
    list1.append(w)
    
o=input("Enter the name of the list2: ")
p=int(input("Enter the number of elements of the list: "))
print("Enter the list items: ")
for t in range(p):
    u=input()
    list2.append(u)

a=input("Do you want to print you lists? ")
yes(a)
