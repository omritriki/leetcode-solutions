"""
4. Median of Two Sorted Arrays
Difficulty: Hard

Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Binary Search on Partitions
        Time Complexity: O(log(min(m,n)))
        Space Complexity: O(1)
        
        Key Idea: Instead of merging arrays, find the correct partition that divides
        all elements into left and right halves, where all left elements <= all right elements.
        """
        
        # Ensure nums1 is the smaller array for efficiency
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        left, right = 0, m
        
        while left <= right:
            partition_x = (left + right) // 2  # How many elements from nums1 go left
            partition_y = (m + n + 1) // 2 - partition_x  # How many elements from nums2 go left
            
            # Left half boundaries
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            
            # Right half boundaries  
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            
            # Correct partition: all left elements <= all right elements
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1
        
        return 0.0 


# Test cases with detailed explanations
def test_find_median_sorted_arrays():
    solution = Solution()
    
    # Test case 1: nums1 = [1,3], nums2 = [2]
    nums1, nums2 = [1, 3], [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.0

    
    # Test case 2: nums1 = [1,2], nums2 = [3,4]
    nums1, nums2 = [1, 2], [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.5
    
    # Test case 3: Edge cases
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert solution.findMedianSortedArrays([], [1]) == 1.0
    assert solution.findMedianSortedArrays([2], []) == 2.0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_median_sorted_arrays()