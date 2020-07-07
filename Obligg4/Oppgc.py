fil = open("oving3", "r")
a = set()
for line in fil:
    words = line.split(" ")
    line = line.lower()
    for word1 in words:
        word1 = word1.strip(".,:;)«\n")
        a.add(word1)


fil2 = open("oving4", "r")
b = set()
for line in fil2:
    words = line.split(" ")
    line = line.lower()
    for word in words:
        word = word.strip(".,:;)«\n")
        b.add(word)

felles_ord = a.intersection(b)
print(felles_ord)
