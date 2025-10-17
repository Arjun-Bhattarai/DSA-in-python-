#"functional recursion "
def number(num):
    if num == 0:
        return 0        #"TC is o (n)"
    else:
        return num+number(num-1)  #"yo program chai sum of n natural number ko ho "
num=int(input("enter"))
print(number(num))


#"yo program chai factorial ko ho "
def factorial(f):
    if f==0:
        return 1
    else:
        return f*factorial(f-1)
f=int(input("for factorial"))    
print(factorial(f))