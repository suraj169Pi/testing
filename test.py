python
import re

def removeDuplicateWords(input):
    """
    Removes consecutive duplicate words from a string
    Maintains original spacing and capitalization
    
    Args:
        input (str): Input string containing potential duplicates
        
    Returns:
        str: String with consecutive duplicates removed
    """
    # Updated regex pattern to better handle word boundaries and duplicates
    # \b ensures word boundaries
    # \w+ matches entire words
    # \s+ matches any whitespace
    regex = r'(\b\w+\b)(\s+\1)+'
    
    return re.sub(regex, r'\1', input, flags=re.IGNORECASE)

str1 = "Good bye bye world world"
print(removeDuplicateWords(str1))

str2 = "Ram went went to to his home"
print(removeDuplicateWords(str2))

str3 = "Hello hello world world"
print(removeDuplicateWords(str3))