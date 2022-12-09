
def duplicates(words: str) -> bool:
    found = []
    for i, word in enumerate(words.strip('\n').split('\n')):
        if word in found:
            return (False, word, i)
        found += word
    return (True, None, None)

files = [
    'adjectives.txt',
    'nouns.txt',
]
for file_name in files:
    with open(file_name, 'rt') as f:
        content = f.read()
    has_duplicate, word, line = duplicates(content)
    if not has_duplicate:
        print(f'duplicate on line: {line} with word: {word} in file {file_name}')
    else:
        print(f'no duplicates in file {file_name}')

    
    
