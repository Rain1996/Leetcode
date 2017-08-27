class Solution(object):
    """
    用字典来存储字符-索引对,
    再根据设置的 起点 以及 字典中的索引 
    判断是否已经有重复字符以此来截取不重复子串
    """
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
