''' Write a python program for Fibonacci numbers'''

n=int(input("Enter the number of terms: "))
currentnum=0
nextnum=1
print("The Fibonacci Series: ")
print(currentnum, end=" ")
print(nextnum, end=" ")
for x in range(0,n-2):
    sum=currentnum+nextnum
    print(sum, end=" ")
    currentnum=nextnum
    nextnum=sum

    
