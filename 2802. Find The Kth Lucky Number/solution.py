class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        digit = 1
        while 2 ** (digit) < k:
            k -= 2 ** digit
            digit += 1
            
        left = k
        binary = bin(left - 1)[2:]
        if len(binary) != digit:
            binary = "0" * (digit - len(binary)) + binary
        binary = binary.replace("0", "4")
        binary = binary.replace("1", "7")
        return binary