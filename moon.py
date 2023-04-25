import turtle
import math

class Moon(turtle.Turtle):
    def __init__(self, color, size, orbit_radius, orbit_speed):
        super().__init__()
        self.dot(size, color)
        self.penup()
        self.hideturtle()
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.size = size
        self.angle = 0
        self.color = color

    def move(self):
        # Calculate new x, y coordinates based on the orbit radius and angle
        self.clear()
        self.dot(self.size, self.color)
        x = self.orbit_radius * math.cos(math.radians(self.angle))
        y = self.orbit_radius * math.sin(math.radians(self.angle))

        # Move to the new coordinates
        self.goto(x, y)

        # Increment the angle to move in the orbit
        self.angle += self.orbit_speed