class Trie:
    """
    Trie with values associated to words. 
    """
    def __init__(self):
        self.children = dict()
        self.value = -1

    def find(self, word):
        current = self
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def insert(self, word, value):
        current = self
        for i, char in enumerate(word):
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        current.value = value
