"""
saving and reading from file
"""
var1 = 01234
var2 = 56789

class SaveLoadClass:

    def __init__(self):
        print("save class is started")

    def saveToFile(self, fileName):
        file = open(fileName, 'w')
        file.write("version 0.1\n")

        file.write(str(var1) + "\n")
        file.write(str(var2) + "\n")

        print(file)

    def loadFromFile(self, fileName):
        file = open(fileName, 'r')
        print(file.readline())

        var1 = file.readline()
        var2 = file.readline()

        print(file)

