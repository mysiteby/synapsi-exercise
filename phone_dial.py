"""
input is through the command line 
'01', '*', '#' buttons are not dialed, entering these buttons will be discarded 
input order supported
any number of inputs available
repeated presses are supported 
"""

dial = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}
output = []

seq = list(input())
seq = [num for num in seq if num not in '01*#']
len_seq = len(seq)

if len_seq == 0: print(output)
if len_seq > 0:
    while len_seq > 0:
        i, *j = seq
        if not output:
            output = [el for el in dial[i]]
        else:
            output = [f+s for s in dial[i] for f in output]
        seq.remove(i)
        len_seq = len(seq)

print(output)
