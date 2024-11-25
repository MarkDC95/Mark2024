# Frequently Used Words Finder

This project implements a Python class `FrequentlyUsedWords` that identifies and prints the most frequently occurring words in a given text message. The words are sorted by their frequency in descending order, and ties are resolved lexicographically (alphabetical order).

## How It Works

1. **Input Standardization**:

   - Converts the input string to lowercase.
   - Removes all punctuation characters.

2. **Word Counting**:

   - Splits the standardized text into individual words.
   - Counts the frequency of each word.

3. **Sorting**:

   - Sorts words by frequency in descending order.
   - For words with the same frequency, sorts them lexicographically in ascending order.

4. **Output**:
   - Prints the top N words based on frequency.

## Usage

### Creating an Instance

To use the `FrequentlyUsedWords` class, initialize it with:

1. A text message (string).
2. The number of top frequent words to display (`n`), defaulting to 10.

### Example

```python
# Example input
text = "Hi, my name is is Mark"

# Initialize the class with the text and the number of top words to display
fw = FrequentlyUsedWords(text, n=2)

# Print the top N most frequent words
fw.printWord()
```

output

```python
[('is', 2), ('hi', 1)]
```
