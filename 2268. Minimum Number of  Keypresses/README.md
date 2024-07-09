# Intuition
We can use a greedy approach to find the minimum keypresses needed. We can map the first nine most repeated characters to one key, next nine most repeated characters to two keys, and the rest to three keys.

* Time Complexity: O(nlogn) from pushing and popping the heap
* Space Complexity: O(1) from storing the occurences of letters
