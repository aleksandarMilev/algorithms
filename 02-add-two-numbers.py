class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums):
    """Helper to convert Python list → Linked list."""
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def print_list(node):
    """Helper to convert Linked list → Python list for printing."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
        
    print(result)


def solve(l1, l2):
    """
    02. Add Two Numbers
    -------------------
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each node contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:
        Input:  l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807
    """

    carry = 0
    dummy = ListNode()
    current = dummy

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10

        current.next = ListNode(total % 10)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


if __name__ == "__main__":
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    print_list(solve(l1, l2))  # Expected: [7, 0, 8]

    l1 = build_list([0])
    l2 = build_list([0])
    print_list(solve(l1, l2))  # Expected: [0]

    l1 = build_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_list([9, 9, 9, 9])
    print_list(solve(l1, l2))  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]
