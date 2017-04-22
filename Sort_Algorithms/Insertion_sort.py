def insertion_sort(arr, n):
	for i in range (0, n):
		temp = arr[i]
		j = i
		while temp<arr[j-1]  and j > 0:			
			arr[j] = arr[j-1]			
			j = j - 1 
		arr[j] = temp

	for x in xrange(0, n):
		print arr[x]


def main():
	arr = [int(i) for i in raw_input().split()]
	n = len(arr)
	insertion_sort(arr, n)

main()

