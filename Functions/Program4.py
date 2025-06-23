def palindrome(s):
    reverse=s[::-1]
    if(reverse==s):
        print("this is palindrome")
    else:
        print("Not an palindrome")


palindrome("madam")
