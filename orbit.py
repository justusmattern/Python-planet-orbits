import turtle
from turtle import *
from math import sqrt, atan2, cos, sin

speed = 1
AstroUnit = 149.6e6 * 1000
GravConst = 6.67408 * 10**(-11)
day = 24*3600 *speed
scale = 320/AstroUnit
current_month = '/'


class Body(Turtle):
    sc = turtle.Screen()
    sc.bgcolor('#0b0529')


    mass = 0
    v_y = 0
    v_x = 0
    posX = 0
    posY = 0


    def calculateForce(self, other):
        self.deltaX = -self.posX
        self.deltaY = -self.posY
        totalForce = GravConst*self.mass*other.mass/(self.deltaX**2 + self.deltaY**2)

        return totalForce 

    def resultingVelocities(self, force):
        try:
            alpha = atan2(self.deltaY,self.deltaX)
        except ZeroDivisionError:
            alpha=0

        fx = force * cos(alpha)
        fy = force * sin(alpha)

        vx = fx*day/self.mass
        vy = fy*day/self.mass

        return [vx, vy]

def orbit(centerBody, planets):
    while True:
        for planet in planets:
            f = planet.calculateForce(centerBody)
            v = planet.resultingVelocities(f)

            planet.v_x += v[0]
            planet.v_y += v[1]

            planet.posX += planet.v_x*day
            planet.posY += planet.v_y*day

            planet.goto(planet.posX*scale, planet.posY*scale)


def main():
    planets = []

    sun = Body()
    sun.mass = 1.9884*10**30
    sun.shape('circle')
    sun.color('#ffa700')
    sun.shapesize(3)

    earth = Body()
    earth.penup()
    earth.speed(0)
    earth.mass = 5.9722*10**24
    earth.shape('circle')
    earth.shapesize(0.35)
    earth.color('#006bff')
    earth.posX = -AstroUnit
    earth.v_y = -29.783*1000
    earth.goto(earth.posX, earth.posY)
    planets.append(earth)


    mercury = Body()
    mercury.penup()
    mercury.speed(0)
    mercury.mass = 0.33011*10**24
    mercury.shape('circle')
    mercury.shapesize(0.2)
    mercury.color('#edeedd')
    mercury.posY = -AstroUnit * 0.39
    mercury.v_x = 47.3625*1000
    mercury.goto(mercury.posX, mercury.posY)
    planets.append(mercury)


    venus = Body()
    venus.penup()
    venus.speed(0)
    venus.mass = 4.876*10**24
    venus.shape('circle')
    venus.shapesize(0.3)
    venus.color('#eecc3d')
    venus.posY = AstroUnit * 0.723
    venus.v_x = -35.0*1000
    venus.goto(venus.posX, venus.posY)
    planets.append(venus)


    mars = Body()
    mars.penup()
    mars.speed(0)
    mars.mass = 0.639*10**24
    mars.shape('circle')
    mars.shapesize(0.3)
    mars.color('#b05000')
    mars.posX = AstroUnit * 1.5
    mars.v_y = 24.13083*1000
    mars.goto(mars.posX, mars.posY)
    planets.append(mars)

    orbit(sun,planets)

if __name__ == '__main__':
    main()

