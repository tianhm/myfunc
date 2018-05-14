import cmath
import math

def HHV(slist, n):
    """
    Highest value over a specified period
    """
    max_list = []
    i = 0
    while i < len(slist):
        if i + 1 < n:
            MAX = max(slist[0:i+1])
        else:
            start = i + 1 - n
            end = i + 1
            MAX = max(slist[start:end])
        max_list.append(MAX)
        i += 1
    return max_list

def MAXINDEX(df, n, price='Close'):
    """
    Index of highest value over a specified period
    """

def LLV(slist, n):
    """
    Lowest value over a specified period
    """
    min_list = []
    i = 0
    while i < len(slist):
        if i + 1 < n:
            MIN = min(slist[0:i+1])
        else:
            start = i + 1 - n
            end = i + 1
            MIN = min(slist[start:end])
        min_list.append(MIN)
        i += 1
    return min_list


if __name__=='__main__':
    a=[1,3,4,5,2,3,56,22,22,55,66,22,11]
    hva=HHV(a,5)
    print(a)
    print( hva)
    print(LLV(a,5))