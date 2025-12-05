"""
This is a test sentnce.Please count number of etration in this sentnce.
Input: Hello Word, I Ravi Kumar. I love to code.with python. Python is great language.
Output: [("hello", 1), ("word", 1), ("i", 2), ("ravi", 1), ("kumar", 1), ("love", 1), ("to", 1), ("code", 1), ("with", 1), ("python", 2), ("is", 1), ("great", 1), ("language", 1)]

RULES:

1. Ignore punctuation marks (.,!?:;-' etc.)
2. Convert all words to lowercase
3. Shorte the output list base on count in descending order. If two words have same count, sort them in ascending alphabetical order.:
"""
from collections import Counter
import re
from typing import Optional

def main(sentence: str, length:Optional[int] = None) -> str:
    
    if not isinstance(sentence, str):
        return None
    
    sentance_list = re.sub(r'[^A-Za-z0-9\s]', '', sentence).split(' ')

    counter = Counter(sentance_list)
    result = counter.most_common(length)
    result = sorted(result, key=lambda x: x[1])
    print(result)


main('hello, ravi, hello sumiot. ravi hi rohit', None)
