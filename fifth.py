#"Reverse a List without using slicing or reverse()."
hello = []
hi = list(map(int, input().split()))

for i in range(len(hi) -1):
    hello.append(hi[i]) 

print(hello)
