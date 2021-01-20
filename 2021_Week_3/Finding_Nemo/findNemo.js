const findNemo = s => s.split(" ").indexOf("Nemo") != -1 
? `I found Nemo at ${1+s.split(" ").findIndex(x => x == "Nemo")}!` 
: "I can't find Nemo :(";