
# The solution has a time complexity of O(n), where n is the length of the input strings. This is because the solution iterates over the characters of both strings once to count their occurrences and then compares the counts.

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
        
		# check if length of both strings is same or not
		if len(s) != len(t):
			return False
		
		# initialize empty hashmaps for each strings
		count_S, count_T = {}, {}

		# build the hashmaps
		# For each character at index i, it increments the count for that character in the respective dictionary using count_S.get(s[i], 0) and count_T.get(t[i], 0). The get method returns the count of the character if it exists in the dictionary or 0 if it doesn't.
		for i in range(len(s)):
			count_S[s[i]] = 1 + count_S.get(s[i], 0)
			count_T[t[i]] = 1 + count_T.get(t[i], 0)
		
		# iterate through both hashmaps and check if count for each key is same
        # current_char is the index for keys in the hashmap
		for current_char in count_S:
			if count_S[current_char] != count_T.get(current_char, 0):
				return False
		
		# otherwise, both hashmaps are same, t is anagram of s
		return True