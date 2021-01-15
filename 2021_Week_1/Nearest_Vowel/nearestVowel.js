const nearestVowel = s => {
	let near, i;
	s = s.charCodeAt(0);
	i = Math.abs(s - 97);
	near = "a";
	if (Math.abs(s - 101) < i){
		i = Math.abs(s - 101);
		near = "e";
	}
	if (Math.abs(s - 105) < i){
		i = Math.abs(s - 105);
		near = "i";
	}
	if (Math.abs(s - 111) < i){
		i = Math.abs(s - 111);
		near = "o";
	}
	if (Math.abs(s - 117) < i){
		i = Math.abs(s - 117);
		near = "u";
	}
	return near;
};