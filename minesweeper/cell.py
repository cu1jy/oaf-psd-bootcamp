from tkinter import Button
import random
import settings

class Cell:
    all = []

    def __init__(self, x, y, isMine=False) -> None:
        self.isMine = isMine
        self.cellButton = None
        self.x = x
        self.y = y

        # append object to the Cell.all list - so we have all instances of cell class in one place
        Cell.all.append(self)
    
    def createButton(self, location):
        button = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        #assign event
        button.bind('<Button-1>', self.leftClick)
        button.bind('<Button-3>', self.rightClick)
        self.cellButton = button

    def leftClick(self, event):
        if self.isMine:
            self.showMine()
        else:
            self.showCell()
    
    # def showCell(self):
        
    
    def showMine(self):
        # logic to interrupt game and display message that player lost
        self.cellButton.configure(bg='red')


    def rightClick(self, event):
        print(event)
        print("Right clicked!")

    @staticmethod
    def randomizeMines():
        pickedCells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for pickedCell in pickedCells:
            pickedCell.isMine = True

    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"
