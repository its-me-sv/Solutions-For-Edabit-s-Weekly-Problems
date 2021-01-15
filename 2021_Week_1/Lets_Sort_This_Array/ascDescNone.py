def asc_des_none(lst, s):
	return sorted(lst) if s == "Asc" else sorted(lst)[::-1] if s == "Des" else lst