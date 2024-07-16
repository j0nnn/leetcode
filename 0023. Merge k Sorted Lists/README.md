# Intuition
We know that all the given lists are sorted. Therefore, to create a merged list of all the elements, my first intuition is to compare each of the elements in the beginning of the list to find the smallest number. Then, add that number to a result linked list and repeat until there is no more nodes list in any of the given lists. 
* Time Complexity: O(kn) as we are comparing the beginning of every list to know which element to add to our result linked list
* Space Complexity: O(n) as we need to create the final linked list

# Divide and Conquer Approach
Utilizing concept similar to merge sort, we can simply perform divide and conquer so that we are only comparing two at once instead of all k lists. This would cut down the number of comparisons and therefore the time complexity.
* Time Complexity: O(nlogk) as we would only need to merge log k lists
* Space Complexity: O(1) as we can merge the list in constant time since we are only merging two lists at once at most