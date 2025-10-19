#"shorting in python :selection shorting"
num=list(map(int,input().split()))
new=len(num)
i=0
for i in range(new):
 min_index=i

 for j in range(i+1,new):
    
         if num[j]<num[min_index]:
            min_index=j
 num[i],num[min_index]=num[min_index],num[i]
print(num)