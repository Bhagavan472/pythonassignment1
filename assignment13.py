string = input("Enter a string: ")
alphabets = 0
digits = 0
specialchars = 0
for i in string:
    if i.isalpha():
        alphabets+=1
    elif i.isdigit():
        digits+=1
    else:
        specialchars+=1
print("alphabets =", alphabets, "digits =", digits, "specialchars =", specialchars)
        
        
        