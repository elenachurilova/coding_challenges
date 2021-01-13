# My commitment to solve 300 Leetcode challenges


# =============================== ! =============================== #

# 1662. Check If Two String Arrays are Equivalent

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false

def smallest_window_to_sort(array):

    results = set()

    for i in range(len(array)-2):
        if i == 0:
            if array[i] > array[i+1]:
                results.add(i)
        else:
            if array[i] < array[i - 1] or array[i] > array[i + 1]:
                results.add(i)

    return results

# =============================== ! =============================== #

# 1640. Check Array Formation Through Concatenation

# Input: arr = [85], pieces = [[85]]
# Output: true

# Input: arr = [15,88], pieces = [[88],[15]]
# Output: true
# Explanation: Concatenate [15] then [88]

# Input: arr = [49,18,16], pieces = [[16,18,49]]
# Output: false
# Explanation: Even though the numbers match, we cannot reorder pieces[0].

# Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# Output: true
# Explanation: Concatenate [91] then [4,64] then [78]

# Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
# Output: false

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        mapped = { piece[0] : piece for piece in pieces }
        result = []
            
        for item in arr:
            result += mapped.get(item, [])
                
        return result == arr







# =============================== ! =============================== #
# 2. Add Two Numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def addTwoNumbers(l1, l2) -> ListNode:
    
    first_list = []
    second_list = [] 
    
    current = l1
    while current is not None:
        first_list.append(current.val)
        current = current.next
        
    current = l2
    while current is not None:
        second_list.append(current.val)
        current = current.next
        
    str1 = ""
    str2 = ""
    
    for item in first_list:
        str1 += str(item)
    
    for item in second_list:
        str2 += str(item)
   
    summ = int(str1) + int(str2)
    result = [ int(i) for i in str(summ) ]
    # [8, 0, 7] 
        
    objs = [ListNode() for i in range(len(result))]
    #[ ListNode(), ListNode(), ListNode() ]
    
    for i in range(len(result)-1):
        if objs[i+1] is not None:
            objs[i].val = result[i]
            objs[i].next = objs[i+1]
    objs[-1].val = result[-1]
    objs[-1].next = None
            
    return objs[0]
        
        
l2 = ListNode()
l5 = ListNode()

l4 = ListNode()
l6 = ListNode()

l3 = ListNode()
l42 = ListNode()

l2.val = 2
l2.next = l4
l5.val = 5
l5.next = l6
l4.val = 4
l4.next = l3
l6.val = 6
l6.next = l42
l3.val = 3
l3.next = None
l42.val = 4
l42.next = None

addTwoNumbers(l2, l5)

# =============================== ! =============================== #
# =============================== ! =============================== #
# =============================== ! =============================== #
# =============================== ! =============================== #
# =============================== ! =============================== #
# =============================== ! =============================== #
# =============================== ! =============================== #
