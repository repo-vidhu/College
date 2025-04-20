# finds the largest number



lis=[]
size=int(input("Enter the size of the required array:"))

for i in range(size):
    lis.append(int(input(f"Value to {i+1}th element:")))
lis.sort()

print(f"The largest number is:{lis[size-1]}")