import turtle
import math
from solarSystem import SolarSystem
from massObject import MassObject
from moon import Moon


if __name__ == "__main__":
    solarSystem = SolarSystem(1400, 900, 0, 0)

    #massObject(color, mass, solarSystem, position, velocity)
    sun = MassObject("yellow", 20000, solarSystem)
    earth = MassObject("blue", 6, solarSystem, (-470, 0), (0, 5))
    moon = Moon("gray", 10, 45, 1)
    

    while True:
        solarSystem.accelerationDueToGravity(sun, earth)
        moon.move()
        moon.goto(earth.xcor() + moon.orbit_radius * math.cos(math.radians(moon.angle)),
              earth.ycor() + moon.orbit_radius * math.sin(math.radians(moon.angle)))
   
        solarSystem.updateAll()


        

    

    
 
