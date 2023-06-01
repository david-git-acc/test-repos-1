import random
import pygame
pygame.init()

winWidth = 1000
winHeight = 1000
window = pygame.display.set_mode((winWidth,winHeight))
projectileList = []
objectList = []

pygame.display.set_caption("Secondary test")

shipping = [[pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U1.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U2.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U3.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U4.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U5.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U6.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U7.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U8.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U9.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U10.png"),], [pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D1.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D2.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D3.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D4.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D5.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D6.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D7.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D8.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D9.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D10.png"),], [pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L1.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L2.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L3.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L4.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L5.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L6.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L7.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L8.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L9.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L10.png"),], [pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R1.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R2.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R3.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R4.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R5.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R6.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R7.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R8.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R9.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R10.png"),]]
background = pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/background!.png")
bullet = pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile.png")
bullet2 = pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile2.png")
enemyShip = [pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/U1.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/D1.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/L1.png"),pygame.image.load(r"C:/Users\david\Desktop\Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/R1.png")]

clock = pygame.time.Clock()

def drawWindow():
    window.blit(background,(0,0))

    play.draw(window)

    badguy.draw(window)

    for o in objectList:
        for p in o.projectiles:
            p.draw(window)
        for h in o.horProjectiles:
            h.draw2(window)


    

    pygame.display.update()

class ship():
    def __init__(self,name,width,height,x,y,speed,projectiles,horProjectiles,left,right,up,down,counter):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.projectiles = projectiles
        self.horProjectiles = horProjectiles
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.counter = counter
        self.projectileFrequency = 0
    
class player(ship):
    def __init__(self,name,width,height,x,y,speed,projectiles,left,right,up,down):
        super().__init__("Player ship",64,64,50,50,10,[],[],False,False,True,False,0)


    def draw(self,window):

        self.counter += 1

        self.projectileFrequency += 1

        if self.projectileFrequency == 3:
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
    def __init__(self,name,width,height,x,y,speed,projectiles,left,right,up,down):
        super().__init__("Enemy ship",64,64,50,50,5,[],[],False,False,True,False,0)

    def draw(self,window):
        conditions = [self.up,self.down,self.left,self.right]
        if self.up:
            self.up = True
            self.down = False
            self.left = False
            self.right = False
            window.blit(enemyShip[0], (self.x,self.y))
            if self.y - self.speed - self.height >= 0:
                self.y -= self.speed
            else:
                self.up = False
                conditions[random.randint(0,3)] = True
        if self.down:
            self.up = False
            self.down = True
            self.left = False
            self.right = False
            window.blit(enemyShip[1], (self.x,self.y))
            if self.y + self.speed + self.height <= winHeight:
                self.y += self.speed
            else:
                self.down = False
                conditions[random.randint(0,3)] = True

        if self.left:
            self.up = False
            self.down = False
            self.left = True
            self.right = False
            window.blit(enemyShip[2], (self.x,self.y))
            if self.x - self.speed - self.width >= 0:
                self.x -= self.speed
            else:
                self.left = False
                conditions[random.randint(0,3)] = True
        
            self.up = False
            self.down = False
            self.left = False
            self.right = True
            window.blit(enemyShip[3], (self.x,self.y))
            if self.x + self.speed + self.width <= winWidth:
                self.x += self.speed
            else:
                self.right = False
                conditions[random.randint(0,3)] = True



badguy = enemy(1,1,1,1,1,1,1,1,1,1,1)




class projectile():
    def __init__(self,x,y,side):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 12
        self.speed = 30 * side

    def draw(self,window):
        window.blit(bullet, (self.x,self.y))
        self.y += self.speed
        if self.y > winHeight or self.y < 0:
            play.projectiles.remove(self)


    def draw2(self,window):
        window.blit(bullet2, (self.x,self.y))
        self.x += self.speed
        if self.x > winWidth or self.x < 0:
            play.horProjectiles.remove(self)



        


play = player(1,1,1,1,1,1,1,1,1,1,1)   
objectList.append(play)







running = True
while running:
    clock.tick(67)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        




    drawWindow()


pygame.quit()