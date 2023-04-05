import turtle

if __name__ == "__main__":
    screen = turtle.getscreen()
    #sun
    sun = turtle.Turtle()
    
    #moon
    moon = turtle.Turtle()
  
    #earth
    earth = turtle.Turtle()


    #draw masses on screen
    earth.pencolor("blue")
    earth.fillcolor("blue")
    earth.dot(50)

    moon.penup()
    moon.setpos(50, 50)
    moon.fillcolor("#CCCCCC")
    moon.pencolor("#CCCCCC")
    moon.dot(20)

    sun.penup()
    sun.setpos(0, -200)
    sun.pencolor("yellow")
    sun.fillcolor("yellow")
    sun.dot(100)


    #initialize screen
    screen.listen()
    screen.mainloop()
    
