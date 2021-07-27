"""
The justification is greedy - as many words as possible in a single line,
some text define in 'words' variable, length line define in 'maximum_width' variable
Spaces between words distributed maximum evenly.
The last line aligned left with no additional spaces.
"""

words = "some text here to check the action of our algorithm"
maximum_width = 16

arr = words.split()
new_arr = []
new_str = ''

for word in arr:
    if len(new_str) < maximum_width:
        temp_str = new_str + word
        if len(temp_str) < maximum_width:
            new_str = temp_str
            if len(new_str) < maximum_width:
                new_str += ' '
        else:
            new_arr.append(new_str)
            new_str = word + ' '
    else:
        new_arr.append(new_str)
        new_str = word + ' '
else:
    new_arr.append(new_str)

for el in new_arr:
    if el != new_arr[-1]:
        trim_str = el.strip()
        space_count = trim_str.count(' ')
        needed_space = maximum_width - len(trim_str)
        space_str = ' '
        new_space_str = '  '

        while len(trim_str) < maximum_width:
            trim_str = trim_str.replace(space_str, new_space_str, needed_space)
            needed_space = maximum_width - len(trim_str)
            space_str += ' '
            new_space_str += ' '
        print(trim_str)
    else:
        el = el.strip()
        print(el)
