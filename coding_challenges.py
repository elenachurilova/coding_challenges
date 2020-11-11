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


def checkMagazine(magazine, note):
    """
    >>> checkMagazine(["give", "me", "one", "grand", "today", "night"], ["give", "one", "grand", "today"])
    Yes

    """

    answer = ''
    dictionary = {}

    for word in magazine:

        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    for word in note:

        if word in dictionary:
            if dictionary[word] > 0:
                dictionary[word] -= 1
                answer = "Yes"
            else:
                answer = "No"
                break
        else:
            answer = "No"
            break

    print(answer)


# * # * # * Class implementation * # * # * #

class Door:

    def __init__(self, height, color, is_locked):
        self.height = height
        self.color = color
        self.is_locked = is_locked

    def __repr__(self):
        return f'<Door of {self.color} color, {self.height} inches high>'

    def open_it(self):
        
        if self.is_locked == True:
            print("The door must be unlocked first")
            self.open = False
        else:
            print("The door is open now...")
            self.open = True

    def close_it(self):
        pass

    def toggle_lock(self):
        if self.is_locked == False:
            self.is_locked = True
            print("Success! The door is locked now")
        else:
            self.is_locked = False
            print("Careful! The door is unlocked now")


def howMany(sentence):
    """Given a sentense made up of groups of words determine the number of words

    Each word is a sequence of letters (a-z, A-Z) that may contain one or more hyphens and may
    end in a punctuation mark: period, comma, question mark or exclamation point. Words will be separated
    by one or more white space characters, hyphens join two words into one and should be retained while the other
    punctuation marks should be stripped. 

    >>> howMany("How many eggs are in half-dozen, 13?")
    6

    """
    s=sentence
    list_of_words = s.split()
    result = []
    
    for word in list_of_words:
        # if word contains not only alphabetical chars
        if not word.isalpha():
            # if 1st-thru-second-to-last-chars are all letters
            if word[0:-1].isalpha():
                # if the last item is an allowed punctuation mark
                if word[-1] in "!?.,":
                    # keep the word
                    result.append(word)
            elif "-" in word:
                # if characters wrapping the "-" are all alphabetical and/or the last char is an allowed punctuation mark
                if word[0:(word.index("-"))].isalpha() and word[(word.index("-"))+1:].isalpha() or word[0:(word.index("-"))].isalpha() and word[(word.index("-"))+1:-1].isalpha() and word[-1] in "!?.,":
                    result.append(word)
            else:
                continue
        else:
            result.append(word)
                             
    return len(result)

def nums_to_target(candidates, target):
    # [2, 3, 5], target = 8
    # result = [ [2, 2, 2, 2], [2, 3, 3], [3, 5]]

    result = []

    for candidate in candidates:
        if target % candidate == 0:
            coeff = int(target / candidate)
            temp = [candidate] * coeff
            result.append(temp)

    start = candidates[0]
    for num in range(1, len(candidates)):
        if start + candidates[num] == target:
            result.append([start, candidates[num]])
            start = candidates[candidates.index(start)+1]

##################################

class Employee():
    """A node in a graph representing a restaurant"""

    def __init__(self, position, connections=None):

        if connections is None:
            connections = set()

        self.position = position
        self.connections = connections

    def __repr__(self):
        return f"<Employee node {self.position}>"

    def add_connection(self, connection):
        self.connections.add(connection)


class Restaurant():
    """A graph holding employees and their connections in the restaurant flow"""

    def __init__(self):
        """Create an empty graph"""
        self.employees = set()

    def __repr__(self):
        """Print instance for easy debugging"""
        return f"<Restaurant graph: {employee for employee in self.employees}>"

    def add_person(self, person):
        """Add a new instance to the graph"""
        self.employees.add(person)

    def set_connection(self, employee1, employee2):
        """Set new connection between two employees"""
        employee1.add_connection(employee2)
        employee2.add_connection(employee1)
        
    def add_employees(self, employees_list):
        """Add employees to the restaurant"""
        for person in employees_list:
            self.add_person(person)

    def are_connected(self, employee1, employee2):
        """Are two employees connected? BFS"""

        seen = set()
        queue = []
        queue.append(employee1)
        seen.add(employee1)
       
        while queue:
            current_employee = queue.pop(0)
            print("checking ", current_employee)
            
            if current_employee is employee2:
                return True
            else:
                for person in current_employee.connections - seen:
                    queue.append(person)
                    seen.add(person)
                    print("added to queue: ", person)
        return False

    def are_connected_recursively(self, employee1, employee2, seen=None):
        """Are two employees connected? DFS using recursion"""

        if not seen:
            seen = set()

        # base case
        if employee1 is employee2:
            return True

        seen.add(employee1)
        print("adding", employee1)

        for employee in employee1.connections:

            if employee not in seen:

                if self.are_connected_recursively(employee, employee2, seen):
                    return True

        return False


    def shortest_path(self, employee1, employee2):
        """Calculate distance (minimal distance) between two employees in a restaurant"""

        seen = []
        queue = [[employee1]]

        if employee1 == employee2:
            print("That was easy!")
            return 0
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in seen:
                connections = node.connections

                for connection in connections:
                    new_path = list(path)
                    new_path.append(connection)
                    queue.append(new_path)

                    if connection == employee2:
                        print(f"Shortest path is: {new_path}")
                        return (len(new_path)-1)
                
                seen.append(node)

        return "Two employees are independent. The connection doesn't exist"




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


    hostess = Employee("hostess")
    waiter = Employee("waiter")
    chef = Employee("chef")
    bus_boy = Employee("bus_boy")
    hostess.add_connection(waiter)
    waiter.add_connection(bus_boy)
    waiter.add_connection(chef)
    chef.add_connection(waiter)
    bus_boy.add_connection(chef)
    sapore = Restaurant()
    sapore.add_employees([hostess, waiter, chef, bus_boy])