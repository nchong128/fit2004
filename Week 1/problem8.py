def fibByIteration(n):
    '''
    Time complexity: O(n)
    Space complexity: O(1)
    '''

    # Check if n is integer and non-negative
    assert (type(n) == int), "n must be an integer"
    assert (n > 0), "n must be non-negative"

    if (n <= 2):
        return 1

    prevFib = 1
    fib = 1

    for i in range(2,n):
        temp = fib
        fib += prevFib
        prevFib = temp
    
    return fib

def fibByRecursion(n):
    '''
    Time complexity: O(2^n)
    Space complexity: O(n)
    '''

    if (n <= 2):
        return 1
    else:
        return fibByRecursion(n-1) + fibByRecursion(n-2)

n = 10
