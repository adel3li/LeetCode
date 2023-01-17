class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []

        for i in operations :

            # For operation "+", there will always be at least two previous scores on the record.
            # if i == '+'. Record a new score that is the sum of the previous two scores.

            if i == "+" and len(record) >= 2 :
                record.append(record[-1] + record[-2])

            # For operations "C" and "D", there will always be at least one previous score on the record.
            # if i = 'D'. Record a new score that is the double of the previous score.

            elif i == "D" and len(record) >= 1 :
                record.append(record[-1] * 2)

            # For operations "C" and "D", there will always be at least one previous score on the record.
            # if i = 'C'. Invalidate the previous score, removing it from the record.

            elif i == "C" and len(record) >=1 :
                record.pop()

            # if i ia An integer x.Record a new score of x.

            else :
                record.append(int(i))

        #Return the sum of all the scores on the record after applying all the operations.

        return sum(record)
        

#Time Complexity: O(N), where N is the length of operations. We parse through every element in the given array once, and do O(1) work for each element.

#Space Complexity: O(N), the space used to store our stack(record).
