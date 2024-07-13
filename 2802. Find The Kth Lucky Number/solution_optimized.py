class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        # transfer k+1 into binary form and get rid of its most significant bit
        binary = bin(k + 1)[3:]

        #replace 0s with 4s and 1s with 7s
        binary = binary.replace("0", "4")
        binary = binary.replace("1", "7")
        return binary