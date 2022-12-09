

files = ['adjectives.txt', 'nouns.txt']
for file_name in files:
    # read file
    with open(file_name, 'rt') as f:
        content = f.read().lower()
    # write file
    with open(file_name, 'wt') as f:
        f.write(content)
    # check file
    with open(file_name, 'rt') as f:
        if f.read().islower():
            print(f'file: {file_name} is all lowercase')
        else:
            print(f'file: {file_name} failed to make it all lowercase')
        
