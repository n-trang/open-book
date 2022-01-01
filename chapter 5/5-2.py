def lots_of_letters(word):
    """
      >>> lots_of_letters('Lidia')
      'Liidddiiiiaaaaa'
      >>> lots_of_letters('Python')
      'Pyyttthhhhooooonnnnnn'
      >>> lots_of_letters('')
      ''
      >>> lots_of_letters('1')
      '1'
    """
    new_word_list = []
    list_of_letter = enumerate(word)
    for set in list_of_letter:
        letter = set[1]
        number_of_times = set[0] +1
        new_word_list.append(letter*number_of_times)
    new_word = ''.join([str(ele) for ele in new_word_list])
    return (new_word)

def seperate_by_type(list_of_stuff):
    """
      >>> seperate_by_type([3, 'a', 4.2, None, (1, 2), 'b'])
      ([3, 4.2], ['a', (1, 2), 'b'], [None])
      >>> seperate_by_type([1, 3, 'xyz', 42, (0, 2), 'qwerty', [1, 0], 12])
      ([1, 3, 42, 12], ['xyz', (0, 2), 'qwerty', [1, 0]], [])
      >>> seperate_by_type([])
      ([], [], [])
    """
    list_of_numbers = []
    list_of_sequences = []
    list_of_other_types = []
    final_list = []
    for i in list_of_stuff:
        if type(i) == int or type(i) == float:
            list_of_numbers.append(i)
        elif type(i) == tuple or type(i) == str or type(i) == list:
            list_of_sequences.append(i)
        else:
            list_of_other_types.append(i)
    return list_of_numbers, list_of_sequences, list_of_other_types


def only_evens(numbers):
    """
    >>> only_evens([1, 3, 4, 6, 7, 8])
    [4, 6, 8]
    >>> only_evens([2, 4, 6, 8, 10, 11, 0])
    [2, 4, 6, 8, 10, 0]
    >>> only_evens([1, 3, 5, 7, 9, 11])
    []
    >>> only_evens([4, 0, -1, 2, 6, 7, -4])
    [4, 0, 2, 6, -4]
    >>> nums = [1, 2, 3, 4]
    >>> only_evens(nums)
    [2, 4]
    >>> nums
    [1, 2, 3, 4]
    """
    even_number = []
    for i in numbers:
        if i % 2 == 0:
            even_number.append(i)
        else:
            pass
    return even_number

import math
def gcf(m, n):
    """
      >>> gcf(10, 25)
      5
      >>> gcf(8, 12)
      4
      >>> gcf(5, 12)
      1
      >>> gcf(24, 12)
      12
    """
    return(math.gcd(m, n))

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()