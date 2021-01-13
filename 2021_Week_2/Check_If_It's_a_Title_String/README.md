# JavaScript Solution
![JavaScript Question](JavaScript.PNG)
```javascript
const checkTitle = title => title.split(" ").every(word => word[0] == word[0].toUpperCase());
```
# Python Solution
![Python Question](Python.PNG)
```python
def check_title(txt):
	return all(map((lambda x : x[0].isupper()), txt.split()))
```
