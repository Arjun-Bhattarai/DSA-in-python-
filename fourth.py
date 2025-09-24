#"Find Maximum in a List."
number=list(map(int,input().split()))
max=number[0]
for i in number:
    if i>max:
        max=i
print(max)