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






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
