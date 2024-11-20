import string

text = input("Input your text: ")

alpha = list(string.ascii_lowercase)
text = list(text.lower())

answer = [] 

for letter in text:
	result = alpha.index(letter)
	answer.append(result + 1)

print(answer)