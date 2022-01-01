for x in range(2, 21, 1):
    if x % 2 == 0 and x % 3  == 0 :
        isdevisable = 'both'
    if x % 2 == 0 and not x % 3 == 0:
        isdevisable = 'by 2'
    if x % 3 == 0 and not x % 2 == 0:
        isdevisable = "by 3"
    else:
        isdevisable = "neither"
    print(x, '\t', isdevisable)