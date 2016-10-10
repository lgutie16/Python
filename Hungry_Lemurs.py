#https://www.hackerearth.com/problem/algorithm/hungry-lemurs/
b = input("Number of bananas: ")
l = input("Number of lemurs: ")

ban = b - (int(b/l)*l)
if(ban == 0):
	print(0)
else:
	dif = int(l-ban)
	if(ban < dif/2):
		print ban
	else:
		if(dif%2==0):
			print(dif/2)
		else:
			print((dif/2)+1)