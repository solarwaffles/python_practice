class ISBN():
    characters = {"X", "x"}
    counter = 0
    s1 = []
    s2 = []

    def Main(self):
        in_file = open ("./isbn.txt", "r")

        while True:
            isbn = in_file.readline()
            isbn = isbn.strip('\n')

            if not isbn:
                break

            self.s1 = []
            self.s2 = []
            for char in isbn:
                if (self.isChar(self, char) == False):
                    print (isbn + "invalid")
                    self.counter = 0
                    break
            if (len(self.s1) == 10):
                for num in self.s1:
                    self.addList(self.s2, num)
                if (int(self.s2[-1]) % 11 == 0):
                    print (isbn + " valid")
                else:
                    print (isbn + " invalid")
                self.counter = 0

    def isChar(self, x):
        if (x.isnumeric()):
            self.addList(self.s1, x)
            self.counter += 1
            return True
        if (x == "-"):
                return True
        for char in self.characters:
            if ((x == char) and (self.counter == 9)):
                self.counter += 1
                self.addList(self.s1, 10)
                return True
        if not x and self.counter == 10:
            return True
        return False
    
    def addList(list, x):
        if (len(list) > 0):
            list.append(int(x) + int(list[-1]))
        else:
            list.append(x)

Isbn = ISBN
Isbn.Main(Isbn)