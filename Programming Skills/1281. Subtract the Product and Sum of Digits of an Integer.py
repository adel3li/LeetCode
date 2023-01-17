class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits_list = []
        product_of_digits = 1
        sum_of_digits = 0

        for i in str(n):
            digits_list.append(i)

        for i in digits_list :
            product_of_digits *= int(i)
            sum_of_digits += int(i) 

        result = (product_of_digits) - (sum_of_digits)

        return result

