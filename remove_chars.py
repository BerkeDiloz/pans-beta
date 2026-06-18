def remove_chars(word, n):
    print('Original string:', word)
   
    res = word[n:]
    return res

print("Remove letters")
print(remove_chars("Reckless", 6))
print(remove_chars("Reckless", 3))
