

# Frequency mapping garne process ho  dict ma 
my_list = list(map(int, input("Enter numbers: ").split()))
my_dict = {}

for i in my_list:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print(my_dict)
