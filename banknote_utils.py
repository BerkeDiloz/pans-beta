def how_many_notes(height):
    thickness = 0.11 #mm 
    number_of_banknotes = round(height/thickness)
    return number_of_banknotes
    
height_of_column = 1000 #mm
print(how_many_notes(height_of_column))

def value_of_column(height, denomination):
    return how_many_notes(height)*denomination
    
print(value_of_column(1000, 100))
