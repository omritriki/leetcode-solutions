"""
2. Add Two Numbers
Difficulty: Medium

Problem:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Elementary Math
        Time Complexity: O(max(M, N)) where M and N are the lengths of l1 and l2
        Space Complexity: O(max(M, N)) for the result linked list
        
        We traverse both linked lists simultaneously, adding corresponding digits
        and handling carry. We continue until both lists are exhausted and
        there's no remaining carry.
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            total = val1 + val2 + carry
            carry = total // 10 
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        if carry > 0:   
            current.next = ListNode(carry)

        return dummy_head.next

# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert a linked list to a Python list"""
    result = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result

# Test cases
def test_add_two_numbers():
    solution = Solution()
    
    # Test case 1: 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    expected = [7, 0, 8]
    actual = linked_list_to_list(result)
    print(f"Test 1: {linked_list_to_list(l1)} + {linked_list_to_list(l2)} = {actual}")
    assert actual == expected
    
    # Test case 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    expected = [0]
    actual = linked_list_to_list(result)
    print(f"Test 2: {linked_list_to_list(l1)} + {linked_list_to_list(l2)} = {actual}")
    assert actual == expected
    
    # Test case 3: 9999999 + 9999 = 10009998
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    expected = [8, 9, 9, 9, 0, 0, 0, 1]
    actual = linked_list_to_list(result)
    print(f"Test 3: {linked_list_to_list(l1)} + {linked_list_to_list(l2)} = {actual}")
    assert actual == expected
    
    # Test case 4: Different lengths
    l1 = create_linked_list([1, 2, 3])
    l2 = create_linked_list([4, 5])
    result = solution.addTwoNumbers(l1, l2)
    expected = [5, 7, 3]
    actual = linked_list_to_list(result)
    print(f"Test 4: {linked_list_to_list(l1)} + {linked_list_to_list(l2)} = {actual}")
    assert actual == expected
    
    # Test case 5: Single digit with carry
    l1 = create_linked_list([5])
    l2 = create_linked_list([5])
    result = solution.addTwoNumbers(l1, l2)
    expected = [0, 1]
    actual = linked_list_to_list(result)
    print(f"Test 5: {linked_list_to_list(l1)} + {linked_list_to_list(l2)} = {actual}")
    assert actual == expected
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_add_two_numbers()
    
    
