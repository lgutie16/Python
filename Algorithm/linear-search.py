def linear_search(x,y):
	n = len( x )
	iaux = 0
	position = 0
	for i in x:
		if i == y:
			position = iaux
		iaux = iaux + 1	
	return position

def main():	
  arr = [int(i) for i in raw_input().split()]
  trgt =int( input())
  print linear_search(arr, trgt)

main()