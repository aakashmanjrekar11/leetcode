class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []		# empty list
        l, r = 0, len(nums) - 1		# l at start, r at end of the array

        while l <= r:
            # absolute disregards -ve sign and gives +ve value of number
			# so abs(-4) > abs(3) = 4 > 3 would be true
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l] * nums[l])
                l += 1
            else:
                result.append(nums[r] * nums[r])
                r -= 1
        
        return result[::-1]		# reverse the list