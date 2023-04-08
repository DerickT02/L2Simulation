import turtle
from solarSystem import SolarSystem
from massObject import MassObject


if __name__ == "__main__":
    solarSystem = SolarSystem(1400, 900)
    
    sun = MassObject("yellow", 10000, solarSystem)
    earth = MassObject("blue", 1, solarSystem, (-270, 0), (0, 5))
    moon = MassObject("gray", 0.01, solarSystem, (-272, 0), (0, 4))
    

    while True:
        solarSystem.accelerationDueToGravity(sun, earth)
        solarSystem.accelerationDueToGravity(earth, moon)
        
        solarSystem.updateAll()

    

    
 
