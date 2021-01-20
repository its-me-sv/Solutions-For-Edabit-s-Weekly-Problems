def find_nemo(sentence):
	try:
		ans = sentence.split().index("Nemo")
		return "I found Nemo at {}!".format(ans+1)
	except:
		return "I can't find Nemo :("