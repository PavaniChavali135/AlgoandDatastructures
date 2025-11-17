from Trie import Trie

def run_demo():
   
    # 1. Initialize the Trie data structure
    trie = Trie()

    # 2. Inserting a sample word list to populate the dictionary
    word_list = ["car", "cargo", "cart", "cat", "apple", "app", "application"]
    print(f"Populating Trie with: {word_list}")
    for word in word_list:
        trie.insert(word)
    print("Insertion complete\n")

    test_prefixes = ["ca", "app","z"]

    for prefix in test_prefixes:
        print(f"Test Case: Auto-complete for prefix '{prefix}'")
        suggestions = trie.get_autocomplete_suggestions(prefix)
        
        if suggestions:
            print(f"Found {len(suggestions)} suggestions: {suggestions}")
        else:
            print("No suggestions found.")
        print("next input \n")
        
run_demo()