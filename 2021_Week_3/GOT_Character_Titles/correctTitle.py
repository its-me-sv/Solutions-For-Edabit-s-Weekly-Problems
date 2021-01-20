def correct_title(txt):
	def func(x):
		if x in "and the of in":
			return x
		else:
			if "-" in x:
				return "-".join(map(func,x.split("-")))
			else:
				return x[0].upper() + x[1:]
	return " ".join(map(func,txt.lower().split(" ")))