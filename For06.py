def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    i=0
    sum=0
    for i in range(A-1,B-1):
        i+=1
        sum+=i
    return sum
print(main(3,6))