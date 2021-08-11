"""
Write a recursive function that, given a string s, prints the characters of s in reverse order
"""
def main():
    reversed_string = reverse_string(input("Enter string:"))
    print(reversed_string)

def reverse_string(input_string):
    if (input_string == ""):
        return ""
    return reverse_string(input_string[1:]) + input_string[0]

main()
