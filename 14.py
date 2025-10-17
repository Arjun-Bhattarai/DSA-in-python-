#"array reverse using recursion"
def reverse_array(num):
    if len(num) == 0:         
        return []
    else:                     
        return [num[-1]] + reverse_array(num[:-1])

arr = list(map(int, input("Enter array elements: ").split()))
print(reverse_array(arr))
