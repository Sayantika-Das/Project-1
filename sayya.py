f = open('file.txt', 'r')
a = f.readlines()

lineCount = len(a)
print("Line Count:",lineCount)

characterCount = 0

for i in a:
    characterCount = characterCount + len(i)
    
print("Character Count:",characterCount)