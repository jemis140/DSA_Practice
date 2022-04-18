###
### You have a word 5 characters long. 
### You also have a set of cubes with one letter on each side of the cube (so 6 letters). 
### Spell the word out using those cubes (if possible) and return which cubes you used to spell it out.
###

# Simple case
cubes = [
  ["a", "i", "p", "q", "x", "q"], # Cube 0
  ["r", "m", "f", "h", "a", "w"], # Cube 1
  ["l", "z", "v", "n", "b", "t"], # Cube 2
  ["r", "m", "o", "f", "a", "r"], # Cube 3
  ["g", "w", "e", "l", "v", "y"], # Cube 4  
]
# Expected output: [0, 1, 3, 2, 4]

# cubes = [
#   ["a", "e", "p", "n", "h", "q"], # Cube 0
#   ["r", "m", "o", "f", "a", "w"], # Cube 1
#   ["r", "h", "n", "f", "a", "r"], # Cube 2
#   ["o", "z", "x", "v", "e", "t"], # Cube 3
#   ["g", "p", "y", "l", "o", "y"], # Cube 4  
# ]
# # Expected output: [4, 0, 1, 2, 3]  or [4, 2, 1, 0, 3]

# cubes = [
#   ["a", "o", "p", "q", "h", "q"], # Cube 0
#   ["r", "m", "o", "f", "a", "w"], # Cube 1
#   ["r", "m", "n", "f", "a", "r"], # Cube 2
#   ["o", "z", "x", "v", "e", "t"], # Cube 3
#   ["g", "p", "n", "l", "o", "y"], # Cube 4  
# ]
# # Expected output: [4, 0, 1, 2, 3]




# Find out if given word can be formed using given curbes
#steps: create map of given word
#create one set for visited cubes 

class Solution:
  
  def findWordFromCubes(self, word):
    
    #set for visited rows
    visited_rows = []

    for w in word:
       for i in range(len(cubes)):
          for j in range(len(cubes[i])):
            if w == cubes[i][j]:
              visited_rows.append(i)
              
    if len(visited_rows) == len(word):
      return visited_rows
    else:
      return []
              

s = Solution()

word = "phone"

print(s.findWordFromCubes(word))