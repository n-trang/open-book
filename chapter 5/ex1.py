def compare(a, b):
    """
      >>> compare(8, 4)
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 9)
      -1
      >>> compare(42, 1)
      1
      >>> compare('c', 'a')
      1
      >>> compare('p', 'p')
      0
    """
    result = 0
    if a > b: 
        result = 1
    elif a < b:
        result = -1
    return(result)



if __name__ == '__main__':
    import doctest
    doctest.testmod()