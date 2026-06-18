text = "Python is a good language. C# is also a good langauge."
length = len(text)

letter_a = 0

for x in text:
    if x=='a':
        letter_a +=1
print(f"the number of letter a is {letter_a}")
