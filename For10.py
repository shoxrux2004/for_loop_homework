def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(0,len(list1)):
        l.append(list1[i].capitalize())
    return l
print(main(list1=['rustam','diyor','alisher']))