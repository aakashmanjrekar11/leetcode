def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


# Example usage
arr = [1, 2, 4, 6, 9]
target = 8
result = two_sum(arr, target)
print(result)
