class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha = []
        numeric = []

        # split the string into array for easier comparisons
        for log in logs:
            arr = log.split(' ')
            if arr[1].isalpha():
                alpha.append(arr)
            else:
                numeric.append(log)

        # sort the letter-logs by their content, then by their identifier with lambda function
        alpha.sort(key=lambda x: [x[1:], x[0]])

        # append everything back into a result array with the given order and also joining the arrays
        result = []
        for a in alpha:
            string = " ".join(a)
            result.append(string)
        for n in numeric:
            result.append(n)
        return result