# Intuition
I knew that this problem has to do with bit maniuplation based on the structure of the problem. I identified the fact that there are only two digits possible and that we are asked for the kth number that satisfies the constraints. I broken the problem down into subsections, where the number of digits is its own category. We first find how many digits the answer is going to contain, then subtracting the number of possible combinations made up by those that have lower digit then it. Then, we construct the binary from the number we have left.
* Time Complexity: O(logk) from finding the number of digits the final result has
* Space Complexity: O(logk) for constructing the final number

# Optimized Bit Maniuplation
If we were to write out the patter, we would find that the result corresponded to the binary of k+1 with the most significant bit dropped. Knowing this, we can simply perform these operations to find the result given the k.
* Time Complexity: O(logk) for representing the k into binary
* Space Complexity: O(logk) for also saving the binary representation