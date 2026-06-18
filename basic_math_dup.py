def add(a, b):
    return a+b 
    
def multiplay (a,b):
    return a*b 
    
def divide(a,b):
    if b == 0:
        return "You can not divide by 0!!!"
    else:
        return a/b
a = 18
b = 3
print (f"{a} + {b} = {add(a,b)}")
print (f"{a} * {b} = {multiplay(a,b)}")
print (f"{a} / {b} = {divide(a,b)}")
