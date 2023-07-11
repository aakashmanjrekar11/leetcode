from typing import List

# Solution
class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		
		# Initialise an empty set
		hashset = set()

		for number in nums:
			# Duplicate found
			if number in hashset:
				return True
			# add the unique number to hashset
			else:
				hashset.add(number)
		
		# No duplicates found
		return False