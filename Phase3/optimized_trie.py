import sys
import time
import random
import string
import heapq

class TrieNode:
    __slots__ = ['children', 'is_end_of_word', 'frequency', 'word']

    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False
        self.frequency = 0
        self.word = None 

class OptimizedTrie:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 1

    def insert(self, word, freq=1):
        node = self.root
        word = word.lower()
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.node_count += 1
            node = node.children[char]
        
        node.is_end_of_word = True
        node.word = word
        node.frequency = freq

    def get_autocomplete_suggestions(self, prefix, top_k=5):
        prefix = prefix.lower()
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        stack = [node]
        suggestions_heap = [] 
        
        while stack:
            curr = stack.pop()
            
            if curr.is_end_of_word:
                if len(suggestions_heap) < top_k:
                    heapq.heappush(suggestions_heap, (curr.frequency, curr.word))
                else:
                    if curr.frequency > suggestions_heap[0][0]:
                        heapq.heappushpop(suggestions_heap, (curr.frequency, curr.word))
            
            for child in curr.children.values():
                stack.append(child)
                
        return sorted([item[1] for item in suggestions_heap], reverse=True, key=lambda x: x)

    def get_fuzzy_suggestions(self, word, max_distance=2):
        results = set()
        word = word.lower()
        
        def recursive_search(node, letter, previous_row):
            columns = len(word) + 1
            current_row = [previous_row[0] + 1]

            for col in range(1, columns):
                insert_cost = current_row[col - 1] + 1
                delete_cost = previous_row[col] + 1
                replace_cost = previous_row[col - 1] + (0 if word[col - 1] == letter else 1)

                current_row.append(min(insert_cost, delete_cost, replace_cost))

            if min(current_row) <= max_distance:
                if node.is_end_of_word and current_row[-1] <= max_distance:
                    results.add(node.word)

                for char, child in node.children.items():
                    recursive_search(child, char, current_row)

        first_row = range(len(word) + 1)
        for char, child in self.root.children.items():
            recursive_search(child, char, first_row)
            
        return list(results)

class TestBench:
    def __init__(self):
        self.trie = OptimizedTrie()
        self.dataset = []

    def generate_dataset(self, num_words=100000):
        print(f"Generating random dataset of {num_words} words")
        for _ in range(num_words):
            length = random.randint(3, 10)
            word = ''.join(random.choices(string.ascii_lowercase, k=length))
            freq = random.randint(1, 100) 
            self.dataset.append((word, freq))
        print("Dataset generation complete.")

    def stress_test(self):
        print("\nRigorous input insertion")
        start_time = time.time()
        for word, freq in self.dataset:
            self.trie.insert(word, freq)
        end_time = time.time()
        print(f"Inserted {len(self.dataset)} words in {end_time - start_time:.4f} seconds.")
        print(f"Total Nodes Created: {self.trie.node_count}")

        print("\nQuery autocomplete")
        prefixes = [''.join(random.choices(string.ascii_lowercase, k=2)) for _ in range(1000)]
        
        start_time = time.time()
        for p in prefixes:
            self.trie.get_autocomplete_suggestions(p)
        end_time = time.time()
        print(f"Executed 1000 Autocomplete queries in {end_time - start_time:.4f} seconds.")

    def edge_cases(self):
        print("\nEdge case")
        
        # Case 1: Empty String
        try:
            res = self.trie.get_autocomplete_suggestions("")
            print(f"Empty string input handling Result: {res}")
        except Exception as e:
            print(f"Empty string crashed system: {e}")

        # Case 2: Non-existent Prefix
        res = self.trie.get_autocomplete_suggestions("xyz123")
        if res == []:
            print("Non-existent prefix so returns empty list.")
        else:
            print(f"Unexpected result for non-existent prefix: {res}")

        # Case 3: Deep String
        long_str = "a" * 500
        try:
            self.trie.insert(long_str)
            res = self.trie.get_autocomplete_suggestions(long_str[:499])
            print("string with 500 characters is inserted and queried without StackOverflow.")
        except RecursionError:
            print("RecursionError detected on long string.")

    def fuzzy_test(self):
        print("\nspelling correction test")
        self.trie.insert("algorithm", 100)
        
        typo = "algorythm" 
        suggestions = self.trie.get_fuzzy_suggestions(typo, max_distance=2)
        print(f"Input: '{typo}' Suggestions: {suggestions}")
        
        if "algorithm" in suggestions:
            print("Fuzzy logic found 'algorithm' from 'algorythm'.")
        else:
            print("Fuzzy logic failed to correct typo.")

test = TestBench()
test.generate_dataset(num_words=100000)
test.stress_test()
test.edge_cases()
test.fuzzy_test()