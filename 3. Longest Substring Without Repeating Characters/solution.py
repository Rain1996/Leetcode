class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        char_to_index = {}
        start = 0

        for last in range(0, len(s)):
            if s[last] in char_to_index:
                index = char_to_index[s[last]]
                if index >= start:
                    result = max(last - start, result)
                    start = index + 1
            char_to_index[s[last]] = last

        return max(result, len(s) - start)
