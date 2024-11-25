import string


def ispangram(str1: string, alphabet=string.ascii_lowercase) -> bool:
    """
    checks if letters in a string are a panagram

    Args:
        str1 (string): String of letters
        list of letters to compare string to. Defaults to string.ascii_lowercase.

    Returns:
        bool: true if panagram
    """
    # remove the spaces and convert to lower cases
    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    # Add the unique letters of string1 to a set
    str1_letters = set(str1)
    alphabetSet = set(alphabet)
    # Check if all alphabet letters are in the string's set of characters
    return alphabetSet.issubset(str1_letters)


print(ispangram("The quick brown fox jumps over the lazy dog"))
