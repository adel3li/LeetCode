class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

#  bin() is an in-built function in Python that takes in integer x and returns the binary representation of x in a string format.
# If x is not an integer,
# then the _index()_ method needs to be implemented to obtain an integer as the return value instead of as a “TypeError” exception.
# source(Educative).
