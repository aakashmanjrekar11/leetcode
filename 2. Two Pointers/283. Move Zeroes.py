class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		l = 0

		for r in range(len(nums)):	# r is at index 0 by default
			# if number at r is 0 then if statement is false, otherwise true for any non-zero number
			if nums[r]:
				nums[l], nums[r] = nums[r], nums[l]		# swap numbers at l and r
				l += 1		# increment pointer at l
		
		return nums
