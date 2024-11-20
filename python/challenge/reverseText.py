# This code sorts every word in alpha-order
# Example: "hello world" becomes "ehllo dlorw"

def isWord(text):
	return len(text.split(" "))

def sortWord(word):
	return ''.join(sorted(word))

def sortText(text):
    text = text.split(" ")
    for i in range(len(text)):
        text[i] = sortWord(text[i])
    return ' '.join(text)
	

text = input("Input your text: ")
print(sortText(text))