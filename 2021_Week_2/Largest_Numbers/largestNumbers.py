def largest_numbers(n, lst):
	return sorted(lst)[-n:] if n > 0 else []