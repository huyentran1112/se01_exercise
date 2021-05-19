#colors = ["1", "2", "0"]
#size = 3

input('Enter the beaker that you would like to move? ')
def countFree(beaker1):
    beaker1[-1] 
def topColor(beaker1):
    for i in reversed(range(beaker1)):
        if i > 0:
            return i
def colorAmount(beaker1):
    for i in reversed(range(beaker1)):
        y = 0
        if i > 0:
            if i == y: 
                return count(i) in beaker
            else:
                y = i
        else:
            return
def move(beaker1, beaker2):
    if countFree(beaker1) == 0:
        if topColor(beaker1) == topColor(beaker2):
            if colorAmount > 1: 
                beaker2.colors.append(beaker1.colors[-1, -2])
                beaker1.colors.pop()
            print("success")
        else:
            print("error")

    else:
        print("error")


class Beaker:
    def __init__(self, name, colors, size, move):
        self.name = name
        self.colors = colors
        self.size = size
        self.move = move

beaker1 = Beaker("1", [1], 3, move)
beaker2 = Beaker("2", [2, 1, 2], 3, move)
beaker3 = Beaker("3", [2, 1], 3, move)

beaker1.move(beaker1, beaker3)

print(beaker1.name + ":" + string(beaker1.colors))
print(beaker2.name + ":" + string(beaker2.colors))
print(beaker3.name + ":" + string(beaker3.colors))


