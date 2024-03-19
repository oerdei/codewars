def order(sentence):
  if not sentence:
      return ""
  words = sentence.split()
  sorted_words = sorted(words, key=lambda w: int(''.join(c for c in w if c.isdigit())))
  return ' '.join(sorted_words)

sentence = "is2 Thi1s T4est 3a"
print(order(sentence))
'''
This code splits the input string into a list of words, then uses the sorted function with a custom key function to sort the words based on the embedded number in each word. Finally, it joins the sorted words into a string and returns the result.
'''

