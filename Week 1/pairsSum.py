# [1,2,4,4] sum = 8 -----> answer = true
# [1,2,3,9] sum = 8  -----> answer = false
# [1,2,3,9] sum = 5 -----> answer = true
# [-1,-2,3,9] sum = 8
# [1,2,3,4,5]

# List is sorted
# Integers
# Can be repeating numbers
# Negatives can be allowed

# Iterate over every possible pair of numbers (O(n2))
# For each number binary search the sum to see if it has the number (O(n + log(n)) = O(n)

# cases
# List has 0 or 1 elements -> Early exit (false)
# Sum being lower than current computed
# Sum being higher than current computed

def pairsSum(list, sum):
    if len(list) < 2:
        return False

    i = 0
    j = len(list) - 1

    while i < j:
        computedSum = list[i] + list[j]
        if computedSum == sum:
            return True
        elif computedSum < sum:
            i += 1
        else:
            j -= 1

    return False

print(pairsSum([1,2,4,9], 8))
