


from os import read


class Object(object):

    def __init__ (self,filename):
        self.vertices =[]
        self.faces=[]

        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.readFile()

    def readFile(self):
        for line in self.lines:
            print(line)


