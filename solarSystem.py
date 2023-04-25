import turtle
import massObject
import math


class SolarSystem:
    def __init__(self, width, height, x, y):
        self.solar_system = turtle.Screen()
        self.solar_system.setup(width, height, x, y)
        self.bodies = []
        self.solar_system.bgcolor("black")
        self.solar_system.tracer(0)

    def addBody(self, body):
        self.bodies.append(body)

    def updateAll(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()


    @staticmethod
    def accelerationDueToGravity(body1: massObject, body2: massObject):
        dist = body1.distance(body2)
        force = (float(body1.mass) * float(body2.mass)) / dist ** 2
        angle = body1.towards(body2)
        reverse = 1
        for body in body1, body2:
            acceleration = force / body.mass
            acc_x = acceleration * (math.cos(math.radians(angle)))
            acc_y = acceleration * (math.sin(math.radians(angle)))
            body.velocity = (
                body.velocity[0] + (reverse * acc_x),
                body.velocity[1] + (reverse * acc_y)
            )

            reverse = -1

   

    def calculateAllInteractions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.accelerationDueToGravity(first, second) 




   
    
   
        
    
        