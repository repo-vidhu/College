#program to check whether  a number is prime or not

num=int(input("Enter the number to check whether is prime or not:"))

def prime(n):
    flag=0
    for i in range(2,n//2):
        if n%i==0:
            flag=1
            break
        else:
            continue
    if flag==0:
        print(f"The number {n} is prime")
    else:
        print(f"The number {n} is not prime")

prime(num)