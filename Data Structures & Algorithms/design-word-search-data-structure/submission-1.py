class WordNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.word

            c = word[i]

            if c == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            if c not in node.children:
                return False

            return dfs(i + 1, node.children[c])

        return dfs(0, self.root)
        

