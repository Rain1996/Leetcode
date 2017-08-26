class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        new_list = []
        m_index = n_index = 0

        for i in range(m + n):
            if m_index == m:
                new_list += nums2[n_index:]
                break
            elif n_index == n:
                new_list += nums1[m_index:]
                break
            elif nums1[m_index] > nums2[n_index]:
                new_list.append(nums2[n_index])
                n_index += 1
            else:
                new_list.append(nums1[m_index])
                m_index += 1

        if ((m + n) % 2):
            return float(new_list[(m + n) / 2])
        else:
            return (new_list[(m + n) / 2 - 1] + new_list[(m + n) / 2]) / 2.0
