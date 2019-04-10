"""
If we were storing arrays of integers, to prevent clustering of both
forms, we would want both the position and value of all elements to
be taken into account.

- Least problematic: Return sum of numbers in the array
This allows us to take the value of all the elements into account so
that only lists of the same total value will hash to the same index

- Medium: Return first number of array
This at least allows us to consider a single value of the array, which
is still bad considering all arrays with the same first value, regardless
of the other elements will hash to the same index

- Most problematic: Return random number in the array
A hash function should always be deterministic. Using a random number
in the array will make the hash function non-deterministic

Better candidate hash function
- We want to take in both position and value of all elements in the array
- Hash function can be the sum of each element's value to the power of its
- position (index + 1)
- e.g. [10,5,7,2] = (10^1 + 5^2 + 7^3 + 2^4) % 4
"""