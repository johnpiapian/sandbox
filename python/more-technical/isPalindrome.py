def isPalindrome(str):
    if len(str) <= 1:
        return True
    elif len(str) == 2:
        return str[0] == str[1]
    else:
        if str[0] == str[len(str) - 1]:
            return isPalindrome(str[1:-1]) # strip the first and last character
        else:
            return False