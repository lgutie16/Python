#O(nlogn)
arr = []
def binary_search(low, high, key):
	if low<=high:
		mid=int((low+high)/2)
		if key == arr[mid]:
			return mid
		elif key < arr[mid]:
			high = mid-1
		else:
			low = mid+1
		return binary_search(low, high, key)	
	return -1

def main():	
  arr = [int(i) for i in raw_input().split()]
  trgt =int( input())
  print binary_search(0, len(arr), trgt)

main()


