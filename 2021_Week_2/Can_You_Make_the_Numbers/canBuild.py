def can_build(digits, lst):
	for num in lst:
		if not num:
			digits[num] -= 1
		while num != 0:
			digits[num%10] -= 1
			num //= 10
		for cnt in digits:
			if cnt < 0:
				return False
	return True