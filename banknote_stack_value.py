thickness = 0.11 #mm 
column = 1000# 1m = 1000mm
number_of_banknotes = round(column/thickness)
note = 100 #value of one banknote
value = number_of_banknotes * note 
print (f"In 1 the column of meter we have {number_of_banknotes}")
print (f"the Value of 1 meter is {value}$")
print (f"1000000000$ will be {round(1000000000/value)} m high.")
