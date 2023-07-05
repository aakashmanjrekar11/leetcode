
#! 1. Iterative python program to reverse an array
# Time Complexity: O(n)
# Space Complexity: O(1)

# Function to reverse arr[] from start to end
def reverseArrayIterative(arr):
	start = 0
	end = len(arr) - 1
    
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6]
print(f"Original array is: {arr}")
reverseArrayIterative(arr)
print(f"Reversed array is: {arr}")


#! 2. Recursive python program to reverse an array
# Time Complexity: O(n)
# Space Complexity: O(n)

# Function to reverse arr[] from start to end
def reverseArrayRecursive(arr, start=0, end=0):
	if start == 0:
		start = 0
		end = len(arr) - 1
    
	if start >= end:
		return
	arr[start], arr[end] = arr[end], arr[start]
	reverseArrayRecursive(arr, start+1, end-1)


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print(f"Original array is: {arr}")
reverseArrayRecursive(arr)
print(f"Reversed array is: {arr}")
