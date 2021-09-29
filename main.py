import math
from itertools import combinations

testData = [
    [14,6,7,7,15,13,7,6],
    [13,14,13,8,15,11,4,8],
    [14,6,12,15,7,6,10,14],
    [15,9,7,10,9,12,15,14],
    [15,4,10,8,11,8,4,14],
    [14,9,15,7,9,7,7,10],
    [4,14,12,11,11,12,9,14],
    [14,9,11,10,7,10,7,6],
    [5,14,10,8,5,7,15,14],
    [7,12,11,12,12,11,12,15]
]

NLS = []

class neuron:
    def __init__(self,ins):
        self.ins = list(ins)
        self.inWeights = [0.5] * len(list(ins))
    def printIns(self):
        print(self.ins)
        print(self.inWeights)

def normalize(listIn):
    out = []
    low = min(listIn)
    high = max(listIn)
    mid = (low + high)/2
    spread = high - mid
    for n in listIn:
        if n > mid:
            out.append(math.atan(math.tan(1) * ((n-spread) / mid)))
        else:
            out.append(math.atan(-math.tan(1) * (spread - n + low)/spread))
    return out

def aggr(line,last,binomial):
    combs = list(combinations(line,2))
    for x in range(binomial):
        last[x] = last[x] + (abs(combs[x][0]) * abs(combs[x][1]))
    return last

def combReverse(pos,len):
    pos = pos + 1
    if pos > math.comb(len,2):
        raise ValueError
    count = 0
    while pos > 0:
        count = count + 1
        pos = pos - (len - count)
    return count-1, (pos + (len - count) + count - 1)


def neuronBuilder(dataIn,dataOut):
    width = len(dataIn[0])
    binomial = math.comb(width,2)
    combM = [0] * binomial
    n = [normalize(list(x)) for x in zip(*dataIn)]
    n1 = [list(x) for x in zip(*n)]
    for x in range(len(n1)):
        combM = aggr(n1[x],combM,binomial)
    combM1 = sorted(combM)[(math.floor(binomial/2)):]
    combM2 = [combM.index(x) for x in combM1]
    combM3 = [combReverse(x,width) for x in combM2]
    print(combM)
    print(combM1)
    print(combM2)
    print(combM3)

neuronBuilder(testData,[])
tn = neuron((1,7))
tn.printIns()