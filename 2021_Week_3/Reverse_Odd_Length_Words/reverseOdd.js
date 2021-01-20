const reverseOdd = x => x.split(" ").map(w => w.length%2==0 ? 
	w : [...w].reverse().join("")).join(" ");