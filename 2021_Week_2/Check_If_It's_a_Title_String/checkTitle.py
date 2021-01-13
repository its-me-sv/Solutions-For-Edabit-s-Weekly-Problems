def check_title(txt):
	return all(map((lambda x : x[0].isupper()), txt.split()))