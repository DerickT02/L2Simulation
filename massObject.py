import turtle

class MassObject():
    def __init__(self, row, col, color, dotsize):
       self.sprite = turtle.Turtle()
       self.color = color
       self.dotsize = dotsize
       self.sprite.penup()
       self.sprite.goto(row,col)

       self.sprite.pencolor(color)
       self.sprite.fillcolor(color)
       self.sprite.dot(dotsize)

    def changePosition(self, row, col):
        self.sprite.clear()
        self.sprite.penup()
        self.sprite.goto(row,col)
        self.sprite.pencolor(self.color)
        self.sprite.fillcolor(self.color)
        self.sprite.dot(self.dotsize)


        

       