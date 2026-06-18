height_cm = 190
feet = int (height_cm / 30.48)
rest = 190 - feet*30.48
inches = round(rest/2.54)
print(feet)
print(inches)
