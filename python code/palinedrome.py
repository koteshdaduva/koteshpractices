def is_palindrome_number(n):
    return str(n) == str(n)[::-1]  # Convert to string, reverse, and compare

num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
