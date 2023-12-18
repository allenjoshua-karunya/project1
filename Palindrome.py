#Palindrome
def isPalindrome(s):
    return s == s[::-1]
s = str(input("word? :"))
ans = isPalindrome(s)
if ans:
    print("given word is a palindrome")
else:
    print("given word is not a palindrome")