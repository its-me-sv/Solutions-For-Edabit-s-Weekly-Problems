def cap_to_front(s):
	upperCase = lowerCase = ""
	for i in s:
		if i.isupper():
			upperCase += i
		else:
			lowerCase += i
	return upperCase + lowerCase