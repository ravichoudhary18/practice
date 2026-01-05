class mian:
    
    def __init__(self) -> None:
        self.text_input = ''
    

    def getString(self) -> None:
        self.text_input = input("Enter text: ")
    
    def printString(self):
        if self.text_input:
            print("Upper test is: ", self.text_input.upper())



strObj = mian()
strObj.getString()
strObj.printString()