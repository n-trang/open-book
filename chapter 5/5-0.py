def count_digits(digit, number):
    """
      >>> count_digits(5, 1055030250)
      3
      >>> count_digits(9, 909)
      2
      >>> count_digits(7, 7777)
      4
      >>> count_digits(7, 1234)
      0
    """
    string_number = str(number)
    string_digit = str(digit)
    count = 0
    for i in string_number:
        if i == string_digit:
            count += 1
    return count


def sum(a):
    """
    >>> sum([5, 10, -15.5, 20])
    19.5
    >>> sum((1, 1, 1, 1))
    4
    """
    total = 0
    for i in a:
        total = total + i
    return total


def find_average(numbers):
    """
      >>> find_average([5, 10])
      7.5
      >>> find_average([5, 10, 15])
      10.0
      >>> find_average((1, 2, 2, 3))
      2.0
      >>> find_average([19])
      19.0
    """
    amount = 0
    total = 0
    for i in numbers:
        amount += 1
        total = total + i
    return total / amount
def only_evens(nums):
    """
      >>> only_evens([3, 8, 5, 4, 12, 7, 2])
      [8, 4, 12, 2]
      >>> my_nums = [4, 7, 19, 22, 42]
      >>> only_evens(my_nums)
      [4, 22, 42]
      >>> my_nums
      [4, 7, 19, 22, 42]
    """
    even_list = []
    for i in nums:
        if (i % 2) == 0:
            even_list.append(i)
    return even_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()
