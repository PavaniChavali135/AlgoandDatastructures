class TrieNode:
    def __init__(self):
        self.children = {} #this acts as hashmap that maps a character to a correspinding child trienode object
        self.is_end_of_word = False #this becomes True if the path from root to the node represents a complete word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        #Implements the insertion algorithm to add a word to the Trie

        word = word.lower()
        current_node = self.root

        for char in word:
            #checking if the character exists as a key
            if char not in current_node.children:
                #if not found create a new Trie node
                current_node.children[char] = TrieNode()
            #update current node to point to the children
            current_node = current_node.children[char]
        current_node.is_end_of_word= True

    def get_autocomplete_suggestions(self,prefix):
        prefix = prefix.lower()
        suggestions = []

        current_node = self.root
        for char in prefix :
            if char not in current_node.children:
                #if prefix path is not present return empty list
                return []
            current_node = current_node.children[char]
        self.find_word_from_node(current_node, prefix, suggestions)
        return suggestions
    
    def find_word_from_node(self,node, current_prefix, suggestions):
        #helper method to perform recursive DFS
        if node.is_end_of_word:
            suggestions.append(current_prefix)

        for char,child_node in node.children.items():
            self.find_word_from_node(child_node, current_prefix + char, suggestions)


            



            
                
            

            

