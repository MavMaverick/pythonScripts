def split_string_at_space(text, max_char_limit):
    """
    Splits a string into two parts: a line of specified max length, wrapping at spaces, 
    and the remaining text. Long words exceeding max length are hyphenated.

    Parameters:
    - text (str): The input string to be wrapped.
    - max_char_limit (int): The maximum number of characters per line.

    Returns:
    - tuple (str, str): A line wrapped to fit within the specified length, and the remaining text.

    Example:
    >>> split_string_at_space("This is a sample string that needs to be split.", 10)
    ("This is a", "sample string that needs to be split.")
    """
    
    text_length = len(text) # Calculate text length once to reduce calculations

    # If the text length is within the limit, return it as-is 
    if text_length <= max_char_limit:
        return text, ""

    # If the next character after max_char_limit's index is a " "
    if text[max_char_limit] == " ":
        return text[0:max_char_limit], text[max_char_limit + 1:]

    # If max_char_limit isn't a space, search backwards for the nearest space
    curr_index = max_char_limit - 2
    while curr_index > 0 and text[curr_index] != " ":
        curr_index -= 1

    # If curr_index is zero, the word exceeds max length and should be split with a hyphen
    # Example: If max_char_limit = 29, and text is 'supercalifragilisticexpialidocious', 
    #          split into ['supercalifragilisticexpiali-', 'docious']
    if curr_index == 0:
         return text[0:max_char_limit - 1]+'-', text[max_char_limit - 1:]

    # Return everything up to the space (but not space), and everything after space.
    else:
         return text[0:curr_index], text[curr_index + 1:]

def wrapper(words, max_char_limit):
    """
    Wraps a string into multiple lines, each line fitting within the specified character limit.
    It uses the split_string_at_space function to ensure that lines wrap at spaces when possible, 
    and hyphenates long words that exceed the character limit.

    Parameters:
    - words (str): The input string to be wrapped into lines.
    - max_char_limit (int): The maximum number of characters allowed per line.

    Returns:
    - list of str: A list of strings, each representing a line that fits within the specified limit.

    Example:
    >>> wrapper("This is a sample string that needs to be split into multiple lines.", 10)
    ["This is a", "sample", "string", "that needs", "to be", "split into", "multiple", "lines."]
    """
    lines = []
    while words:
        line, words = split_string_at_space(words, max_char_limit)
        lines.append(line)
    return lines
 

# for line in lines:
#     print(line)

