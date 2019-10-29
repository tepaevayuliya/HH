def maximal_element(arg):
    if arg == []:
        return -1
    elif len(arg) == 1:
        return 0
    else:
        maxElement = arg[0]
        maxIndex = 0
        for i in range(1, len(arg)):
            if arg[i] > maxElement:
                maxElement = arg[i]
                maxIndex = i
        return maxIndex
