"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        max_length = 0
        seen_chars = set()

        while right < n:
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                seen_chars.remove(s[left])
                left += 1
        return max_length
    
    
# Test cases
def test_length_of_longest_substring():
    solution = Solution()
    
    # Test case 1: Regular string with repeating characters
    s1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(s1)
    print(f"Test 1: s='{s1}', result={result1}")
    assert result1 == 3
    
    # Test case 2: String with all same characters
    s2 = "bbbbb" 
    result2 = solution.lengthOfLongestSubstring(s2)
    print(f"Test 2: s='{s2}', result={result2}")
    assert result2 == 1
    
    # Test case 3: String with non-consecutive repeating characters
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    print(f"Test 3: s='{s3}', result={result3}")
    assert result3 == 3
    
    # Test case 4: Empty string
    s4 = ""
    result4 = solution.lengthOfLongestSubstring(s4)
    print(f"Test 4: s='{s4}', result={result4}")
    assert result4 == 0
    
    # Test case 5: Single character
    s5 = "a"
    result5 = solution.lengthOfLongestSubstring(s5)
    print(f"Test 5: s='{s5}', result={result5}")
    assert result5 == 1
    
    # Test case 6: String with spaces and special characters
    s6 = "Hello World!"
    result6 = solution.lengthOfLongestSubstring(s6)
    print(f"Test 6: s='{s6}', result={result6}")
    assert result6 == 7  # "World! "
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_longest_substring()
