"""
Getting sign,mantise and exponent
"""
import math


def disect_float(f,b):
    f = float(f)  # fixes passing integers
    sign = '+'  # positive
    exp = 0
    mant = 0

    if f < 0:  # make f positive, store the sign
        sign = '-'  # negative

    f = abs(f)
    j = f
    if j > 0.5:
        for x in range(1072):  # exp is positive
            res, remainder = divmod(j, b)
            #print(res, remainder,x)
            exp += 1
            if res <= 0:
                break
            j = res
    else:
        for x in range(1072):  # exp is positive
            res = j * b
            exp -= 1
            #print(res,x)
            if res > 0.5:
                break
            j = res

    mant = f / pow(b, exp)
    return sign, mant, exp

print("=================================================================")
print('Sign:{0},Mantissa:{1},Exponent:{2}'.format(*disect_float(-0.31415, 2)))
print('The easy way: ' + str(math.frexp(-0.31415)))
print("=================================================================")

