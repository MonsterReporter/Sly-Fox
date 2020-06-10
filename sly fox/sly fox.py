from pygame import mixer
from time import sleep, time
mixer.init()
start = mixer.Sound("start.wav")
start.play()
ouch = mixer.Sound("ouch.wav")
foxw = mixer.Sound("foxw.wav")
yes = mixer.Sound("yes.wav")
foxq = mixer.Sound("untitled.wav")
import pgzrun
WIDTH = 1000
HEIGHT = 1000
OPEN = True
caught1 = 0
caught2 = 0
fox = Actor("fox")
fox.pos = 600, 200
mouse = Actor("mouse")
mouse.pos = 600, 700
skunk = Actor("skunk")
skunk.pos = 400, 700
line = Actor("finish")
line.pos = 500, 300
cheese = Actor("cheese")
cheese.pos = 800, 200
story = Actor("story")
story.pos = 200, 100
def draw():
    screen.fill("green")
    fox.draw()
    mouse.draw()
    skunk.draw()
    line.draw()
    cheese.draw()
    story.draw()
def update():
    if keyboard.space:
        story.image = "no"
        foxq.play(-1)  
    global OPEN, caught1, caught2
    if keyboard.v:
        if OPEN == True:
            fox.image = "fox2"
            OPEN = False
        else:
            fox.image = "fox"
            OPEN = True
    if keyboard.z:
        mouse.y -= 10
        sleep(.5)
    if keyboard.z and OPEN == True:
        mouse.pos = 600, 700
        caught1 += 1
        ouch.play()

    if keyboard.m:
        skunk.y -= 10
        sleep(.5)
    if keyboard.m and OPEN == True:
        skunk.pos = 400, 700
        caught2 += 1
        ouch.play()
    if caught1 == 3:
        mouse.y += 10000
    if caught2 == 3:
        skunk.y += 10000
    if caught1 == 3 and caught2 == 3:
        line.image = "no"
        cheese.image = "no"
        fox.image = "foxs"
        fox.pos = 600, 400
        foxq.stop()
        foxw.play(-1)
    if mouse.colliderect(line):
        line.x += 1000
        cheese.x += 1000
        skunk.x += 1000
        mouse.image = "m"
        fox.x += 1000
        mouse.pos = 600, 400
        foxq.stop()
        yes.play(-1)
    if skunk.colliderect(line):
        line.image = "no"
        cheese.image = "no"
        skunk.image = "no"
        mouse.image = "no"
        fox.image = "skunks"
        fox.pos = 600, 400
        foxq.stop()
        yes.play(-1)
pgzrun.go()    

