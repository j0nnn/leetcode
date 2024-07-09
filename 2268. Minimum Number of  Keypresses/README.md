# Solution
The goal of this problem is to get the minimum number of keypresses given a string. 
* To minimize the key presses, we want the most frequently pressed characters to be mapped to a single press. 
* We use Counter in the collections module to counter the occurences of each letter of the input string.
* We put all the letters in a maxHeap so that we can access the letters with the most occurence first.
* We loop through the maxHeap and add the corresponding number of keypresses required.
* We have a variable to keep track of the keypresses that we have mapped.
* Time Complexity: O(nlogn) from pushing and popping the heap
* Space Complexity: O(1) from storing the occurences of letters
