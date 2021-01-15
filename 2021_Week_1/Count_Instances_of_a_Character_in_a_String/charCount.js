const charCount = (myChar, str) => {
	let cnt = 0;
	for (let i of str)
		if (i === myChar)
			cnt++;
	return cnt;
};
// return [...str].filter(x => x == myChar).length;