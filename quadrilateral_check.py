def is_trapezoid(a,b,c,d):
    sides = [a,b,c,d]
    longest = max(sides)
    others_sum = sum(sides) - longest
    
    if others_sum > longest:
        return "possible" 
    else:
        return "not possible"
        
print(is_trapezoid(2,1,8,10))
