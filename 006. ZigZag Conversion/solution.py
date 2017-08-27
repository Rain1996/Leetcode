# -*- coding: utf-8 -*-


class Solution(object):
    """
    找规律
    """

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= numRows or numRows == 1:
            return s
        result = ''
        step = (numRows + numRows - 2)
        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                index = row
                while index < length:
                    result += s[index]
                    index += step
            else:
                index = row
                while index < length:
                    result += s[index]
                    next_step = (numRows - 1 - row) * 2
                    if index + next_step < length:
                        result += s[index + next_step]
                    index += step
        return result
