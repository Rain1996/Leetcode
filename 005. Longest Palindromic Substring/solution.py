class Solution(object):
    """
    回文有两种情况：
    'aba'
    'abba'
    然后从中心出发，此题可解，时间复杂度O(n ^ 2)
    最长回文子串还有个O(n)解法...
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = -1
        length = len(s)
        result = ""

        for index in range(length):
            left = index - 1
            right = index + 1

            while left > -1 and s[left] == s[index]:
                left -= 1

            while right < length and s[right] == s[index]:
                right += 1

            while left > -1 and right < length:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            temp = s[left + 1: right]
            result = temp if len(temp) > len(result) else result
        return result
