# Intuition
This question is relatively similar to Clone Graph question. We can choose any tree traversal method that will allow us to reach all possible ndoes and save the encountered nodes in a hashmap that maps the node to its copy. We create copies of the nodes and assign its corresponding pointer values during the second traversal of the hashmap after we know that all possible nodes and its copies have been created.
* Time Copmlexity: O(n) from traversing each node twice
* Space Complexity: O(n) from storing each node and their copies in a hashmap