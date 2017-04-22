#O(logn)
def ternary_search(l, r, key, arr):
	if r>=l:
		mid =  l+int((r-l)/3)
		mid2 = r-int((r-l)/3)
		if key == arr[mid]:
			return mid
		elif key == arr[mid2]:
			return mid2
		elif key < arr[mid]:
			return ternary_search(l, mid-1,key, arr)
		elif key > arr[mid2]:
			return ternary_search(mid2+1, r, key, arr)
		else:
			return ternary_search(mid+1, mid2-1, key, arr)	
	return -1

def main():	
  arr = [int(i) for i in raw_input().split()]
  trgt =int( input())
  print ternary_search(0,len(arr), trgt, arr)

main()
