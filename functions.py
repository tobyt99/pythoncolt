#  exercise 44
# def return_day(day):
#     days = {
#         1 : "Sunday",
#         2 : "Monday",
#         3 : "Tuesday",
#         4 : "Wednesday",
#         5 : "Thursday",
#         6 : "Friday",
#         7 : "Saturday"
#     }
#     if day in days:
#         return days[day]
#     return None

# return_day(5)

# exercise 45
# def last_element(aList):
#     if len(aList) == 0: 
#         return None
#     return(aList.pop())


# exercise 46
# def number_compare(x, y):
#     if x == y:
#         return "Numbers are equal"
#     elif x > y:
#         return "First is greater"
#     return "Second is greater"

# number_compare(15,10)

# print (number_compare(1,1))
# print (number_compare(1,0))
# print (number_compare(0,1))

#  exercise 47
# def single_letter_count(phrase, letter):
#     return phrase.lower().count(letter.lower())

# single_letter_count("I love my dog", "o")

# print(single_letter_count("Hello World", "h"))
# print(single_letter_count("Hello World", "z"))
# print(single_letter_count("HelLo World", "l"))

# exercise 48    
# from collections import Counter
# def multiple_letter_count(string):
#     list(string)
#     return dict(Counter(string))
# multiple_letter_count("awesome")
# print(multiple_letter_count("awesome"))

# def multiple_letter_count(string):
#     return {letter: string.count(letter) for letter in string}
# multiple_letter_count("awesome")
# print(multiple_letter_count("awesome"))    

# exercise 49
# def list_manipulation (aList, command, location, value=None):
#     if (command == "remove" and location == "end"):
#         return aList.pop()
#     elif (command == "remove" and location == "beginning"):
#         return aList.pop(0)
#     elif (command == "add" and location == "beginning"):
#         aList.insert(0, value)
#         return aList    
#     elif (command== "add" and location == "end"):
#         aList.append(value) 
#         return aList 

#  exercise 50

# def is_palindrome(check):
#     check.lower().replace(" ", "")
#     kcehc = "".join(reversed(check))
#     if (check == kcehc): 
#         return True
#     return False

# def is_palindrome(string):
#     stripped = string.replace(" ", "")
#     return stripped == stripped[::-1]