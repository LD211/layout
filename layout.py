list = []
print("hi")
with open("english200.txt") as fd:
    englishWords = [line.strip() for line in fd]
    with open("combinations.txt", 'a') as combos:
        for i in range(0, len(englishWords)):
            for j in range(0, len(englishWords[i])-1):
                list.append(englishWords[i][j] + englishWords[i][j+1])
                combos.write(englishWords[i][j] + englishWords[i][j+1] + "\n")
