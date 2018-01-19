# Open a file and sort based on criteria

content = open('mbox-short.txt')

for lines in content:
    lines = lines.rstrip()
    filtered = lines.rstrip()

# Guardian
    if len(filtered) < 10 or filtered == '' :
        continue
    print(filtered)
