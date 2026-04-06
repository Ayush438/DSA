#solved using BFS (Breadth-First Search) because we need the shortest path.

Approach (BFS + Set)
1. Convert wordList → set (O(1) lookup)
2. Start BFS from beginWord
3. For each word:
  Change every character (a → z)
  Generate all possible next words
4. If generated word exists in set:
  Add to queue
  Remove from set (avoid revisiting)
5. If endWord found → return level


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet=set(wordList)
        if endWord not in wordList:
            return 0

        queue=deque([(beginWord,1)])

        while queue:
            word, level=queue.popleft()

            if word==endWord:
                return level
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word= word[:i]+ ch + word[i+1:]  

                    if new_word in wordSet:
                        queue.append((new_word , level+1))
                        wordSet.remove(new_word)
            
        return 0
