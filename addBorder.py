# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
# [input] array.string picture A non-empty array of non-empty equal-length strings.
# [output] array.string
# The same matrix of characters, framed with a border of asterisks of width 1.

def addBorder(picture):
    output = []
    border = ''
    
    for i in range(len(picture[0]) +2):
        border += '*'
    output.append(border)
    for i in range(len(picture)):
        output.append('*' + picture[i] + '*')
    output.append(border)
    return output
        
    
# picture = ["abc","ded"]
# output addBorder(picture) = ["*****","*abc*","*ded*","*****"]