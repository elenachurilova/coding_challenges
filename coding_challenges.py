"""A collection of solved coding challenges"""

def is_palindrome(string):
    """Return True if a given string is a palindrome

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("snellens")
    True

    >>> is_palindrome("mother")
    False
    """

    result = None
    length = len(string)
    middle = int(length/2)

    if length % 2 != 0:
        
        for i in range(1, middle+1):

            if string[(middle-i)] == string[(middle+i)]:
                result = True
                continue
            else:
                result = False
                break
    
    else:

        prev = middle - 1

        for i in range(0, middle):

            if string[(middle+i)] == string[(prev-i)]:
                result = True
                continue
            else:
                result = False
                break

    return result


def repeatedString(s, n):
    """Given sample string S and number N return count of 'a' chars 
    in N first characters in an infinitely repeated S string
    
    >>> repeatedString("aba", 10)
    7

    >>> repeatedString("ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt", 685118368975)
    41107102139

    >>> repeatedString("a", 1000000000000)
    1000000000000
    
    """

    length = len(s) 
    coeff = int(round(n / length, 0)) 
    bigger_string = coeff * length 
    difference = bigger_string - n 
    tail = s[0:(-difference)]
    
    count_in_final = tail.count('a') + ( s.count('a') * int(n / length) )    

    return count_in_final



def hourglassSum(arr):
    """Given a 6x6 2D array of numbers (a list with 6 sublists of 6 integers each) 
    print out the max sum of an hourglass shape.

    An hourglass in an array is a subset of values with indices falling in the following pattern of graphical representation:

    a b c
      d
    e f g 

    >>> hourglassSum([ [-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],  [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0 ] ])
    28
    """

    sum = []

    for i in range(0, 4): 

        for j in range(0, 4): 

            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            sum.append(total)

    print(max(sum))


def rotLeft(a, d):
    """Given an array of integers A and an integer D, perform D left rotations on A and return the result.

    Result should be returned as space-separated characters in one line

    >>> rotLeft( [1, 2, 3, 4, 5], 4)
    '5 1 2 3 4'

    >>> rotLeft( [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10)
    '77 97 58 1 86 58 26 10 86 51 41 73 89 7 10 1 59 58 84 77'

    """

    for i in range(0, d):
        a.append(a.pop(0))
    
    new_a = []
    for char in a:
        new_a.append(str(char))

    return " ".join(new_a)
        

def count(string):
    """Given a string, return a dictionary with keys as characters and values as count of characters
    in the given string (int)

    >>> count('aba')
    {'a': 2, 'b': 1}

    >>> count("")
    {}
    """

    letters_count = {}
    
    if string == "":
        return {}
    else:
        for char in string:
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1
                
    return letters_count


def pig_it(text):
    """Given a string move the first letter of each word to the end of it, 
    then add "ay" to the end of the word. Leave punctuation marks untouched.

    >>> pig_it('Quis custodiet ipsos custodes ?')
    'uisQay ustodietcay psosiay ustodescay ?'
    """
    
    original_words = text.split()
    pig_words = []
    
    for word in original_words:
        
        if word in '!@#$%^&*()?.,':
            pig_words.append(word)
        else:
            first_letter = word[0]
            sliced = word[1:]
            
            new_word = sliced + first_letter + 'ay'
            pig_words.append(new_word)

    pig_phrase = " ".join(pig_words)
    return pig_phrase


def pick_peaks(arr):
    """Given an array of integers, return the positions and the values of the 
    "peaks" (or local maxima) in the following format {pos: [], peaks: []}

    >>> pick_peaks([1,2,3,6,4,1,2,3,2,1])
    {'pos': [3, 7], 'peaks': [6, 3]}

    >>> pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])
    {'pos': [2, 7, 14, 20], 'peaks': [5, 6, 5, 5]}
    """
    
    result = {"pos": [], "peaks": []}
    
    for i in range(1, len(arr)-1):
        
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            
            result["pos"].append(i)
            result["peaks"].append(arr[i])
            
        elif arr[i] > arr[i-1] and arr[i] >= arr[i+1]:
                
                for j in range(i, len(arr)):
                    
                    if arr[i] != arr[j]:
                        if arr[i] < arr[j]:
                            break
                        elif arr[i] > arr[j]:
                            result["pos"].append(i)
                            result["peaks"].append(arr[i])
                            break 
                        
    return result



        
# * # * # * Linked list implementation * # * # * #

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return(f'Node {self.data}')

class LinkedList:
    def __init__(self, nodes=None):
        """Initiate a LinkedList object"""
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        """Pretty print an instance"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """Traverse over the instance"""
        node = self.head
        while node.next is not None:
            yield node
            node = node.next

    def add_beginning(self, node):
        """Add a new Node to the beginning of the LinkedList"""
        node.next = self.head
        self.head = node

    def add_end(self, node):
        """Add a new Node to the end of the LinkedList"""
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next.next = node
        
            
def to_camel_case(text):
    """Given a string convert it to camel case.
    
    The first word within the output should be capitalized only if the original word was capitalized 
    (known as Upper Camel Case or Pascal case)

    >>> to_camel_case('the_stealth_warrior') 
    'theStealthWarrior'

    >>> to_camel_case('The-Stealth-Warrior') 
    'TheStealthWarrior'

    >>> to_camel_case('A-B-C')
    'ABC'

    """
    new_string = []
    
    for i in range(0, len(text)):
        
        if text[i] == "-" or text[i] == "_":
            continue
        elif i > 0 and text[i-1] == "-" or text[i-1] == "_":
            new_string.append(text[i].upper())
        else:
            new_string.append(text[i])
        
    return "".join(new_string)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')

    llist = LinkedList()
    node1 = Node("orange")
    node2 = Node("banana")
    node3 = Node("grape")
    node4 = Node("strawberry")
    llist.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4


