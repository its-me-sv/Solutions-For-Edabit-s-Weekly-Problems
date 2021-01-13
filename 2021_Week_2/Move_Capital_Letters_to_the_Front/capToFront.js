const capToFront = s => {
	let lowerCase = "", upperCase = "";
	for (let i of s){
		if (i == i.toLowerCase())
		lowerCase += i;
		else
		upperCase += i
	}
	return upperCase + lowerCase;
};