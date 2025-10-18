#"string palindrome ?"
def string (hello):
    newstring=len(hello)
    reversestr=hello[::-1]
    if hello==reversestr:
        return"palindrome"
    else:
        return "not palindrome"
hello=str(input("enter string"))   

print(string(hello))
