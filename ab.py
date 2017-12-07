from math import ceil

def createString(N, K):
    """Create strings of length N with exactly K AB pairs for index A < index B."""
    b = N / 2
    a = int(ceil(float(N)/2))

    if K > b * a:
        return ""
    elif K == b * a:
        return "A" * a + "B" * b

    return "B" * ((b-1) - K // a) + "A" * (K % a) + "B" + "A" * (a - (K % a)) + "B" * (K // a)


for i in range(13):
    print createString(7, i)

