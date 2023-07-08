def max_subarray_sum(arr, window_size):
    left = 0
    right = window_size - 1

    # Calculate the initial sum
    # slicing is inclusive of 'left' index and exclusive of the 'right+1' index
    max_sum = sum(arr[left:right + 1])
    current_sum = max_sum

    # Slide the window
    while right < len(arr) - 1:
        # Move the window one position to the right
        left += 1
        right += 1

        # Update the current sum
        # current_sum = 7 - 2 + 5 = 10
        current_sum = current_sum - arr[left - 1] + arr[right]

        # Update the maximum sum if necessary
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage
arr = [2, 4, 1, 5, 3, 7, 2, 8]
arr1 = [1, 2, 5, 2, 8, 1, 5]

window_size = 3

max_sum = max_subarray_sum(arr, window_size)
max_sum1 = max_subarray_sum(arr1, window_size)

print("Maximum sum of subarray of size", window_size, ":", max_sum)
print("Maximum sum of subarray of size", window_size, ":", max_sum1)
