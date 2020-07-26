import time
d={}
def yes(v):
    if v=="yes":
        delvar=input("Enter the key to be deleted: ")
        d.pop(delvar, None)
    print("The updated dictionary is:",end=" ")
    print(d)
        
n=int(input("Enter the number of elements in the dictionary: "))
print("Enter the elements: ")
for g in range(n):
    print("Enter the key: ")
    keys=input()
    print("Enter the value: ")
    value=int(input())
    d[keys]=value

print("The dictionary is : ",end=" ")
print(d)
time.sleep(1.5)
j=input("Do you want to delete a key? ")
yes(j)

