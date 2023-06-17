def is_palindrome(word):
    return word == word[::-1]

word = "level"
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
