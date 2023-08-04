def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(B,A-1,-1):
        l.append(i)
    return l
print(main(A=5,B=9))