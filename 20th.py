# Open a file and strip whitespace

fileContents = open('mbox-short.txt')
print(fileContents)

for contents in fileContents :
    contentsClean = contents.rstrip()   # Strip whitespace from right side.
#    print(contentsClean)                # Print new variable
    print(contentsClean.upper())        # Convert to all UPPERCASE 
