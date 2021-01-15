from datetime import datetime
def how_unlucky(y):
	return len(list(filter(lambda x: datetime(y,x,13).strftime("%w") == "5",range(1, 13))))