'''
Multiples of 3 or 5
-------------------
Problem 1
---------

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiples_of_3_or_5(num_range):
    
    """Find the multiples of 3 and 5 in difined range

    Args:
        num_range (int): Range of number to check

    Returns:
        list: Multiples of 3 or 5
    """
    
    if num_range < 1:
        print('Range needs to be higher than 0!')
        return

    multiples = []
    
    for num in range(1, num_range):
        if num % 3 == 0:
            multiples.append(num)
        elif num % 5 == 0:
            multiples.append(num)
    
    return multiples

if __name__ == '__main__':
    
        result = sum(multiples_of_3_or_5(0))
        print(result)
