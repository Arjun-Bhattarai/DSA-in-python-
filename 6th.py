#"reverse an number"
n=int(input("enter number to reverse"))
num=n
while num > 0:
    digit=num%10
    print(digit)
    num=num//10


