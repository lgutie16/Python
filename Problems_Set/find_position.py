"""
You have been given an A array consisting of 
N integers. All the elements in this array are
guaranteed to be unique. For each position i
in the array A. You need to find the position  
A[i] should be present in, if the array was a 
sorted array. You need to find this for each 
i and print the resulting solution."""

def insertion_sort(arr, n):
	for i in range (0, n):
		temp = arr[i]
		j = i
		while temp<arr[j-1]  and j > 0:			
			arr[j] = arr[j-1]			
			j = j - 1 
		arr[j] = temp
	return arr


def ternary_seach(l, r, key, arr):
	mid = l + int((r-l)/3)
	mid2 = r - int((r-l)/3)

	if arr[mid] == key:
		return mid
	elif arr[mid2] == key:
		return mid2
	elif key < arr[mid]:
		return ternary_seach(l, mid-1, key, arr)
	elif key > arr[mid2]:
		return ternary_seach(mid2+1, r, key, arr)
	else:
		return ternary_seach(mid+1, mid2-1, key, arr)



def main():
	n = input()
	if 1 <= n <= 100:
		arr = [int(i) for i in raw_input().split()]
		arr2 = insertion_sort(arr, n)
	for i in xrange(0,n):
		print ternary_seach(0, n, arr2[i], arr2)
	
main()