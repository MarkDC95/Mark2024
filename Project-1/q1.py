import string

class FrequentlyUsedWords:

    def __init__(self, message, n=10):
        self.message = message
        self.n = n

    def standardizeAndRemovePunctuation(self):
        """
        Converts the input message to lowercase and removes punctuation.

        Returns:
            string: a string of characters without punctuation
        """
        messageWithoutPunctuation = ""
        message = self.message.lower()
        for char in message:
            if char not in string.punctuation:
                messageWithoutPunctuation += char
        return messageWithoutPunctuation

    def printWord(self):
        """
        Prints the top N most frequent words in the message, sorted by frequency
        and lexicographically in case of a tie.
        """
        # Remove punctuation and convert to lowercase
        standardized_message = self.standardizeAndRemovePunctuation()

        # Split into words and count frequency
        words = standardized_message.split()
        wordCounter = {}
        for word in words:
            wordCounter[word] = wordCounter.get(word, 0) + 1

        # Sort by frequency (descending) and lexicographical order (ascending) for ties
        sorted_items = sorted(wordCounter.items(), key=lambda item: (-item[1], item[0]))

        # Take the top N items
        top_n_words = sorted_items[:self.n]

        # Print the results
        print(top_n_words)


# Example usage
x = FrequentlyUsedWords("Hi, my name is is mark", n=2)
x.printWord()
