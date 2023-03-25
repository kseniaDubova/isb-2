NUM = "00011101110111100010101000010101000110010011011001010101110000010110100110101000101111011110000001001100101101101010011111111001"
import math
import numpy as np
def first_test(lnum: list)->float:
    sum = 0
    for i in lnum:
        if i == 0:
            sum += -1
        else: sum += 1
    print(math.erfc((sum/math.sqrt(128))/math.sqrt(2)))

def second_test(lnum: list)->float:
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
    print(math.erfc((math.fabs(v-2*128*sum*(1-sum)))/(2*math.sqrt(2*128)*sum*(1-sum))))
    
def third_test(lnum: list):
    splits = np.array_split(lnum, 16)
    """
    for i in splits:
        print(i)
    
    [0 0 0 1 1 1 0 1] 3
    [1 1 0 1 1 1 1 0] 4
    [0 0 1 0 1 0 1 0] 1
    [0 0 0 1 0 1 0 1] 1
    [0 0 0 1 1 0 0 1] 2
    [0 0 1 1 0 1 1 0] 2
    [0 1 0 1 0 1 0 1] 1
    [1 1 0 0 0 0 0 1] 2
    [0 1 1 0 1 0 0 1] 2
    [1 0 1 0 1 0 0 0] 1
    [1 0 1 1 1 1 0 1] 4
    [1 1 1 0 0 0 0 0] 3
    [0 1 0 0 1 1 0 0] 2
    [1 0 1 1 0 1 1 0] 2
    [1 0 1 0 0 1 1 1] 3
    [1 1 1 1 1 0 0 1] 5
    """
    v = [4,6,3,3]
    '''
    v1 = (4) # <= 1
    v2 = (6) #  = 2
    v3 = (3) #  = 3
    v4 = (3) # >= 4
    '''
    p = [0.2148, 0.3672, 0.2305, 0.1875]
    xx = 0
    i = 0
    while not i == 4:
        xx+=((v[i] - 16*p[i])*(v[i] - 16*p[i]))/(16*p[i])
        i +=1
    print(xx)
    #xx = 0.2232915342847958

lnum =[]
for i in NUM:
    lnum.append(int(i))
first_test(lnum)
#0.8596837951986662
second_test(lnum)
#0.3751531318048568
third_test(lnum)
#p = 0.97362493
