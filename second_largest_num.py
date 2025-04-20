# finds the second largest number

lis=[]
size=int(input("Enter the size of the required array:"))

for i in range(size):
    lis.append(int(input(f"Value to {i+1}th element:")))
lis.sort()

print(f"The Second largest number is:{lis[size-2]}")