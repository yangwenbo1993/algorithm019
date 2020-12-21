# 实现 Trie (前缀树)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root= TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_end = True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return True

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


# 单词搜索 II

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, prefix, visited):
            if '#' in node:
                result.add(prefix)
                del node['#']
            visited.add((i,j))
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                the_i,the_j = i+di,j+dj
                if -1 < the_i < h and -1 < the_j < w and board[the_i][the_j] in node and (the_i, the_j) not in visited:
                    search(the_i, the_j, node[board[the_i][the_j]], prefix+board[the_i][the_j], visited)
                    if not node[board[the_i][the_j]]:
                        del node[board[the_i][the_j]]
            visited.remove((i,j))


        result, h, w,visited = set(), len(board), len(board[0]),set
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], visited)
                    if not trie[board[i][j]]:del trie[board[i][j]]
        return list(result)










# N皇后

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cheseboard = [['.'] * n for _ in range(n)]

        def backtracking(n, row, cheseboard):
            if row == n:
                temp_res = []
                for temp in cheseboard:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                result.append(temp_res)
                return
            for col in range(n):
                if isValid(row, col, cheseboard):
                    cheseboard[row][col] = "Q"
                    backtracking(n, row + 1, cheseboard)
                    cheseboard[row][col] = "."

        def isValid(row, col, cheseboard):
            for i in range(len(cheseboard)):
                if cheseboard[i][col] == 'Q':
                    return False

            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if cheseboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i = row - 1
            j = col + 1
            while i >= 0 and j < len(cheseboard):
                if cheseboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        backtracking(n, 0, cheseboard)
        return result