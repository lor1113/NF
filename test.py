import math

def combReverse(pos,len):
    pos = pos + 1
    if pos > math.comb(len,2):
        raise ValueError
    count = 0
    while pos > 0:
        count = count + 1
        pos = pos - (len - count)
    return count-1, (pos + (len - count) + count - 1)

print(combReverse(10,8))