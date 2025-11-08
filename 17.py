#"bubble shorting"
number=list(map(int,input().split()))
num=len(number)

for i in range(num-1):
    for j in range (num-i-1):
        if number[j]>number[j+1]:
           number[j],number[j+1]=number[j+1],number[j]
print(number)    
           

