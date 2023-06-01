import random
import math
import pygame
pygame.init()


winWidth = 1000
winHeight = 1000
window = pygame.display.set_mode((winWidth,winHeight))
projectileList = []
objectList = []
BOOM = []

pygame.display.set_caption("Secondary test")

shipping = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U10.png"),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D10.png"),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L10.png"),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R10.png"),]]
background = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/background!.png")
bullet = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile.png")
bullet2 = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile2.png")
enemyShip = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/U1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/D1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/L1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/R1.png")]
explosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E9.png")]
shipExplosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS11.png")]
enemyProjectiles = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/verEnemyProjectile.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/horEnemyProjectile.png")]
damageCounterAllied = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/0.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/9.png"),]



clock = pygame.time.Clock()


def drawWindow():
    window.blit(background,(0,0))


    for o in objectList:
        for d in o.damages:
            d.draw(window)
        if o.alreadyCollided >= 1:
            o.alreadyCollided -= 1
        o.draw(window)
        if o.damagedCount > 0:
            trueHealthPercentage = o.health / o.orgHealth 
            try:
                redElement = int(2.55 / trueHealthPercentage ** 8)
            except:
                redElement = 255
            greenElement = int(255 * trueHealthPercentage)        
            pygame.draw.rect(window, (0,0,0), o.healthbar, 1)
            try:
                if 72 <= redElement <= 201:
                    redElement = 201
                pygame.draw.rect(window, (abs(redElement) ,abs(greenElement),0), o.innerBar, 0)
            except:
                try:
                    pygame.draw.rect(window, (255,abs(greenElement),0), o.innerBar, 0)
                except:
                    pass
            o.damagedCount -= 1
        for hit in o.hits:
            if hit.randomCheck == 0:
                hit.randNum = random.randint(10,o.width // 1.2)
                hit.randomCheck = 1
            if hit.randomCheck == 1:
                hit.randNum2 = random.randint(10,o.height // 1.2)
                hit.randomCheck = 2
            if o.left or o.right:        
                hit.x += o.x - hit.x + hit.randNum
                hit.y += o.y - hit.y + hit.randNum2
            if o.up or o.down:
                hit.y += o.y - hit.y + hit.randNum
                hit.x += o.x - hit.x + hit.randNum2
            window.blit(explosion[hit.animCounter//3],(hit.x,hit.y))
            hit.animCounter += 1
            if hit.animCounter >= 24:
                o.hits.remove(o.hits[o.hits.index(hit)])

        for b in BOOM:
            b.draw(window)



        for p in o.projectiles:
            p.draw(window)
        for h in o.horProjectiles:
            h.draw2(window)





    

    pygame.display.update()

class ship():
    def __init__(self,name,width,height,x,y,health,orgHealth,speed,projectiles,horProjectiles,left,right,up,down,counter):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.health = health
        self.orgHealth = orgHealth
        self.speed = speed
        self.projectiles = projectiles
        self.horProjectiles = horProjectiles
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.counter = counter
        self.projectileFrequency = 0
        self.hitbox = (self.x,self.y,regularHitboxValueX,regularHitboxValueY)
        self.healthbar = (self.x+1,self.y-0.2*self.height,20,20)
        self.hitCoordinatesCheck = 0
        self.hitCheck = 0
        self.explosionAnimationCounter = 0
        self.hits = []
        self.damagedCount = 0
        self.enraged = 0
        self.target = 0
        self.aiCounter = 0
        self.countingMechanism = 0
        self.attackTimer = 40
        self.runTimer = 0
        self.afkTimer = 70
        self.enemyMemoryX = 0
        self.enemyMemoryY = 0
        self.afkTimeDelay = 0
        self.suicideAttack = 0
        self.suicideAcceleration = 1.0125
        self.randomNum = 0
        self.alreadyCollided = 0
        self.damages = []
        
regularHitboxValueX = 64
regularHitboxValueY = 64 
class player(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,speed,projectiles,left,right,up,down):
        super().__init__("Player ship",64,64,50,50,100,100,10,[],[],False,False,True,False,0)


    def draw(self,window):
        tupleEvasion = self.healthbar[2] - 2
        trueHealthPercentage = self.health / self.orgHealth 
        self.healthbar = (self.x + self.width / 4,self.y-0.2*self.height,self.width / 2,self.height / 8)
        self.innerBar = (self.healthbar[0] + 1, self.healthbar[1] + 1, tupleEvasion * trueHealthPercentage, self.healthbar[3] - 2)
        self.hitbox = (self.x,self.y,64,64)

        self.counter += 1

        self.projectileFrequency += 1

        if self.projectileFrequency == 5:
            self.projectileFrequency = 0

    



        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.projectileFrequency == 0:
            player.fireGuns(self)

        if keys[pygame.K_UP]:
            window.blit(shipping[0][self.counter], (self.x,self.y))
            if self.y - self.speed >= 0:
                self.y -= self.speed
            self.left = False
            self.right = False
            self.down = False
            self.up = True
        
        elif keys[pygame.K_DOWN]:
            window.blit(shipping[1][self.counter], (self.x,self.y))
            if self.y + self.speed + self.height <= winHeight:
                self.y += self.speed
            self.left = False
            self.right = False
            self.down = True
            self.up = False

        elif keys[pygame.K_LEFT]:
            window.blit(shipping[2][self.counter], (self.x,self.y))
            if self.x - self.speed >= 0:
                self.x -= self.speed
            self.left = True
            self.right = False
            self.down = False
            self.up = False

        elif keys[pygame.K_RIGHT]:
            window.blit(shipping[3][self.counter], (self.x,self.y))
            if self.x + self.width + self.speed <= winWidth:
                self.x += self.speed
            self.left = False
            self.right = True
            self.down = False
            self.up = False

        else:
            conditions = [self.up,self.down,self.left,self.right]
            window.blit(shipping[[conditions.index(c) for c in conditions if c][0]][self.counter], (self.x,self.y))


        if self.counter + 1 >= 10:
            self.counter = 0

    def fireGuns(self):  
        value = 8
        value2 = 18
        if len(self.projectiles) + len(self.horProjectiles) <= 4:
            if self.up:
                proj = projectile(play.x + value ,play.y + value, -1)
                proj2 = projectile(play.x + self.width - 1 - value, play.y + value, -1)
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
            elif self.down:
                proj = projectile(play.x + value, play.y + self.height - 2.5 * value, 1)
                proj2 = projectile(play.x + self.width - value - 1, play.y + self.height - 2.5 * value, 1)
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
            elif self.left:
                proj = projectile(play.x + value, play.y + value, -1)
                proj2 = projectile(play.x + value, play.y + self.height - value - 1, -1 )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
            else:
                proj = projectile(play.x + self.width - value2 - 1, play.y + value, 1)
                proj2 = projectile(play.x + self.width - value2 - 1, play.y + self.height - value - 1, 1 )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)

            projectileList.append(proj)
            projectileList.append(proj2)


class enemy(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,speed,projectiles,left,right,up,down):
        super().__init__("Enemy ship",64,64,random.randint(50,600),random.randint(50,600),500,500,5,[],[],False,False,True,False,0)

    def draw(self,window):
        conditions = [self.up,self.down,self.left,self.right]
        tupleEvasion = self.healthbar[2] - 2
        trueHealthPercentage = self.health / self.orgHealth 
        self.healthbar = (self.x + self.width / 4,self.y-0.2*self.height,self.width / 2,self.height / 8)
        self.innerBar = (self.healthbar[0] + 1, self.healthbar[1] + 1, tupleEvasion * trueHealthPercentage, self.healthbar[3] - 2)
        for o in objectList:
            allegianceCheck = isinstance(o,enemy)
            if not allegianceCheck:
                pythagDistance = math.hypot(o.x - self.x, o.y - self.y)
            try:
                if not allegianceCheck and pythagDistance < 1000 and self.enraged != 1:
                    self.target = objectList[objectList.index(o)]
                    self.enraged = 1
                    break
            except:
                pass

        self.hitbox = (self.x,self.y,regularHitboxValueX,regularHitboxValueY)
                
        if conditions[2]:
            window.blit(enemyShip[2], (self.x,self.y))
        elif conditions[3]:
            window.blit(enemyShip[3], (self.x,self.y))
        elif conditions[0]:
            window.blit(enemyShip[0], (self.x,self.y))
        elif conditions[1]:
            window.blit(enemyShip[1], (self.x,self.y))

        if self.health / self.orgHealth <= 0.2 and self.suicideAttack == 0 and self.alreadyCollided == 0:
            self.speed -= self.speed / 2.4
            self.suicideAttack = 1




        for o in objectList:
            if o != self and self.suicideAttack != 1:
                actualDistanceFromTarget = math.hypot(o.x-self.x,o.y-self.y)
                if actualDistanceFromTarget <= self.width + 38 and self.runTimer == 0:
                    self.runTimer = 9
                if self.runTimer >= 1:
                    self.runTimer -= 1
                    if self.randomNum == 0:
                        self.randomNum = random.randint(1,3)
                    if o.x > self.x:
                        if self.randomNum == 1:
                            self.left = True
                            self.down = False
                            self.up = False
                            self.right = False
                            if self.x - self.speed >= 0:
                                self.x -= self.speed
                            else:
                                self.randomNum = 0

                        elif self.randomNum == 2:
                            self.left = False
                            self.down = True
                            self.up = False
                            self.right = False
                            if self.y + self.speed + self.height <= winHeight:
                                self.y += self.speed
                            else:
                                self.randomNum = 0
                        else:
                            self.up = True
                            self.down = False
                            self.left = False
                            self.right = False
                            if self.y - self.speed >= 0:
                                self.y -= self.speed
                            else:
                                self.randomNum = 0
                        return
                    elif o.x < self.x:# and abs(o.y - self.y) <= abs(o.x - self.x): #ENEMY IS TO THE LEFT
                        if self.randomNum == 1:
                            self.left = False
                            self.down = False
                            self.up = False
                            self.right = True
                            if self.x + self.speed  + self.width <= winWidth:
                                self.x += self.speed
                            else:
                                self.randomNum = 0

                        elif self.randomNum == 2:
                            self.left = False
                            self.down = True
                            self.up = False
                            self.right = False
                            if self.y + self.speed + self.height <= winHeight:
                                self.y += self.speed
                            else:
                                self.randomNum = 0
                        else:
                            self.up = True
                            self.down = False
                            self.left = False
                            self.right = False
                            if self.y - self.speed >= 0:
                                self.y -= self.speed
                            else:
                                self.randomNum = 0
                        return

                    elif o.y < self.y:# and abs(o.y - self.y) >= abs(o.x - self.x): #ABOVE
                        if self.randomNum == 1:
                            self.left = True
                            self.down = False
                            self.up = False
                            self.right = False
                            if self.x - self.speed >= 0:
                                self.x -= self.speed
                            else:
                                self.randomNum = 0

                        elif self.randomNum == 2:
                            self.left = False
                            self.down = True
                            self.up = False
                            self.right = False
                            if self.y + self.speed + self.height <= winHeight:
                                self.y += self.speed
                            else:
                                self.randomNum = 0
                        else:
                            self.up = False
                            self.down = False
                            self.left = False
                            self.right = True
                            if self.x + self.speed + self.width <= winWidth:
                                self.x += self.speed
                            else:
                                self.randomNum = 0
                        return
                    elif o.y > self.y:# and abs(o.y - self.y) >= abs(o.x - self.x): #BELOW
                        if self.randomNum == 1:
                            self.left = True
                            self.down = False
                            self.up = False
                            self.right = False
                            if self.x - self.speed >= 0:
                                self.x -= self.speed
                            else:
                                self.randomNum = 0

                        elif self.randomNum == 2:
                            self.left = False
                            self.down = False
                            self.up = True
                            self.right = False
                            if self.y - self.speed - self.height >= 0:
                                self.y -= self.speed
                            else:
                                self.randomNum = 0
                        else:
                            self.up = False
                            self.down = False
                            self.left = False
                            self.right = True
                            if self.x + self.speed + self.width <= winWidth:
                                self.x += self.speed
                            else:
                                self.randomNum = 0
                        return
                else:
                    self.randomNum = 0
                    
        if self.afkTimer == 70:
            try:
                self.enemyMemoryX = self.target.x
                self.enemyMemoryY = self.target.y
                self.afkTimer = 69
            except:
                pass
        try:
            if self.enemyMemoryX == self.target.x and self.enemyMemoryY == self.target.y and self.afkTimer > 0:
                self.afkTimer -= 1
            if self.enemyMemoryX != self.target.x or self.enemyMemoryY != self.target.y:
                self.afkTimer = 70
        except:
            pass

        if self.afkTimer == 0 and self.target in objectList and self.suicideAttack != 1:
            enemy.fireGuns(self,self.target)
            
        if self.suicideAttack == 1:
            number = 3.5 / self.suicideAcceleration
            if random.randint(1,10) < 3.5 * self.speed / number:
                self.hits.append(explosionEffect(random.randint(10,self.width // 1.2),random.randint(10,self.height // 1.2)))
            self.suicideNum1 = 0
            self.suicideNum2 = 0
            self.speed = self.speed * self.suicideAcceleration
            if self.target.x > self.x + 25:
                self.x += self.speed
                self.up = False
                self.right = True
                self.down = False
                self.left = False
            elif self.target.x < self.x - 25:
                self.x -= self.speed
                self.up = False
                self.right = False
                self.down = False
                self.left = True
            elif self.target.y > self.y + 25:
                self.y += self.speed
                self.up = False
                self.right = False
                self.down = True
                self.left = False
            elif self.target.y < self.y - 25:
                self.y -= self.speed
                self.up = True
                self.right = False
                self.down = False
                self.left = False



        if self.target not in objectList:
            self.enraged = 0
            self.suicideAttack = 0


        if self.runTimer <= 1 and self.suicideAttack != 1:
            try:
                if self.target.x + 35 > self.x and self.target.x - 35 < self.x:
                    if self.target.y > self.y + 200:
                        self.down = True
                        self.right = False
                        self.left = False
                        self.up = False
                        enemy.fireGuns(self,self.target)
                    if self.target.y < self.y - 200:
                        self.down = False
                        self.right = False
                        self.left = False
                        self.up = True
                        enemy.fireGuns(self,self.target)
                elif self.target.y + 35 > self.y and self.target.y - 35 < self.y:
                    if self.target.x > self.x + 200:
                        self.down = False
                        self.right = True
                        self.left = False
                        self.up = False
                        enemy.fireGuns(self,self.target)
                    if self.target.x < self.x - 200:
                        self.down = False
                        self.right = False
                        self.left = True
                        self.up = False
                        enemy.fireGuns(self,self.target)
                else:
                    pass
            except:
                pass
   


    def fireGuns(self, target):
        tupleEvasion = self.healthbar[2] - 2
        trueHealthPercentage = self.health / self.orgHealth 
        self.healthbar = (self.x + self.width / 4,self.y-0.2*self.height,self.width / 2,self.height / 8)
        self.innerBar = (self.healthbar[0] + 1, self.healthbar[1] + 1, tupleEvasion * trueHealthPercentage, self.healthbar[3] - 2)
        self.hitbox = (self.x,self.y,regularHitboxValueX,regularHitboxValueY)
        if self.left:
            window.blit(enemyShip[2], (self.x,self.y))
            self.up = False
            self.down = False
            self.right = False
        elif self.right:
            window.blit(enemyShip[3], (self.x,self.y))
            self.left = False
            self.up = False
            self.down = False
        elif self.up:
            window.blit(enemyShip[0], (self.x,self.y))
            self.left = False
            self.right = False
            self.down = False

        else:
            window.blit(enemyShip[1], (self.x,self.y))
            self.up = False
            self.left = False
            self.right = False

        

        self.attackTimer -= 1

        self.afkTimeDelay += 1

        if self.afkTimeDelay == 10:
            self.afkTimeDelay = 0

        if self.afkTimer == 0 and self.runTimer == 0:    
            if target.y + 25 > self.y and target.y - 25 < self.y:
                if target.x > self.x:
                    self.left = False
                    self.right = True
                    self.up = False
                    self.down = False
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x + self.width, self.y + self.height / 2, 1)
                        self.horProjectiles.append(spaceBullet)
                if target.x < self.x:
                    self.left = True
                    self.right = False
                    self.up =  False
                    self.down = False
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x, self.y+ self.height / 2, -1)
                        self.horProjectiles.append(spaceBullet)

                try:
                    projectileList.append(spaceBullet)
                except:
                    pass
            elif target.x + 25 > self.x and target.x - 25 < self.x:
                if target.y > self.y:
                    self.left = False
                    self.right = False
                    self.up = False
                    self.down = True 
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height, 1)
                        self.projectiles.append(spaceBullet)
                if target.y < self.y:
                    self.left = False
                    self.right = False
                    self.up = True
                    self.down = False
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y, -1)
                        self.projectiles.append(spaceBullet)
                try:
                    projectileList.append(spaceBullet)
                except:
                    pass
            else:
                if target.x > self.x:# and abs(o.y - self.y) < abs(o.x - self.x):
                    if target.y + 25 > self.y and target.y - 25 < self.y:
                        pass
                    else:
                        self.x += self.speed
                        self.right = True
                        self.left = False
                        self.up = False
                        self.down = False
                elif target.x < self.x:# and abs(o.y - self.y) < abs(o.x - self.x):
                    if target.y + 25 > self.y and target.y - 25 < self.y:
                        pass
                    else:
                        self.x -= self.speed
                        self.right = False
                        self.left = True
                        self.up = False
                        self.down = False
                elif target.y > self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                    if target.x + 25 > self.x and target.x - 25 < self.x:
                        pass
                    else:
                        self.y += self.speed
                        self.right = False
                        self.left = False
                        self.up = False
                        self.down = True
                elif target.y < self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                    if target.x + 25 > self.x and target.x - 25 < self.x:
                        pass
                    else:
                        self.y -= self.speed
                        self.right = False
                        self.left = False
                        self.up = True
                        self.down = False


                





                


        if self.attackTimer <= 0:
            self.attackTimer = 40



        if self.afkTimer > 0:
            if target.y + 25 > self.y and target.y - 25 < self.y:

                if target.x > self.x + 200:
                    self.x += self.speed
                    if self.attackTimer == 39:
                        spaceBullet = enemyProjectile(self.x + self.width, self.y + self.height / 2, 1)
                        self.horProjectiles.append(spaceBullet)
                    if self.attackTimer == 19:
                        spaceBullet = enemyProjectile(self.x + self.width, self.y + self.height / 2, 1)
                        self.horProjectiles.append(spaceBullet)

                if target.x < self.x - 200:
                    self.x -= self.speed
                    if self.attackTimer == 39:
                        spaceBullet = enemyProjectile(self.x, self.y+ self.height / 2, -1)
                        self.horProjectiles.append(spaceBullet)
                    if self.attackTimer == 19:
                        spaceBullet = enemyProjectile(self.x, self.y + self.height / 2, -1)
                        self.horProjectiles.append(spaceBullet)

            if target.x + 25 > self.x and target.x - 25 < self.x:

                if target.y > self.y + 200:
                    self.y += self.speed
                    if self.attackTimer == 39:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, 1)
                        self.projectiles.append(spaceBullet)
                    if self.attackTimer == 19:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, 1)
                        self.projectiles.append(spaceBullet)

                if target.y < self.y - 200:
                    self.y -= self.speed
                    if self.attackTimer == 39:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, -1)
                        self.projectiles.append(spaceBullet)
                    if self.attackTimer == 19:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, -1)
                        self.projectiles.append(spaceBullet)
            try:
                projectileList.append(spaceBullet)
            except:
                pass

                
    

        






class enemyProjectile():
    def __init__(self,x,y,side):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 12
        self.speed = 15 * side
        self.damage = 0
        self.owner = "Enemy ship"

    def draw(self,window):
        window.blit(enemyProjectiles[0], (self.x,self.y))
        self.y += self.speed
        if self.y > winHeight or self.y < 0:
            try:
                projectileList.remove(self)
            except:
                pass
        if self not in projectileList:
            try:
                for o in objectList:
                    if self in o.projectiles:
                        o.projectiles.remove(self)
            except:
                pass

    def draw2(self,window):
        window.blit(enemyProjectiles[1], (self.x,self.y))
        self.x += self.speed
        if self.x > winWidth or self.x < 0:
            try:
                projectileList.remove(self)
            except:
                pass
        if self not in projectileList:
            try:
                for o in objectList:
                    if self in o.horProjectiles:
                        o.horProjectiles.remove(self)
            except:
                pass

        

class explosionEffect():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.animCounter = 0
        self.randomCheck = 0
        self.randNum = 0
        self.randNum2 = 0


class shipExploding():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.boomCycle = 0

    def draw(self,window):
        if len(objectList) >= 2:
            window.blit(shipExplosion[self.boomCycle//9], (self.x,self.y))
            self.boomCycle += 1
            if self.boomCycle >= 90:
                BOOM.remove(self)
        else:
            try:
                window.blit(shipExplosion[self.boomCycle//3], (self.x,self.y))
                self.boomCycle += 1
                if self.boomCycle >= 30:
                    BOOM.remove(self)
            except:
                pass

class damage():
    def __init__(self,damageCaused,responsibleProjectile,damageOwner,damageOwnerX):
        self.y = 0
        self.damageCaused = damageCaused
        self.responsibleProjectile = responsibleProjectile
        self.damageOwner = damageOwner
        self.damageOwnerX = damageOwnerX
        self.distance = 0
        self.gap = 0
    


    def draw(self,window):
        for o in objectList:
            if self in o.damages:
                self.distance = o.damages.index(self) + 1      
        if self.damageOwnerX == 1:
            window.blit(damageCounterAllied[self.damageCaused], (self.damageOwner.x+8.1 + self.damageOwner.width * 0.85,self.damageOwner.y + self.y - 15 * self.distance))
        else:
            window.blit(damageCounterAllied[self.damageCaused], (self.damageOwner.x + self.damageOwner.width * 0.85,self.damageOwner.y + self.y - 15 * self.distance))
        self.y -= 0.5
        if self.y < -20:
            self.damageOwner.damages.remove(self)






class projectile():
    def __init__(self,x,y,side):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 12
        self.speed = 30 * side
        self.damage = 2
        self.owner = "Player ship"

    def draw(self,window):
        window.blit(bullet, (self.x,self.y))
        self.y += self.speed
        if self.y > winHeight or self.y < 0:
            try:
                play.projectiles.remove(self)
                projectileList.remove(self)
            except:
                pass
        if self not in projectileList:
            try:
                play.projectiles.remove(self)
            except:
                pass


    def draw2(self,window):
        window.blit(bullet2, (self.x,self.y))
        self.x += self.speed
        if self.x > winWidth or self.x < 0:
            try:
                play.horProjectiles.remove(self)
                projectileList.remove(self)
            except:
                pass
        if self not in projectileList:
            try:
                play.horProjectiles.remove(self)
            except:
                pass



        
play = player(1,1,1,1,1,1,1,1,1,1,1,1,1)  
objectList.append(play) 





print("Your object list contains" , objectList)


running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    noDuplicates = 0
    count = 0
    count2 = 0
    for o in objectList:
        if isinstance(o,enemy):
            count += 1
        if isinstance(o, player):
            count2 += 1

    if count == 0:
        for x in range(1):
            objectList.append(enemy(1,1,1,1,1,1,1,1,1,1,1,1,1))

    if count2 == 0:
        play = player(1,1,1,1,1,1,1,1,1,1,1,1,1)
        objectList.append(play)


        

    for o in objectList:
        if o.health <= 0:
            BOOM.append(shipExploding(o.x,o.y))
            objectList.remove(o)  


    for p in projectileList:
        for o in objectList:    
            if p.x > o.hitbox[0] and p.x < o.hitbox[2] + o.x and p.owner != o.name:
                if p.y > o.hitbox[1] and p.y < o.y + o.hitbox[3] and p not in o.projectiles and p not in o.horProjectiles:
                    try:
                        projectileList.remove(p)
                        if p.damage > 0:
                            o.health -= p.damage
                            o.damagedCount = 130    
                            for c in str(p.damage):
                                if len(str(p.damage)) == 2 and noDuplicates == 0:
                                    damageNumber = damage(int(str(p.damage)[0]),p.owner,o,0)
                                    o.damages.append(damageNumber)
                                    damageNumber = damage(int(str(p.damage)[1]),p.owner,o,1)
                                    o.damages.append(damageNumber)
                                    noDuplicates = 1



                                elif len(str(p.damage)) != 2 and noDuplicates == 0:
                                    damageNumber = damage(int(c),p.owner,o,0)
                                    o.damages.append(damageNumber)
                                    noDuplicates = 1
                                        



                        o.hits.append(explosionEffect(p.x,p.y))
                    except:
                        pass

    for ob in objectList:
        for otherOb in objectList:
            if ob.x + ob.width / 2 > otherOb.hitbox[0] and ob.x < otherOb.hitbox[2] + otherOb.x and ob is not otherOb: 
                if ob.y  + ob.height / 2 > otherOb.hitbox[1] and ob.y < otherOb.y + otherOb.hitbox[3]:
                    if ob.suicideAttack == 1 and ob.alreadyCollided <= 0:
                        ob.health -= ob.orgHealth / 1.5
                        ob.health -= 35
                        otherOb.health -= otherOb.orgHealth / 1.5
                        otherOb.health -= 35
                        ob.damagedCount = 130
                        otherOb.damagedCount = 130
                    elif otherOb.suicideAttack == 1 and otherOb.alreadyCollided <= 0:
                        ob.health -= ob.orgHealth / 1.5
                        ob.health -= 35
                        otherOb.health -= otherOb.orgHealth / 1.5
                        otherOb.health -= 35
                        ob.damagedCount = 130
                        otherOb.damagedCount = 130
                    else:
                        o.runTimer += 4
                        ob.alreadyCollided = 45
                        totalHp = ob.orgHealth + otherOb.orgHealth
                        ob.health -= totalHp // 54
                        ob.damagedCount = 130
                        otherOb.damagedCount = 130
                        otherOb.health -= totalHp // 54
                    
                    for x in range(2):
                        ob.hits.append(explosionEffect(ob.x,ob.y))
                        otherOb.hits.append(explosionEffect(otherOb.x,otherOb.y))
                




    noDuplicates = 0


        




    drawWindow()


pygame.quit()