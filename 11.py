#"hashing in py is like a table of contain which make data finding easy "
first=list(map(int,input("enter values ").split()))#"first ma only 0 to 10"
second=list(map(int,input("enter values").split()))
my_dict={}
for num in first:
    if num in my_dict:
        my_dict[num]+=1       #"time complexity chai 0(m+n) because two for loops first and second"
    else:
        my_dict[num]=1    
result={}
for num in second:
    result[num]=my_dict.get(num,0)
print(result)    
#".get() la chai key find garxa if key xa vana true else false "

#"another method using hash"
hash_list=[0]*11 #"aasla 11 oota array banauxa from 0 to 11 jasko value starting ma 0 hunxa "
for num in first:
    hash_list[num]+=1
for num in second:
    if num<0 or num>10:
        print(0)   
    else:
        print(hash_list[num])    