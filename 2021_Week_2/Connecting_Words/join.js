const longestCommon = (prevStr, currStr) => {
	let max = 0, j = 0;
	for (let i in prevStr){
		if (prevStr[i] == currStr[j])
		j += 1;
		else{
			max = j > max ? j : max;
			j = 0;
			if (prevStr[i] == currStr[j])
			j += 1;
		}
	}
	return j > max ? j : max;
};
const join = arr => {
	let ans = arr[0], min = 10000, len;
	for (let i = 1; i < arr.length; i += 1){
		len = longestCommon(arr[i-1],arr[i]);
		ans += [...arr[i]].slice(len).join("");
		min = min < len ? min : len;
	}
	return [ans, min];