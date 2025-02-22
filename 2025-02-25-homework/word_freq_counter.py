def count_word_frequencies(sentence):
    """
    Create a function that takes a sentence and returns a dictionary 
    containing the frequency of each word (case-insensitive).
    
    Example:
    >>> count_word_frequencies("The cat and the dog are friends")
    {'the': 2, 'cat': 1, 'and': 1, 'dog': 1, 'are': 1, 'friends': 1}
    """
    #split each sentence into w. then count the frequency of each owrd 
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


def count_word_frequencies(sentence):
 
    # Convert to lowercase . otherwise i will have to add more variables to deal with uppercase and lowercase,instead of just  lowercase  letters. This does not affect the word count. 
    sentence = sentence.lower()

    # Manually remove punctuation by keeping only letters, numbers, and spaces. It makes sure the program does not count punctuation as words.
    cleaned_sentence = ""
    for c in sentence:
        #c stands for character.
        if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9') or  c == ' ':
            cleaned_sentence += c

    # Split the cleaned sentence into words  manually using arrays and splicing. This will allow us to later compare individual words.
    w = []
    word = ""
    for c in cleaned_sentence:
        if c == " ":
            if word:
                w += [word]  # Manually append to list
                word = ""  # Reset word
        else:
            word += c
    if word:
        w += [word]  # Add last word if exists

    # Count word frequencies using a dictionary
    word_count = {}
    for word in w:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
