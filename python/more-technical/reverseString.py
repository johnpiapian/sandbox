# There is an easier way to do it
# however this is a little bit more efficient
# O(n) vs O(n/2), although they are essentially both linear
def reverseString(str):
    left = ""
    right = ""
    start = 0
    end = len(str) - 1
    
    while start != end and start < end:
        left += str[end]
        right = str[start] + right
        start = start + 1
        end = end - 1
    
    if start == end:
        left += str[start]
    
    return left + right