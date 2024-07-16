class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # store the relationship between the words in the wordList and all the possible words that it could create
        option = {}

        wordList.append(beginWord)
        for word in wordList:
            if word not in option: option[word] = []
            for i in range(len(word)):
                # new word would be the old word with a letter starred out to indicate it could be any character
                newWord = word[:i] + "*" + word[i+1:]
                if newWord not in option: option[newWord] = []
                # add link between word and newWord and newWord and word
                option[word].append(newWord)
                option[newWord].append(word)
        
        # set up for bfs
        queue = []
        queue.append(beginWord)
        level = 0
        seen = set()
        while queue:
            for i in range(len(queue)):
                word = queue.pop(0)
                # if word is the endWord, we reached our goal and return the level we found it
                if word == endWord:
                    return level + 1
                # if cycle is detected, we skip over it
                if word in seen:
                    continue
                seen.add(word)
                # add any other word that is linked to this current word to the queue for more bfs
                for neighbor in option[word]:
                    for second_neighbor in option[neighbor]:
                        queue.append(second_neighbor)
            level += 1
        return 0
            
        
        