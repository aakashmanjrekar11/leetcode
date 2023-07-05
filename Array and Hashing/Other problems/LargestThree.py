
def find_largest_3_elements(arr):
	# Remove duplicates from the original array
	unique_arr = []
	for num in arr:
		if num not in unique_arr:
			unique_arr.append(num)

	# Check if the unique-array has at least three distinct elements
	if len(unique_arr) < 3:
		print("Unique array does not have 3 distinct elements")
		return
	else:
		print(unique_arr)

	# Sort the unique-array in descending order using bubble sort
	n = len(unique_arr)
	for i in range(n - 1):
		for j in range(n - i - 1):
			if unique_arr[j] < unique_arr[j + 1]:
				print(unique_arr[j], unique_arr[j + 1])
				unique_arr[j], unique_arr[j + 1] = unique_arr[j + 1], unique_arr[j]
				print(unique_arr[j], unique_arr[j + 1])

	# Print the largest three distinct elements
	print(unique_arr)
	for i in range(3):
		print(unique_arr[i])


# Example usage
array = [10, 5, 20, 30, 30, 20, 40, 10, 50]
find_largest_3_elements(array)
