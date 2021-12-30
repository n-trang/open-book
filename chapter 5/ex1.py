import math
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
    c = math.sqrt(a**2 + b**2) 
    return c

def slope(x1, y1, x2, y2):
    """
      >>> slope(5, 3, 4, 2)
      1.0
      >>> slope(1, 2, 3, 2)
      0.0
      >>> slope(1, 2, 3, 3)
      0.5
      >>> slope(2, 4, 1, 2)
      2.0
    """
    slope = (y2 - y1) / (x2 - x1)
    return slope

def intercept(x1, y1, x2, y2):
    """
      >>> intercept(1, 6, 3, 12)
      3.0
      >>> intercept(6, 1, 1, 6)
      7.0
      >>> intercept(4, 6, 12, 8)
      5.0
    """
    intercept = y2 - slope(x1, y1, x2, y2) * x2
    return intercept

def is_factor(f, n):
    """
      >>> is_factor(3, 12)
      True
      >>> is_factor(5, 12)
      False
      >>> is_factor(7, 14)
      True
      >>> is_factor(2, 14)
      True
      >>> is_factor(7, 15)
      False
    """
    answer = (n%f) == 0
    return answer

def is_multiple(m, n):
    """
      >>> is_multiple(12, 3)
      True
      >>> is_multiple(12, 4)
      True
      >>> is_multiple(12, 5)
      False
      >>> is_multiple(12, 6)
      True
      >>> is_multiple(12, 7)
      False
    """
    return is_factor(n, m)

def f2c(t):
    """
      >>> f2c(212)
      100
      >>> f2c(32)
      0
      >>> f2c(-40)
      -40
      >>> f2c(36)
      2
      >>> f2c(37)
      3
      >>> f2c(38)
      3
      >>> f2c(39)
      4
    """
    c = round(5/9*(t-32))
    return c
def num_digits(n):
    """
      >>> num_digits(12345)
      5
      >>> num_digits(0)
      1
      >>> num_digits(-12345)
      5
    """
    string_degit = str(n)
    number_of_digits = 0
    for i in string_degit:
        if i == "-":
            pass
        else:
            number_of_digits += 1
    return number_of_digits

def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
if __name__ == '__main__':
    import doctest
    doctest.testmod()