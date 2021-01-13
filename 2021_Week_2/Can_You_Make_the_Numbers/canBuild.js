const canBuild = (digits, arr) => {
	let digit;
	for (let num of arr){
		if (num == 0)
		digits[num] -= 1;
		while (num != 0){
			digit = num % 10;
			digits[digit] -= 1;
			num -= digit;
			num /= 10;
		}
		if (digits.some(i => i < 0) == true)
		return false;
	}
	return true;
};