import turtle
import math



class MassObject(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1

    def __init__(self, color, mass, solar_system, position = (0, 0), velocity = (0, 0)):
       super().__init__()
       self.color(color)
       self.mass = mass
       self.position = position
       self.setposition(position)
       self.velocity = velocity
       self.solar_system = solar_system
       self.penup()
       self.hideturtle()

        
       self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
       
       solar_system.addBody(self)


    def draw(self):
        self.clear()
        self.dot(self.display_size)

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])   



    def moonOrbit(self, moon):
        print("x: ",self.xcor())
    
        print("y: ",self.ycor())

            
            


       
        
    
    
        

      
        
    
        
            
      
        

   

         

        
       








        

       