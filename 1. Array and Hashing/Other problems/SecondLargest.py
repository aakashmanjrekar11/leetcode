
def find_second_largest(arr):
    # Check if the array has at least two elements
	if len(arr) < 2:
		print("Array does not have a second-largest number.")
		return
	
	# Initialise largest, second_largest variables as -inf
	largest = float('-inf')
	second_largest = float('-inf')

	# Find the largest and second-largest elements
	for num in arr:
		if num > largest:
			second_largest = largest
			largest = num
		elif num > second_largest and num != largest:
			num = second_largest

	if second_largest == float('-inf'):
		print("There is no second-largest element.")
	else:
		print("Second largest number is: ", second_largest)

# Example usage
array = [10, 5, 20, 30, 30, 20, 40, 10, 50]
find_second_largest(array)