def largest_swap(num):
	temp = num
	rev = 0
	while temp > 0:
		rev = (rev * 10) + (temp % 10)
		temp //= 10
	return num >= rev