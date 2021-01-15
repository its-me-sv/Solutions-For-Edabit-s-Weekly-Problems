const howUnlucky = y => [0,1,2,3,4,5,6,7,8,9,10,11]
							.filter(m => new Date(y,m,13).getDay() == 5).length;