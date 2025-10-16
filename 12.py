#"recursion theory:function calling itself"

def fibonacci(num):
    if num==0 or num==1:
        return 1    #"yo chai head recursion ho aasama where function is called at last"
    else:
        return fibonacci(num-1)+fibonacci(num-2)

num=int(input("enter number for fibonacci"))    
for i in range (num):
   print(fibonacci(i))
#"arko program"
def func():
    count=0
    if count==4:
        return
    count+=1
    func()
    print("Arjun")