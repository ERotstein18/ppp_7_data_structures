#Use a single operation (no loops) to multiply every element of an array by 3.
#For example, if we had an array of [1,6,3], the output would be [3,18,9].

import numpy as np
a = np.array([1, 2, 3, 4])

def multiply_by(array, multiplier):
    print(np.multiply(array, multiplier))


multiply_by(a, 3)
