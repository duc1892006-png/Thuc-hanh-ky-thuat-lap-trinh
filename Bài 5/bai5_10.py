def bubbleSort(nlist):
    loop = len(nlist)
    for i in range(loop):
        swapped = False
        for j in range(loop - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        if not swapped:
            break
    return nlist
