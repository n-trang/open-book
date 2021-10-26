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

def hypotenuse(a, b):
    """
      >>> hypotenuse(3, 4)
      5.0
      >>> hypotenuse(12, 5)
      13.0
      >>> hypotenuse(7, 24)
      25.0
      >>> hypotenuse(9, 12)
      15.0
    """
    cbinh = a**2 + b**2
    c =  sqrt(cbinh) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()