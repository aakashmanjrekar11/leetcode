from typing import List

# Solution
class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		
		# Initialise an empty set
		hashset = set()

		for number in nums:
			if number in hashset:
				# Duplicate found
				return True

			# add the unique number to hashset
			hashset.add(number)
		
		# No duplicates found
		return False