#This program check whether the data is a palindrome or not

data=input("Enter the content:")
flag=0
for i in  range(len(data)):
    if data[i].lower()!=data[len(data)-i-1].lower():
        flag=1
        break
if flag==0:
    print(f"The word {data} is a Pallindrome")
else:
    print(f"The word {data} is not a Pallindrome")