def high(x):
    # Define a lambda function to calculate the score of a word
    word_score = lambda word: sum(ord(char) - ord('a') + 1 for char in word)
    
    # Split the input string into words and calculate the score for each word
    words = x.split()
    scores = [word_score(word) for word in words]
    
    # Find the index of the highest score
    max_index = scores.index(max(scores))
    
    # Return the word with the highest score
    return words[max_index]

print(high("abad abc xyz"))
