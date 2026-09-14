word = input("Enter a word to check palindrome:")
word1 = word[::-1]
if word == word1:
    print("Given Word is Palindrome")
else:
    print("Given word is not Palindrome")