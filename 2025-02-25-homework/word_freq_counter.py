def count_word_frequencies(sentence):
    """
    Create a function that takes a sentence and returns a dictionary 
    containing the frequency of each word (case-insensitive).
    
    Example:
    >>> count_word_frequencies("The cat and the dog are friends")
    {'the': 2, 'cat': 1, 'and': 1, 'dog': 1, 'are': 1, 'friends': 1}
    """
    # Your code here
    pass

# Test cases
test_cases = [
    "The cat and the dog are friends",
    "Python Python PYTHON python",
    "Hello! Hello? hello..."
]

# Run your function against the test cases
for test in test_cases:
    print(f"\nInput: {test}")
    print(f"Output: {count_word_frequencies(test)}")