import cmath
num = 1+2j
num_sqrt = cmath.sqrt(num)
print('the square root of {0} is {1:0.3f}+{2:0.3f}j'. format(num ,num_sqrt.real ,num_sqrt.imag))
