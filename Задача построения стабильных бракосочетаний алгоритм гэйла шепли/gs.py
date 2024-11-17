prefer = [[7, 5, 6, 4], [5, 4, 6, 7],
          [4, 5, 6, 7], [4, 5, 6, 7],
          [0, 1, 2, 3], [0, 1, 2, 3],
          [0, 1, 2, 3], [0, 1, 2, 3]]
N = len(prefer) // 2


def wPrefersMOverM1(prefer, w, m, m1):
    for i in range(N):
        if prefer[w][i] == m:
            return False
        if prefer[w][i] == m1:
            return True


def stableMarriage(prefer):
    preferData = prefer.copy()
    wPartner = [-1 for i in range(N)]
    freeList = [i for i in range(N)]
    while len(freeList) > 0:
        m = freeList.pop()
        w = preferData[m][-1]
        m1 = wPartner[w - N]
        if m1 == -1:
            wPartner[w - N] = m
        elif wPrefersMOverM1(preferData, w, m, m1):
            wPartner[w - N] = m
            preferData[m1].remove(w)
            freeList.append(m1)
        else:
            preferData[m].remove(w)
            freeList.append(m)
    print("Woman ", " Man")
    for i in range(N):
        print(i + N, "\t", wPartner[i])
        

stableMarriage(prefer)



