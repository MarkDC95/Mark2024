# Pangram Checker

This project implements a Python function that checks if a given string is a **pangram**. A **pangram** is a sentence that contains every letter of the alphabet at least once.

The program works by:

1. Removing spaces and non-alphabet characters.
2. Converting the string to lowercase.
3. Checking if the string contains all 26 letters of the English alphabet.

## Usage

### Calling the Function

To use the `ispangram` function, you need to pass a string as an argument. The function will then check if the string contains all letters of the English alphabet and return `True` if it is a pangram, or `False` otherwise.

### Example:

```python
ispangram("The quick brown fox jumps over the lazy dog")
```

outputs:

```python
True
```
