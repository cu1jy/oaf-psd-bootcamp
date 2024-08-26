from tkinter import *
from cell import Cell
import settings
import utils

# create window
root = Tk()

#change visuals of window - override settings of window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

topFrame = Frame(
    root,
    width=settings.WIDTH,
    height=utils.heightPct(25)
)
topFrame.place(x=0, y=0)

leftFrame = Frame(
    root,
    width=utils.widthPct(25),
    height=utils.heightPct(75)
)
leftFrame.place(x=0, y=utils.heightPct(25))

centerFrame = Frame(
    root,
    width=utils.widthPct(75),
    height=utils.heightPct(75)
)
centerFrame.place(
    x=utils.widthPct(25),
    y=utils.heightPct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.createButton(centerFrame)
        c.cellButton.grid(
            column=x, row=y
        )

Cell.randomizeMines()

# run window
root.mainloop()
