def mysplit(strng):
#
# 
#
	#First check all the empty and invalid strings, exclude them from further process...
	if strng =="" or strng.isspace():
		return []
	else:
		word = ""
		myList = []
		#We need to be sure that the first position of the string is not a space.
		isWord = not strng[0].isspace()
		for letter in strng:
			if isWord:
				#If it's a letter, adding it to word
				if not letter.isspace():
					word += letter
				#Otherwise, the word is completed, adding it to the list
				else:
					myList.append(word)
					isWord = False

			#After updating the list, we start the new cycle, adding the first new letter to new word
			elif not letter.isspace():
				word = letter
				isWord = not letter.isspace()
		else:
			#Since the last word won't be added according to the above logic
			#We need to exclusively add it after we finish the entire iteration.
			#For case " abc " the isWord is False, so we take advantage of it
			if isWord:
				myList.append(word)



		return myList



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
