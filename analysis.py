NUM = "00011101110111100010101000010101000110010011011001010101110000010110100110101000101111011110000001001100101101101010011111111001"
import math

def first_test():
    sum = 0
    for i in NUM:
        if i == "0":
            sum += -1
        else: sum += 1
    return math.erfc((sum/math.sqrt(128))/math.sqrt(2))

print(first_test())