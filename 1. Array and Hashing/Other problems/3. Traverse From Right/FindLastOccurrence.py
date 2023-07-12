def find_last_occurrence(arr, target):
    right = len(arr) - 1

    while right >= 0:
        if arr[right] == target:
            return right
        right -= 1

    return False


# Example usage
arr = [1, 2, 3, 4, 2, 6, 2]
target = 4
result = find_last_occurrence(arr, target)
print(f"Target = {target} | Location = {result}")
