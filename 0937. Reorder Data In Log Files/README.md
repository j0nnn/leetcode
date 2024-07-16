# Intuition
The directions in this question is pretty clear, we have to sort the letter-logs lexicographically by their content, then their identifiers. Therefore, we separate out the letter-logs from the numeric ones, then use a lambda function as a comparator to sort the logs. We split the string into array for simpler comparison. Then, we append all the logs back together in their sorted order
* Time Complexity: O(nlogn) for sorting the letter-logs
* Space Complexity: O(n) for storing all the logs