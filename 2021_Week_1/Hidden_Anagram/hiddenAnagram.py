def hidden_anagram(text, phrase):
	sortedPhrase = "".join(filter(lambda x : x.isalpha() ,sorted(phrase.lower())))
	filteredText = "".join(filter(lambda x : x.isalpha(), text.lower()))
	for i in range(0,len(filteredText)-len(sortedPhrase)+1):
		currentString = filteredText[i:i+len(sortedPhrase)]
		sortedCurrentString = "".join(sorted(currentString.lower()))
		if sortedCurrentString == sortedPhrase:
			return currentString
	return "noutfond"