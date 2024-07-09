# Inutition
We are given the range and need to compute the number of plates between candles in the given range. Use prefix sum to calculate the number of plates in any given range. To compute the actual range (disregard plates not enclosed by candles), we have to keep track of the nearest candles to the left and right of any given position.

* Time Complexity: O(n) from iterating through the string twice to form the prefix sum and calculate the corresponding candles
* Space Complexity: O(n) from storing all the positions of the nearest candles to the left and right of each plate and the prefix sum