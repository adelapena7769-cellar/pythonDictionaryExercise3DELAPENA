fName = input("Enter file name: ")
fHand = open(fName)

counts = dict()

for line in fHand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

print(counts)