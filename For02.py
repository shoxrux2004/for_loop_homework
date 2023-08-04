def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    result=''
    i=0
    for i in range(n):
        result+=','+str(i)
    return result[1:]
print(main(n=3))