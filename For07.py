def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    sum=0
    i=0
    for i in range(0,N,2):
        i+=1
        sum+=i
    return sum
print(main(12))