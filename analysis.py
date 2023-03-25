NUM = "00011101110111100010101000010101000110010011011001010101110000010110100110101000101111011110000001001100101101101010011111111001"
import math

def first_test(lnum: list)->float:
    sum = 0
    for i in lnum:
        if i == 0:
            sum += -1
        else: sum += 1
    return math.erfc((sum/math.sqrt(128))/math.sqrt(2))

def second_test(lnum: list):
    sum = 0
    for i in lnum:
        sum += i
    sum = sum/128
    if not math.fabs(sum - 0.5)<2/math.sqrt(2):
        return 0
    v = 0
    count = 0
    while count<len(lnum)-1:
        if not lnum[count] == lnum[count+1]:
            v += 1
        count +=1
    print(v)
    print(math.erfc((math.fabs(v-2*128*sum*(1-sum)))/(2*math.sqrt(2*128)*sum*(1-sum))))
        
#print(first_test())
lnum =[]
for i in NUM:
    lnum.append(int(i))
second_test(lnum)