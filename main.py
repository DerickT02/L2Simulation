import turtle
from screen import Screen
from massObject import MassObject


if __name__ == "__main__":
    mainScreenObj = Screen()
    mainScreen = mainScreenObj.getScreen()

    sun = MassObject(0, -100, "yellow", 100)
    earth = MassObject(0, 0, "blue", 20)
    earth.changePosition(0, -100)
    mainScreen.mainloop()
