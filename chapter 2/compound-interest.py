p = 100
n = 12
r = 0.08
t = int(input('how many years? '))
a = p * (1 + r/n) ** (n*t)
print('the final amount is', a)