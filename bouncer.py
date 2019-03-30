age = input("How old are you? :")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but you need a writsband")
    elif age >= 21:
        print("Come on in")
    else:
        print("Sorry you can't come in")        
else:
    print("Please enter your age")