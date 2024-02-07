class Work_string:

    def getString(self):
        self.content = str(input()).upper()
    
    def printString(self):
        print(self.content)

x = Work_string()
x.getString()
x.printString()
