"""
Write a recursive function that checks whether a string is a palindrome (a palindrome is
a string that's the same when reads forwards and backwards.)
"""
def Main():
    input_string = input("Input your string: ")
    return_bool = is_palindrome(input_string)
    
    if (return_bool == True):
        print(f"{input_string} is a palindrome")
    else:
        print(f"{input_string} is not a palindrome")

def is_palindrome(input_string):
    if (input_string == ""):
        return True
    
    if (input_string[0] == input_string[-1]):
        return is_palindrome(input_string[1:-1])

    return False

Main()
