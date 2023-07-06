class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
        
		# check if length of both strings is same or not
		if len(s) != len(t):
			return False
		
		# initialize empty hashmaps for each strings
		countS, countT = {}, {}

		# build the hashmaps
		for i in range(len(s)):
			countS[s[i]] = 1 + countS.get(s[i], 0)
			countT[t[i]] = 1 + countT.get(t[i], 0)
		
		# iterate through both hashmaps and check if count for each key is same
        # c is the key for the character in the hashmap
		for c in countS:
			if countS[c] != countT.get(c, 0):
				return False
		
		# otherwise, both hashmaps are same, t is anagram of s
		return True