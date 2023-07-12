# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
        
		# empty hashmap for values coming before the current value.
		prev_map = {}	# value : index

		# The "enumerate()" function is used to retrieve both the index and the corresponding value of each element in the list.
		for i, n in enumerate(nums):	# i=index, n=value
			diff = target - n
			
			if diff in prev_map:
				return [prev_map[diff], i]

			# soltuion not found, update hashmap
			prev_map[n] = i
		
		# a solution is guaranteed in the problem statement, but still put return.
		return