class Trie():
    
    def __init__(self, children={}):
        self.end_of_word = False
        self.children = children

    def insert(self, word):
        if not word:
            self.end_of_word = True
        elif word[0] in self.children:
            self.children[word[0]].insert(word[1:])
        else:
            t = Trie({})
            t.insert(word[1:])
            self.children[word[0]] = t

    def search(self, word):
        if word:
            if word[0] in self.children:
                return self.children[word[0]].search(word[1:])
            else:
                return False
        else:
            return self.end_of_word

    def traverse(self, prefix=""):
        if self.end_of_word:
            yield prefix
        for char in self.children:
            for word in self.children[char].traverse(prefix + char):
                yield word


import unittest

class Test(unittest.TestCase):
    def test_insert_retrieve(self):
        words = ["as", "at", "be", "by", "bet", "byte", "ask", "ate", "a", ""]
        t = Trie()
        for word in words:
            t.insert(word)
        for word in words:
            self.assertTrue(t.search(word))

    def test_traverse(self):
        words = ["as", "at", "be", "by", "bet", "byte", "ask", "ate", "a", ""]
        t = Trie()
        for word in words:
            t.insert(word)
        print(list(t.traverse()))
        self.assertEqual(set(words), set(t.traverse()))

if __name__ == '__main__':
    unittest.main()
