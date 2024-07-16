# Intuition
Given any interval problem, oftentimes the first thing to do is to sort the intervals so that it is to our benefit to process it. In this case, the brute force solution also requires us to sort the intervals by start time first. We can keep track of all active meetings in an array and also keep track of the maximum size the array achieved. While iterating through all intervals, we check if there is any interval in this array that has already ended and therefore could be replaced. 
* Time Complexity: O(n^2) from iterating through the intervals and also iterating through the intervals in the active meetings array
* Space Complexity: O(n) from storing the intervals in the active array

# Heap Solution
Instead of storing all the intervals in a stack and iterating through all of it, we observe that we are only comparing the ending times of these stored intervals. Therefore, this is the only attribute that we need to store. Moreover, we recognize that we simply need to compare the current interval with the earliest end time of the ongoing intervals to check if any can be popped out. We can utilizxe a minHeap to achieve this functionality
* Time Complexity: O(nlogn) from sorting the intervals and popping and pushing elements into the heap
* Space Comlexity: O(n) from storing the ending times into the heap