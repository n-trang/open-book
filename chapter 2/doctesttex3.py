"""
  >>> x + y
  42
  >>> type(message)
  <class 'str'>
  >>> len(message)
  13
"""
x = 40
y= 2
message = '0123456789111'

if __name__ == '__main__':
    import doctest
    doctest.testmod()