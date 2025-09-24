#"2 sum of list"
total=0
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
for i in numbers:
    total+=i
    print(total)
    