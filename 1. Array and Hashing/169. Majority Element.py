
# Solution 1 - Boyer-Moore Algorithm (Optimal Solution)
# Time complexity: O(n), Space complexity: O(1)
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		result, count = 0, 0

		for n in nums:
			if count == 0:
				result = n

			count += (1 if n == result else -1)

		return result


# Solution 2 - Using hashmap
# Time and Space complexity: O(n)
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		count_map = {}  # hashmap to store count of all numbers
		result, max_count = 0, 0

		for n in nums:
			# increment count for each element
			count_map[n] = 1 + count_map.get(n, 0)
			
			# update majority element
			if count_map[n] > max_count:
				result = n
			
			# update max count
			max_count = max(max_count, count_map[n])

		return result
