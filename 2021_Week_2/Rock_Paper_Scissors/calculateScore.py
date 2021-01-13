def calculate_score(games):
	abigail = benson = 0
	for a, b in games:
		if a == b:
			continue
		elif a == "P":
			if b == "R":
				abigail += 1
			else:
				benson += 1
		elif a == "R":
			if b == "S":
				abigail += 1
			else:
				benson += 1
		else:
			if b == "P":
				abigail += 1
			else:
				benson += 1
	return "Abigail" if abigail > benson else "Benson" if benson > abigail else "Tie"