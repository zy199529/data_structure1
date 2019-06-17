# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        l = 1
        prev = None #开辟新的一条链表
        p = head
        while p:
            if l<m:#判断是否到达逆序的位置
                q = p 
                p = p.next
                l = l+1
                continue
            while l<=n and l>=m:# 达到逆序的位置
                h = p.next 
                p.next = prev #这两条逆序
                prev = p
                h = p
                print(p.val)
                l = l+1
            break
            #加下来拼接
        return prev

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            line = next(lines)
            m = int(line);
            line = next(lines)
            n = int(line);
            
            ret = Solution().reverseBetween(head, m, n)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()