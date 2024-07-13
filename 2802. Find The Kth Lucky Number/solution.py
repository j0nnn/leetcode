class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        digit = 1
        # calculate the nubmer of digits that exist in the result while also calculating how many variations are left
        while 2 ** (digit) < k:
            k -= 2 ** digit
            digit += 1

        left = k
        # transform the number of variations left into the correct length of the result in binary form
        binary = bin(left - 1)[2:]
        if len(binary) != digit:
            binary = "0" * (digit - len(binary)) + binary

        # replaces the 0s with 4s and 1s with 7s
        binary = binary.replace("0", "4")
        binary = binary.replace("1", "7")
        return binary