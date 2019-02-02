 
# Get largest and smallest number from a tuple of tuple with integer and string values 

 def getTuple(aTuple):
    aNum = ()
    aWord = ()

    for t in aTuple:
        aNum = aNum + (t[0],)
        if t[1] not in aWord:
            aWord = aWord + (t[1],)

    maxNum = max(aNum)
    minNum = min(aNum)
    return maxNum, minNum


