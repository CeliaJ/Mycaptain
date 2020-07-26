import time
tuple1=()
list3=[]
name=input("Enter the name of the tuple: ")
num=int(input("Enter the number of elements: "))
print("Enter the elements: ")
for var in range(num):
    ele=input()
    list3.append(ele)
    
tuple1=tuple(list3)

y=int(input("Enter the item number of the tuple to be accessed: "))
print("Fetching your data... ")
time.sleep(2)
print("The item with the number %d is: "%y, end=" ")
print(tuple1[y-1])

