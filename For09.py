def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    l=[]
    sum=1
    i=0
    for i in range(1,10):
        sum=i*price
        l.append(sum)
    return l
print(main(2.25))