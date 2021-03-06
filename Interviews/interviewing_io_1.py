"""
Given three rows of characters representing a keyboard and a word, by moving only once at a time to adjacent keys 
{up, down, left, right}, record the key strokes required to fully spell out the word. An 'E' is entered at each 
character of the given word to denote an 'Enter' stroke. You always begin your traversal from character 'A' on 
the keyboard. The characters 'U', 'D', 'L', 'R' represents each direction you may move. Return the string that
represents every movement required to spell out the given word.

E.g.

"BAT" -> "RELEDDE"

Notes:
> The directions you can go in are U, D, L, R and you have E for #enter. Any path is okay as long as it works.
> You start at letter A and you try to spell out a word. 
"""


# A = [0][0]
# B = [0][1]
# i = {0..9}
# key_table = {
#    "A" : (0,0),
# .  "B" : (0,1),
# }
# keyboard = [
#     [A B C D E F G H I J],
#     [K L M N O P Q R S _],
#     [T U V W X Y Z _ _ _]
# ]

"""
1) initialize keyboard
2) create key_table
-> index 0 corresponds to {U, D}
-> index 1 corresponds to {L, R}
3) return as a string
"""

# Time complexity: O(N)
# Space complexity: O(N)
def keyboard_steps(word : str) -> str:
    
    keyboard = [
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "_"],
        ["T", "U", "V", "W", "X", "Y", "Z", "_", "_", "_"]
    ]
    
    key_table = {}
    for i, row in enumerate(keyboard):
        for j, char in enumerate(row):
            key_table[char] = (i, j)

    steps = []
    word = word
    position = [0, 0]
    
    for i in range(len(word)):
        diff_y = key_table[word[i]][0] - position[0]
        diff_x = key_table[word[i]][1] - position[1]
        position[0] = key_table[word[i]][0]
        position[1] = key_table[word[i]][1]
        
        if diff_x > 0:
            steps.append(diff_x*"R")
        else:
            steps.append(abs(diff_x)*"L")
        
        if diff_y > 0:
            steps.append(diff_y*"D")
        else:
            steps.append(abs(diff_y)*"U")
            
        steps.append("E")
    
    return "".join(steps)
