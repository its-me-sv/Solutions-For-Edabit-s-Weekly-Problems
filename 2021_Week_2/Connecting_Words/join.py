def longestCommon(prevStr, currStr):
	maxLen = j = 0
	for i in range(len(prevStr)):
		if prevStr[i] == currStr[j]:
			j += 1
		else:
			maxLen = j if j > maxLen else maxLen
			j = 0
			if prevStr[i] == currStr[j]:
				j += 1
	return j if j > maxLen else maxLen

def join(lst):
	ans = lst[0]
	minLen = 10000
	for i in range(1,len(lst)):
		length = longestCommon(lst[i-1],lst[i])
		ans += lst[i][length:]
		minLen = minLen if minLen < length else length
	return [ans, minLen]