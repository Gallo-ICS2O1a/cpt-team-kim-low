class Levels():
    
    def __init__(self):
        
        self.levelNumb = 0
        self.currentMap = loadImage("0.png")
       
    def spawn(self):
        for x in range(width):
            for y in range(height):
                    playerObj.position = screen_to_world(PVector(x,y))     
   
    def nextLevel(self):
        try:
            self.levelNumb += 1
            self.currentMap = loadImage(str(self.levelNumb) + ".png")
        
        except: 
            self.levelNumb = 0
            self.currentMap = loadImage(str(self.levelNumb) + ".png")
        self.spawn()
        
    
class Player():
    
    def __init__(self,x,y):
        
        self.position = PVector(x, y)
        self.acceleration = PVector(0,0)
        self.velocity = PVector(0,0)
        self.friction = .9
        self.maxSpeed = 2
        self.accelSpeed = 1
        self.maxJump = 15
        self.playerDimensions = 30
        self.gravity = -.5
        self.collisionArray = [False, False, False, False]
        self.wallFriction = .1
        self.currentJump = 1 
        self.maxJumps = 1
        
    def display(self):
        screenPos = worldPoint_to_screenPoint(self.position)
        
        fill(0)
        rect(int(screenPos.x - self.playerDimensions/2), int(screenPos.y - self.playerDimensions/2), self.playerDimensions, self.playerDimensions)
        
    def applyForce(self,x ,y):
        
        self.acceleration.x += x
        self.acceleration.y += y
    

    def colorCollide(self):
        
        skinWidth = 2
        startR1 = PVector(self.position.x + self.playerDimensions/2 -skinWidth, self.position.y + self.playerDimensions/2 - skinWidth)
        endR1 = PVector(self.position.x + self.playerDimensions/2 + self.velocity.x, self.position.y + self.playerDimensions/2)
        
        startR2 = PVector(self.position.x + self.playerDimensions/2 - skinWidth, self.position.y - self.playerDimensions/2 + skinWidth)
        endR2 = PVector(self.position.x + self.playerDimensions/2 + self.velocity.x, self.position.y - self.playerDimensions/2)
        
        startL1 = PVector(self.position.x - self.playerDimensions/2 + skinWidth, self.position.y + self.playerDimensions/2 - skinWidth)
        endL1 = PVector(self.position.x - self.playerDimensions/2 + self.velocity.x, self.position.y + self.playerDimensions/2)
        
        startL2 = PVector(self.position.x - self.playerDimensions/2 + skinWidth, self.position.y - self.playerDimensions/2 + skinWidth)
        endL2 = PVector(self.position.x - self.playerDimensions/2 + self.velocity.x, self.position.y - self.playerDimensions/2)
       
        startD1 = PVector(self.position.x + self.playerDimensions/2 - skinWidth, self.position.y - self.playerDimensions/2 + skinWidth)
        endD1 = PVector(self.position.x + self.playerDimensions/2, self.position.y - self.playerDimensions/2 + self.velocity.y)
        
        startD2 = PVector(self.position.x - self.playerDimensions/2 + skinWidth, self.position.y - self.playerDimensions/2 + skinWidth)
        endD2 = PVector(self.position.x - self.playerDimensions/2, self.position.y - self.playerDimensions/2 + self.velocity.y)
        
        startU1 = PVector(self.position.x + self.playerDimensions/2 - skinWidth, self.position.y + self.playerDimensions/2 - skinWidth)
        endU1 = PVector(self.position.x + self.playerDimensions/2, self.position.y + self.playerDimensions/2 + self.velocity.y)
        
        startU2 = PVector(self.position.x - self.playerDimensions/2 + skinWidth, self.position.y + self.playerDimensions/2 - skinWidth)
        endU2 = PVector(self.position.x - self.playerDimensions/2, self.position.y + self.playerDimensions/2 + self.velocity.y)
        
        rayAray = []
        
        lineR1 = lineCollision(startR1, endR1, 'h')
        lineR2 = lineCollision(startR2, endR2, 'h')
        
        lineL1 = lineCollision(startL1, endL1, 'h')
        lineL2 = lineCollision(startL2, endL2, 'h')
        
        lineU1 = lineCollision(startU1, endU1, 'v')
        lineU2 = lineCollision(startU2, endU2, 'v')
        
        lineD1 = lineCollision(startD1, endD1, 'v')
        lineD2 = lineCollision(startD2, endD2, 'v')
        
        rayAray.append(lineR1)
        rayAray.append(lineR2)
        rayAray.append(lineL1)
        rayAray.append(lineL2)
        rayAray.append(lineD1)
        rayAray.append(lineD2)
        rayAray.append(lineU1)
        rayAray.append(lineU2)

        self.collisionArray = [False, False, False, False]
        
        if lineU1[0] and lineU1[2] == "Wall":
            self.position.y = lineU1[1].y - self.playerDimensions/2
            self.velocity.y = 0
            self.collisionArray[0] = True
            
        if lineU2[0] and lineU2[2] == "Wall":
            self.position.y = lineU2[1].y - self.playerDimensions/2 
            self.velocity.y = 0
            self.collisionArray[0] = True

            
        if lineD1[0] and lineD1[2] and "Wall":
            self.position.y = lineD1[1].y + self.playerDimensions/2 
            self.velocity.y = 0
            self.collisionArray[1] = True
        if lineD2[0] and lineD2[2] and "Wall":
            self.position.y = lineD2[1].y + self.playerDimensions/2 
            self.velocity.y = 0
            self.collisionArray[1] = True
            
        if lineL1[0] and lineL1[2] == "Wall":
            self.position.x = lineL1[1].x + self.playerDimensions/2 +1
            self.velocity.x = 0
            self.collisionArray[2] = True

        if lineL2[0] and lineL2[2] == "Wall":
            self.position.x = lineL2[1].x + self.playerDimensions/2 +1
            self.velocity.x = 0
            self.collisionArray[2] = True
            
        if lineR1[0] and lineR1[2] == "Wall":
            self.position.x = lineR1[1].x - self.playerDimensions/2 -1
            self.velocity.x = 0
            self.collisionArray[3] = True
        if lineR2[0] and lineR2[2] == "Wall":
            self.position.x = lineR2[1].x - self.playerDimensions/2 -1
            self.velocity.x = 0
            self.collisionArray[3] = True
        
        for line in rayAray:
            if line[0] and line[2] == "Spike":
                levelManager.spawn()
            if line[0] and line[2] == "Door":
                levelManager.nextLevel()
            
    def update(self):
        
        self.applyForce(0,self.gravity)
                
        self.velocity.x *= self.friction
        
        if (self.velocity.y < -1 and (keyArrays[0] or keyArrays[1]) and (self.collisionArray[2] or self.collisionArray[3])):
            self.velocity.y *= self.wallFriction
        
        
       
        if self.collisionArray[1] or  self.collisionArray[2] or  self.collisionArray[3]:
            self.currentJump = self.maxJumps
            
        if keyArrays[0]:
            self.applyForce(-self.accelSpeed, 0)
        if keyArrays[1]:
            self.applyForce(self.accelSpeed,0)
            
        if keyArrays[2] and not self.collisionArray[1] and self.currentJump > 0 and keyArrays[0]:
            self.currentJump -= 1
            self.applyForce(15,15)

        if keyArrays[2] and not self.collisionArray[1] and self.currentJump > 0 and keyArrays[1]:
            self.currentJump -= 1
            self.applyForce(-15,15)
        
        if keyArrays[2] == True and self.currentJump > 0:
            self.currentJump -= 1
            self.velocity.y = 0
            self.applyForce(0,self.maxJump)
                
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
    
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        self.acceleration = PVector(0,0)
            
        self.colorCollide()
        
        keyArrays[2] = False
        self.display()

def lineCollision(startPoint, endPoint, axis): 
    sP = worldPoint_to_screenPoint(startPoint)
    eP = worldPoint_to_screenPoint(endPoint)
    sPx = int(sP.x)
    sPy = int(sP.y)
    ePx = int(eP.x)
    ePy = int(eP.y)
    
    
    if axis == 'h':
        if sPx > ePx:
            for x in range(sPx, ePx,-1):
                c = levelManager.currentMap.get(int(x), sPy)
                
                if c == color(104,255,147):
                    return [True, screen_to_world(PVector(int(x), sPy)), 'Wall']
                if c == color(255,73,79):
                    return [True, screen_to_world(PVector(int(x), sPy)), 'Spike']
                if c == color(255,122,188):
                    return [True, screen_to_world(PVector(int(x), sPy)), 'Door']

        else:
            for x in range(sPx, ePx):
                c = levelManager.currentMap.get(int(x), sPy)

                    
                if c == color(104,255,147):
                    return [True, screen_to_world(PVector(int(x), sPy)),'Wall']
                if c == color(255,73,79):
                    return [True, screen_to_world(PVector(int(x), sPy)), 'Spike']
                if c == color(255,122,188):
                    return [True, screen_to_world(PVector(int(x), sPy)), 'Door']
    else:
        if sPy > ePy:
            for y in range(sPy, ePy, -1):
                c = levelManager.currentMap.get(int(sP.x), int(y))
                
                if c == color(104,255,147):
                    return [True, screen_to_world(PVector(sPx, int(y))), 'Wall']  
                if c == color(255,73,79):
                    return [True, screen_to_world(PVector(sPx, int(y))), 'Spike']  
                if c == color(255,122,188):
                    return [True, screen_to_world(PVector(sPx, int(y))), 'Door']
        else:
            for y in range(sPy, ePy):
                c = levelManager.currentMap.get(int(sP.x), int(y))
                
                if c == color(104,255,147):
                    return [True, screen_to_world(PVector(sPx, int(y))), 'Wall']  
                if c == color(255,73,79):
                    return [True, screen_to_world(PVector(sPx, int(y))), 'Spike']   
                if c == color(255,122,188):
                    return [True, screen_to_world(PVector(sPx, int(y))), 'Door']
                 
    return [False]
        
def screen_to_world(screenPos):
    return PVector((screenPos.x - width/2), -(screenPos.y - height/2))

def worldPoint_to_screenPoint(worldPoints):
    return PVector((width/2 + worldPoints.x),(height/2 - worldPoints.y))

def setup():
    
    fullScreen()
    global levelManager
    levelManager = Levels()
            
    global playerObj
    playerObj = Player(0,0)
    
    global keyArrays
    keyArrays = [False, False, False, False] 
    
    global tempKey
    tempKey = [False, False, False, False]
    
    levelManager.spawn()

def draw():
    frameRate(120)
    
    background(levelManager.currentMap)
    
    playerObj.update()
    
def keyPressed():
    
    if keyCode == LEFT or key == "a" :
        keyArrays[0] = True
    if keyCode == RIGHT or key == "d":
        keyArrays[1] = True
    if keyCode == UP or key == "w" or key == " ":
        keyArrays[2] = True 
        
def keyReleased():
    
    if keyCode == LEFT or key == "a":
        keyArrays[0] = False
    if keyCode == RIGHT or key == "d":
        keyArrays[1] = False
    if keyCode == UP or key == "w" or key == " ":
        keyArrays[2] = False 