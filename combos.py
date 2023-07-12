class CombineCount:
    def __init__(self, name, number):
        self.name = name
        self.number = number


count = 0
my_list = []
with open("combinations.txt") as fd:
    combos = [lines.strip() for lines in fd]
    for i in combos:
        for j in combos:
            if (i == j):
                count += 1
        my_list.append(CombineCount(i, count))
        count = 0
sortedList = sorted(my_list, key=lambda comb: comb.number)
with open("combosx.txt", 'a') as combosx:
    for x in range(0, len(sortedList)):
        combosx.write(sortedList[x].name + " " +
                      str(sortedList[x].number) + "\n")
        print(str(my_list[x].number) + my_list[x].name)
