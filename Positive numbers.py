''' Write a python progra to print all the positve numbers in a range'''

list1=[]
n=int(input("Enter the number of elemnts: "))
print("Enter all elements: ")
for x in range(n):
      i=int(input())
      list1.append(i)
print("The positive numbers are: ")
for y in range(n):
    if (list1[y]>=0):
        print(list1[y], end=" ")
        
        
        
