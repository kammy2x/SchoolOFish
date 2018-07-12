

def setup():
    size(400,400)
    background(0,0,255)
    fish(random(255), random(255), random(50,100), random(30,60))
    fish(random(255), random(255), random(50,100), random(10,30))
    fish(random(255), random(255), random(50,100), random(60,80))
    
def fish(xCoordinate, yCoordinate, fWidth, fHeight):
    fill(255, 100, 255)
    ellipse(xCoordinate, yCoordinate, fWidth, fHeight)
    fill(0, 255,250)
    triangle(xCoordinate+fWidth/2, yCoordinate, xCoordinate+fWidth, yCoordinate+fHeight/2, xCoordinate+fWidth, yCoordinate-fHeight)
    ellipse(xCoordinate-20, yCoordinate, 10, 15)
    
fWidth = 50
fHeight = 50
yCoordinate = 50
xCoordinate = 50
yspeed = 2
xspeed = 6

ellipseSize = 50
def setup():
    size(400,400)

def draw():
    k= random(23, 50)
    background(0, 0, 255)
    global xCoordinate, yCoordinate, xspeed, yspeed, ellipseSize, fWidth
    
    leftBoundary = fWidth / 2
    rightBoundary = 400 - fWidth / 2
    topBoundary = fWidth / 2
    bottomBoundary = 400 - fWidth / 2
    xCoordinate += xspeed
    yCoordinate += yspeed
    
    if xCoordinate >= rightBoundary or xCoordinate <= leftBoundary:
        xspeed = -xspeed
        
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
        yspeed = - yspeed
    fill(57, 100, 130)
    fish(xCoordinate, yCoordinate, fWidth, fHeight)
    fish(xCoordinate+50, yCoordinate+50, fWidth, fHeight) 
    fish(xCoordinate-50, yCoordinate+100, fWidth, fHeight)
