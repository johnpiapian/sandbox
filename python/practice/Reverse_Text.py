#This code sorts every word in alpha-order

def isaword(text):
	return len(text.split(" "))

def textsort(word):
	return ''.join(sorted(word))


text = input("Input your text: ")

if isaword(text) > 1:
	text = text.split(" ")
	for i in range(len(text)):
		text[i] = textsort(text[i])
else:
	text = textsort(text)

print(text)