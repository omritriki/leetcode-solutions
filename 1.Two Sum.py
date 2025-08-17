"""
1. Two Sum
Difficulty: Easy

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []  

# Test cases
def test_two_sum():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}, result={result1}")
    assert sorted(result1) == [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2}, result={result2}")
    assert sorted(result2) == [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3}, result={result3}")
    assert sorted(result3) == [0, 1]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()
