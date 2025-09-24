#"1 prime check"
flag=0
n=int(input("enter number to check if prime from 1 to 50 "))
if n==0 or n==1:
    print("not prime number")
for num in range (2,n):
    if n%num==0:
        flag=2

if flag==2:
    print(n,"not a prime number")
else:
    print(n,"number is prime number")


