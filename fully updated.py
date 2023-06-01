import random
import math
import copy
import pygame  #Importing necessary modules
pygame.mixer.pre_init(frequency=44100, size=-16, channels=8, buffer=51200000)
pygame.init()

def loadify(imgname):
    return pygame.image.load(imgname).convert_alpha()



count = 1 #This variable makes sure that all ship explosions have the same animation duration, as well as tracking the number of enemies
minerCount = 0 #Keeps track of the number of miners, so that the number of mines doesn't go over 4 times the overall number of miners
criticalStrike = 0 #Checks whether a given strike is a critical hit or not
winWidth = 1920 #Screen sizes
winHeight = 1080
#window = pygame.display.set_mode((winWidth,winHeight))
from pygame.locals import *

flags = FULLSCREEN | DOUBLEBUF | HWSURFACE
window = pygame.display.set_mode((winWidth,winHeight),flags,8)
projectileList = [] #Tracks all projectiles
objectList = [] #Tracks all objects
powerUpList = [] #Tracks all powerups
buffList = [] # Tracks all buffs
BOOM = [] #Tracks all explosions
mineList = [] #...
healthCall = 0 #tracks which ship will go for health boost
score = 0#853223000
enemyKills = 0
minerKills = 0
frigateKills = 0
spacing = 30
currentLives = 3
lifeSpacing = 58
purchasingTimeDelay = 5
purchasingTimeDelayTimer = 0
stationSpacing = 100

enemyChoice = 1
alliedChoice = 0

alliedTeam = ["Player ship" , "Friendly"]
enemyTeam = ["Enemy ship","EnemyS"]

upgrades = [0,0,0,0,0,0]



pygame.display.set_caption("Secondary test")

f = open("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/gamesave.txt","r+")
text = str(f.readline())
print(text)
if text == "":
    f.write("0")
    highScore = 0
else:
    try:
        highScore = int(text)
    except:
        highScore = 0 

f.close()




#These are the sprite images loaded from the Computer
shipping = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U10.png").convert_alpha(),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D10.png").convert_alpha(),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L10.png").convert_alpha(),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R10.png").convert_alpha(),]]
shippingInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Uinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Dinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Linvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Rinvis.png").convert_alpha(),]
background = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/background2.jpg").convert_alpha()
scoreground = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/ScoreTest2.png").convert_alpha()
purchasesBlit = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/possiblePurchases.png").convert_alpha()
purchasesUsed = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/purchases/annoraxAFT.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/purchases/BuffsAFT.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/purchases/HealthAFT.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/purchases/InvisAFT.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/purchases/FireAFT.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/purchases/AmplifyAFT.png").convert_alpha(),]
bullet = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile.png").convert_alpha()
bullet2 = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile2.png").convert_alpha()
bullet3 = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile3.png").convert_alpha()
bullet4 = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile4.png").convert_alpha()
enemyShip = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U17.png")],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S17.png")],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L17.png")],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R17.png")]]
enemyShipInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Uinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Sinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Linvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Rinvis.png").convert_alpha(),]
explosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E9.png")]
shipExplosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS11.png")]
largerExplosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE9.png").convert_alpha(),]
enemyProjectiles = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/verEnemyProjectile.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/horEnemyProjectile.png")]
fighterProjectiles = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FPH.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FPU.png").convert_alpha(),]
damageCounterAllied = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/0.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/10.png")]
minerBlit = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L15.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R15.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U15.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S15.png").convert_alpha(),]]
minerBlitInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Sinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Uinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Linvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Rinvis.png").convert_alpha(),]
mineBlitStill = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb.png").convert_alpha()
mineBlitAnim = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb13.png").convert_alpha(),]
mineBlitBlink = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bombBlink.png").convert_alpha()
health = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h52.png").convert_alpha(),]
invis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i52.png").convert_alpha(),]
firePower = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f52.png").convert_alpha(),]
fireProjectile = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPU.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPS.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPL.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPR.png")]
amplify = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplify/a52.png").convert_alpha(),]
amplifyActivated = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/amplifyActivated/a52.png").convert_alpha(),]
friendlyStation = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS17.png").convert_alpha(),]
shields = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU25.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR25.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD25.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL25.png").convert_alpha(),],]
shieldsUA = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldUpUA.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldRightUA.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldDownUA.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldLeftUA.png").convert_alpha(),]
torpedoAnimation = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST19.png").convert_alpha(),]
enemyTorpAnimation = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET19.png").convert_alpha(),]
rocketAnimation = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU23.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR23.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS23.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL23.png").convert_alpha(),]]
scoreCounter = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b0.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b9.png").convert_alpha(),]
livesRemaining = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/lives.png").convert_alpha()
healthyActivated = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h52.png").convert_alpha(),]
invisActivated = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i52.png").convert_alpha(),]
fireActivated = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f28.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f29.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f30.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f31.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f32.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f33.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f34.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f35.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f36.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f37.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f38.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f39.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f40.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f41.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f42.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f43.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f44.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f45.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f46.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f47.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f48.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f49.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f50.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f51.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f52.png").convert_alpha(),]
annorax = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL17.png").convert_alpha(),]]
annoraxInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/up.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/right.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/down.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/left.png").convert_alpha(),]
frigateAnim = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL17.png").convert_alpha(),]]
frigateInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRUinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRRinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRDinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRLinvis.png").convert_alpha(),]
beamAnim = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BU1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BU2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BU3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BU4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BU5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BU6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BU7.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BR1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BR2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BR3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BR4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BR5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BR6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BR7.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BD1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BD2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BD3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BD4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BD5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BD6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BD7.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BL1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BL2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BL3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BL4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BL5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BL6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/beam/BL7.png").convert_alpha(),],]
reinforcementsBlit = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/RB28.png").convert_alpha(),]
healthBuffBlit = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/HB28.png").convert_alpha(),]
scoreBlit = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB17.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB18.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB19.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB20.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB21.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB22.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB23.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB24.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB25.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB26.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB27.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/buffs/SB28.png").convert_alpha(),]
fighterBlit = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIU17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIR17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FID17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/FIL17.png").convert_alpha(),],]
fighterInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/fighterInvis/FIUinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/fighterInvis/FIRinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/fighterInvis/FISinvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/fighter/fighterInvis/FILinvis.png").convert_alpha(),]
carrierBlit = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAU17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAR17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAD17.png").convert_alpha(),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/CAL17.png").convert_alpha(),],]
carrierInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/carrierInvis/CAUInvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/carrierInvis/CARInvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/carrierInvis/CASInvis.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/carrier/carrierInvis/CALInvis.png").convert_alpha(),]
markerDraw = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/marker.png").convert_alpha()
enemyStation = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES1.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES2.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES3.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES4.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES5.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES6.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES7.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES8.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES9.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES10.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES11.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES12.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES13.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES14.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES15.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES16.png").convert_alpha(),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyStationAnim/ES17.png").convert_alpha(),]
enemyShields = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESS21.png"),]
enemyShieldsUA = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/enemyShieldAnim/ESSUa.png").convert_alpha()

# SOUNDS

torpedoFired = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/torpedoFired.ogg")
shoot2 = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/shoot2.ogg")
bigEnemyFire = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/bigEnemyFire.ogg")
enemyFire = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/enemyFire.ogg")
littleShoot = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/littleShoot.ogg")
powerUpEffect = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/powerUpEffect.ogg")
shipExplosionFX = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/shipExplosionFX.ogg")
mainMusic = "C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/Shiny Tech II comp REDUCED.ogg"
explosionSoundFX2 = pygame.mixer.Sound("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/sound/explosionSoundFX2.ogg")

attackCoordinates = [(63,28),(28,63),(98,63),(63,98)]
BACU = [(63,11),(63,18),(63,28),(63,63),(11,63),(18,63),(28,63),(98,63),(108,63),(115,63)]
BACL = [(63,11),(63,18),(63,28),(63,63),(11,63),(18,63),(28,63),(63,98),(63,108),(63,115)]
BACR = [(63,11),(63,18),(63,28),(63,63),(98,63),(108,63),(115,63),(63,98),(63,108),(63,115)]
BACD = [(63,63),(11,63),(18,63),(28,63),(98,63),(108,63),(115,63),(63,98),(63,108),(63,115)]

stationSpawnCoordinates = [(90+stationSpacing,119+stationSpacing),(winWidth-90-stationSpacing,119+stationSpacing),(90+stationSpacing,winHeight-119-stationSpacing),(winWidth-90-stationSpacing,winHeight-119-stationSpacing),(winWidth//2,winHeight//2)]
allSpawnCoordinates = copy.deepcopy(stationSpawnCoordinates)

healthAnimCounter = 0
invisAnimCounter = 0
fireAnimCounter = 0
amplifyAnimCounter = 0

clock = pygame.time.Clock()

def drawWindow():
    #Draws the window each frame
    global healthAnimCounter
    global invisAnimCounter
    global fireAnimCounter
    global amplifyAnimCounter
    global count
    global minerCount
    global healthCall
    global upgrades
    global score
    global play
    global purchasingTimeDelay
    global purchasingTimeDelayTimer
    global allSpawnCoordinates
    window.blit(background,(0,0))
    window.blit(scoreground,(winWidth-400,winHeight-253))
    window.blit(purchasesBlit,(0,winHeight-108))

    for x in range(len(str(score))):
        window.blit(scoreCounter[int(str(score)[x])],(winWidth - 406 + x * spacing, winHeight - 200))

    for x in range(len(str(enemyKills))):
        window.blit(scoreCounter[int(str(enemyKills)[x])],(winWidth - 108 + x * spacing, winHeight - 192))

    for x in range(len(str(minerKills))):
        window.blit(scoreCounter[int(str(minerKills)[x])],(winWidth - 108 + x * spacing, winHeight - 128))

    for x in range(len(str(frigateKills))):
        window.blit(scoreCounter[int(str(frigateKills)[x])],(winWidth - 108 + x * spacing, winHeight - 69))

    for x in range(len(str(highScore))):
        window.blit(damageCounterAllied[int(str(highScore)[x])],(winWidth - 390 + x * 7, winHeight - 203))

    if currentLives > 0:
        for x in range(currentLives):
            window.blit(livesRemaining,(winWidth - 396 + x * lifeSpacing,winHeight-71))

    for x in range(6):
        if upgrades[x] == 1:
            window.blit(purchasesUsed[x],(1 + 98 * x, winHeight-108))



    numbers = pygame.key.get_pressed()



    if purchasingTimeDelayTimer <= 0:
        if numbers[K_1] and (upgrades[0] == 0 and score >= 80000 or upgrades[0] == 1 and score >= 280000):
            purchasingTimeDelayTimer = purchasingTimeDelay
            if upgrades[0] == 0:
                upgrades[0] = 1
                score -= 80000
                currentPlayerLocation = [play.x,play.y,play.invisible,play.fireBoost,play.healthRegenTime,play.amplified]
                try:
                    objectList.remove(play)
                except:
                    pass
                for ob in [a for a in objectList if not isinstance(a,spaceStation) and not isinstance(a, shield)]:
                    if ob.target == play:
                        ob.target = 0
                play = annoraxPlayable(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
                objectList.append(play)
                play.x = currentPlayerLocation[0]
                play.y = currentPlayerLocation[1]
                play.invisible = currentPlayerLocation[2]
                play.fireBoost = currentPlayerLocation[3]
                play.healthRegenTime = currentPlayerLocation[4]
                play.amplified = currentPlayerLocation[5]
                if play.amplified > 1:
                    play.mitigation *= 1.75
                    play.speed *= 1.75
                    play.orgSpeed = play.speed
                    play.orgHealth *= 1.75
                    play.health *= 1.75
                    play.orgHealthRecovery /= 2.5
            else:
                score -= 280000
                currentStations = [a for a in objectList if isinstance(a, friendly)]
                for coordinate in allSpawnCoordinates:
                    for givenStation in currentStations:

                        if math.hypot(givenStation.x-coordinate[0],givenStation.y-coordinate[1]) < 35:
                            allSpawnCoordinates.remove(coordinate)

                for coordinate in [a for a in stationSpawnCoordinates if a not in allSpawnCoordinates]:
                    if len([a for a in currentStations if math.hypot(a.x-coordinate[0],a.y-coordinate[1]) <35]) == 0:
                        allSpawnCoordinates.append(coordinate)


                




                aPurchasedStation = friendly(1,1,1,1,1,1,1,1,1,1,1)
                try:
                    aPurchasedStation.x = allSpawnCoordinates[0][0]
                    aPurchasedStation.y = allSpawnCoordinates[0][1]
                    allSpawnCoordinates = allSpawnCoordinates[1:] 
                except:
                    pass
                
                objectList.append(aPurchasedStation)

                shieldUp1 = friendlyS(1,aPurchasedStation.x,aPurchasedStation.y-24,0,1,1,1,1,1,1,aPurchasedStation)
                objectList.append(shieldUp1)

                shieldRight1 = friendlyS(1,aPurchasedStation.x+aPurchasedStation.width+4,aPurchasedStation.y,1,1,1,1,1,1,1,aPurchasedStation)
                objectList.append(shieldRight1)

                shieldDown1 = friendlyS(1,aPurchasedStation.x,aPurchasedStation.y+aPurchasedStation.height,2,1,1,1,1,1,1,aPurchasedStation)
                objectList.append(shieldDown1)

                shieldLeft1 = friendlyS(1,aPurchasedStation.x-20,aPurchasedStation.y,3,1,1,1,1,1,1,aPurchasedStation)
                objectList.append(shieldLeft1)
     
            pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
        elif numbers[K_2] and score >= 45000:
            purchasingTimeDelayTimer = purchasingTimeDelay
            score -= 45000
            if upgrades[1] == 0:
                upgrades[1] = 1
                buffList.append(reinforcements(1,1,1))
                buffList.append(extraLife(1,1,1))
                buffList.append(extraScore(1,1,1))
            else:
                for x in range(2):
                    decision = random.randint(1,2)
                    if decision == 1:
                        objectList.append(playerN(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
                    else:
                        objectList.append(annoraxN(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
            pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)

        elif numbers[K_3] and (score >= 15000 and upgrades[2] == 0 or score >= 25000 and upgrades[2] == 1) :
            purchasingTimeDelayTimer = purchasingTimeDelay
            pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
            if upgrades[2] == 0:
                score -= 15000
                upgrades[2] = 1
                try:
                    powerUpList.append(healthPowerUp("health",random.randint(play.x-90,play.x+90),random.randint(play.y-90,play.y+90),1)) #16x16 dimensions
                except:
                    pass
            else:
                score -= 25000
                play.healthRegenTime += 500

        elif numbers[K_4] and (score >= 15000 and upgrades[3] == 0 or score >= 25000 and upgrades[3] == 1):
            purchasingTimeDelayTimer = purchasingTimeDelay
            pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
            if upgrades[3] == 0:
                score -= 15000
                upgrades[3] = 1
                powerUpList.append(invisPowerUp("invis",random.randint(play.x-90,play.x+90),random.randint(play.y-90,play.y+90),1)) #16x16 dimensions
            else:
                score -= 25000
                play.invisible += 500
        elif numbers[K_5] and (score >= 15000 and upgrades[4] == 0 or score >= 25000 and upgrades[4] == 1):
            purchasingTimeDelayTimer = purchasingTimeDelay
            pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
            if upgrades[4] == 0:
                score -= 15000
                upgrades[4] = 1
                powerUpList.append(firePowerUp("fire",random.randint(play.x-90,play.x+90),random.randint(play.y-90,play.y+90),1)) #16x16 dimensions
            else:
                score -= 25000
                play.fireBoost += 750
        elif numbers[K_6] and (score >= 15000 and upgrades[5] == 0 or score >= 25000 and upgrades[5] == 1):
            purchasingTimeDelayTimer = purchasingTimeDelay
            pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
            if upgrades[5] == 0:
                score -= 15000
                upgrades[5] = 1
                powerUpList.append(amplifyPowerUp("amplify",random.randint(play.x-90,play.x+90),random.randint(play.y-90,play.y+90),1)) #16x16 dimensions
            else:
                score -= 25000
                if play.amplified <= 1:
                    play.mitigation *= 1.75
                    play.speed *= 1.75
                    play.orgSpeed = play.speed
                    play.orgHealth *= 1.75
                    play.health *= 1.75
                    play.orgHealthRecovery /= 2.5

                play.amplified += 750
    else:
        purchasingTimeDelayTimer -= 1




    if play.healthRegenTime > 0:
        healthAnimCounter += 1
        window.blit(healthyActivated[healthAnimCounter], (winWidth - 387, winHeight - 141))
        if healthAnimCounter >= 51:
            healthAnimCounter = 0

    if play.invisible > 0:
        invisAnimCounter += 1
        window.blit(invisActivated[invisAnimCounter], (winWidth - 335, winHeight - 141))
        if invisAnimCounter >= 51:
            invisAnimCounter = 0

    if play.fireBoost > 0:
        fireAnimCounter += 1
        window.blit(fireActivated[fireAnimCounter], (winWidth - 283, winHeight - 141))
        if fireAnimCounter >= 51:
            fireAnimCounter = 0

    if play.amplified > 0:
        amplifyAnimCounter += 1
        window.blit(amplifyActivated[amplifyAnimCounter], (winWidth - 231, winHeight - 141))
        if amplifyAnimCounter >= 51:
            amplifyAnimCounter = 0





    healthList = []
    nameList = []

    [m.draw(window) for m in mineList] #Draws all current mines

    check = 0

    for o in objectList:
        #pygame.draw.rect(window,(255,0,0),o.hitbox,2) #HITBOXES
        if not isinstance(o,player) and not isinstance(o, spaceStation) and not isinstance(o, shield) and not isinstance(o,annoraxPlayable) and o.runTimer <= 0 and o.health < 0.51 * o.orgHealth:
            healthList.append(o.health / o.orgHealth)
            nameList.append(o)

    for o in objectList:


        if not isinstance(o, spaceStation) and not isinstance(o, shield) and o.healthTarget != 0:
            check = 1       


        if check == 0:
            healthCall = 0

        if healthCall == 0 and len(powerUpList) > 0 and len(healthList) > 0:
            healthIndex = healthList.index(min(healthList))
            unhealthyObject = nameList[healthIndex]
            
            healths = [p for p in powerUpList if p.name == "health"]
            if len(healths) > 0:
                currentShortestDistance = 9999
                target = 0
                for h in healths:
                    distance = math.hypot(h.x - unhealthyObject.x, h.y - unhealthyObject.y)
                    if distance < currentShortestDistance:
                        currentShortestDistance = distance
                        target = h

                unhealthyObject.healthTarget = healths[healths.index(target)] 
                healthCall = 1


                
                



        #Checks for miners
        if isinstance(o,miner):
            minerCount += 1
        #Checks for enemies
        if isinstance(o,enemy):
            count += 1

        for d in o.damages:
            [a.draw(window) for a in d]
            # Draws all object damages
        if o.alreadyCollided >= 1:
            o.alreadyCollided -= 1
            #Timer for collisions with enemies to prevent them from using suicide mode if already in collision with the player
        o.basicFunctions(window)
        #Every object has these basic functions, so every frame they will perform these behaviours
        o.draw(window)
        #Every object will need to be drawn
        if not isinstance(o, shield) and o.damagedCount > 0:
            #Damage count to determine how long an object's health bar will show after being damaged
            trueHealthPercentage = o.health / o.orgHealth 
            #Calculates what percentage of health an object is at

            #The following structure determines what colour the health bar will show, dependent on the health percentage
            #Red element for the (255,255,255) structure
            redElement = int(2.55 / (0.0001 + trueHealthPercentage) ** 8)
            #If above code fails, set the red to 255
            #redElement = 255
            #Determines what the green element will be for the (255,255,255) structure
            greenElement = int(255 * trueHealthPercentage)

            #Draws the bar OUTLINE      
            pygame.draw.rect(window, (0,0,0), o.healthbar, 1)
            try:
                if 72 <= redElement <= 201:
                    redElement = 201
                #Tries to draw the red element 
                pygame.draw.rect(window, (abs(redElement) ,abs(greenElement),0), o.innerBar, 0)
            except:
                #If this fails, default redElement to 255
                try:
                    #Final attempt to draw the healthbar
                    pygame.draw.rect(window, (255,abs(greenElement),0), o.innerBar, 0)
                except:
                    pass
            #Decrements the damage count per frame,so that the healthbar does not show up constantly
            o.damagedCount -= 1
        
        #This determines where on the object a hit will be displayed if an object has been hit
        for hit in o.hits:

            #Creates 2 random numbers, a check is needed to ensure that the hits always stay in the same place so the number will have to be kept the same throughout the explosion
            if hit.randomCheck == 0:
                hit.randNum = random.randint(10,o.width // 1.2)
                hit.randomCheck = 1
            if hit.randomCheck == 1:
                hit.randNum2 = random.randint(10,o.height // 1.2)
                hit.randomCheck = 2

            #Which direction the object is moving must be known so that the explosion will appear to be hitting the ship and not nearby
            if not isinstance(o,spaceStation) and not isinstance(o, shield):
                if o.left or o.right:        
                    hit.x += o.x - hit.x + hit.randNum
                    hit.y += o.y - hit.y + hit.randNum2
                if o.up or o.down:
                    hit.y += o.y - hit.y + hit.randNum
                    hit.x += o.x - hit.x + hit.randNum2
                if hit.type == 1:
                    window.blit(explosion[hit.animCounter//3],(hit.x,hit.y))
                elif hit.type == 2:
                    window.blit(largerExplosion[hit.animCounter//3],(hit.x,hit.y))
                #Increments the animation counter to display the explosion animation
                hit.animCounter += 1
                if hit.animCounter >= 24:
                    o.hits.remove(o.hits[o.hits.index(hit)])
                    #Removes the explosion
            else:
                hit.x += o.x - hit.x + hit.randNum
                hit.y += o.y - hit.y + hit.randNum2
                window.blit(explosion[hit.animCounter//3],(hit.x,hit.y))
                hit.animCounter += 1
                if hit.animCounter >= 24:
                    o.hits.remove(o.hits[o.hits.index(hit)])
                    #Removes the explosion





                    
            


        for p in o.projectiles:
            p.draw(window)
        for h in o.horProjectiles:
            h.draw2(window)
    for b in BOOM:
        b.draw(window)
    for power in powerUpList:
        power.draw(window)
        power.floatAnimation()
    for buff in buffList:
        buff.floatAnimation()
        buff.draw(window)

        #Draws all explosions and projectiles per frame



    count = 1
    minerCount = 0

    #pygame.display.update()

class ship():
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,horProjectiles,left,right,up,down,counter,healthRecovery):
        #All the key attributes of a ship object
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.health = health
        self.orgHealth = orgHealth
        self.mitigation = mitigation
        self.speed = speed
        self.projectiles = projectiles
        self.horProjectiles = horProjectiles
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.counter = counter
        self.healthRecovery = healthRecovery
        self.orgHealthRecovery = self.healthRecovery
        self.projectileFrequency = 0
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.healthbar = (self.x+1,self.y-0.2*self.height,20,20)
        self.hitCoordinatesCheck = 0
        self.hitCheck = 0
        self.explosionAnimationCounter = 0
        self.hits = []
        self.damagedCount = 0
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
        self.notLeft = False
        self.notRight = False
        self.notUp = False
        self.notDown = False
        self.enemyRange = 125
        self.attackPatternLeft = 0
        self.attackPatternRight = 0
        self.attackPatternSouth = 0
        self.attackPatternTop = 0
        self.myRand = 0
        self.part2 = 0
        self.firstAttack = 0
        self.enemyAnimCounter = 0
        self.friendCount = 1
        self.needHealth = 0
        self.healthTarget = 0
        self.healthRegenTime = 0
        self.invisCall = 0
        self.fireCall = 0
        self.amplifyCall = 0
        self.invisible = 0
        self.fireBoost = 0
        self.fireProjectiles = []
        self.leeway = 0
        self.fleeTimer = 0
        self.currentFleeDirection = 0
        self.notGoingAnywhere = 0
        self.trigger = 0
        self.moving = 0
        self.timer = 0
        self.firingBeam = 0
        self.amplified = 0
        self.amplificationBoost = 0
        #Any unexplained attributes will be done so where they are used

    #All basic functions
    def basicFunctions(self,window):
        trueHealthPercentage = self.health / self.orgHealth 

        #Calculates the DIMENSIONS of the healthbar - smaller ships will have smaller healthbars and vice versa
        if isinstance(self, annoraxPlayable) or isinstance(self, annoraxN):
            self.healthbar = (self.x + 60 / 4,self.y-0.2*60,60 / 2,60 / 8)
        else:
            self.healthbar = (self.x + self.width / 4,self.y-0.2*self.height,self.width / 2,self.height / 8)
        self.innerBar = (self.healthbar[0] + 1, self.healthbar[1] + 1, (self.healthbar[2] - 2) * trueHealthPercentage, self.healthbar[3] - 2)
        self.hitbox = (self.x,self.y,self.width,self.height)


        #Further reinforcement variables to eliminate any leftover bugs
        self.notLeft = False
        self.notRight = False
        self.notUp = False
        self.notDown = False

        self.healthRecovery -= 1 #depreciates hp recovery cooldown

        if self.healthRecovery <= 0 and self.suicideAttack != 1:
            self.healthRecovery = self.orgHealthRecovery #hp recovery reaches 0, add health and reset cooldown
            if self.health + 1 <= self.orgHealth:
                self.health += 1

        if self.healthRegenTime >= 1:
            self.healthRegenTime -= 1
            if self.health + 0.4 <= self.orgHealth and self.health != 0:
                self.health += 0.4

        if self.fireBoost > 0:
            self.fireBoost -= 1






        




        if (isinstance(self,annoraxN) and self.firingBeam == 0) or isinstance(self, playerN) or isinstance(self,frigate) or isinstance(self,carrier):
            
            if self.target == 0:
                if isinstance(self,frigate) or isinstance(self,carrier):
                    poTargets = [a for a in objectList if a.name in alliedTeam]
                else:
                    poTargets = [a for a in objectList if a.name in enemyTeam]
                if len(poTargets) > 0:
                    self.target = poTargets[random.randint(0,len(poTargets)-1)]

            if isinstance(self,playerN) and self.rocketTimer <= 0:
                aPowerfulBullet = rocket(self.x + self.width / 2, self.y + self.height / 2, self.name,self,self.target)
                self.projectiles.append(aPowerfulBullet)
                projectileList.append(aPowerfulBullet)
                self.rocketTimer = 90
                pygame.mixer.Channel(6).play(torpedoFired, maxtime=1805)

            if self.runTimer <= 0: 
                self.timer -= 1

                if self.target != 0 and self.target.health <= 0:
                    self.target = 0
                elif self.healthTarget == 0 and self.runTimer <= 0 and self.firingBeam == 0 and self.target != 0:
                    if abs(self.target.x + self.target.width / 2 - self.x - self.width / 2) <= 35:
                        if self.target.y < self.y:
                            self.down = False
                            self.up = True
                            self.left = False
                            self.right = False
                            
                            if isinstance(self, frigate):
                                frigate.fireGuns(self)
                            elif isinstance(self,playerN):
                                playerN.fireGuns(self)
                            elif isinstance(self,annoraxN):
                                if self.timer <= 0 and self.annoraxBeamTimer <= 0:
                                    self.firingBeam = 1
                                    self.annoraxBeamTimer = 600
                                annoraxN.fireGuns(self)
                            else:
                                carrier.fireGuns(self)
                            if self.y - self.target.y - self.target.height / 2 > 60 + self.target.width:
                                self.y -= self.speed
                        else:
                            self.up = False
                            self.down = True
                            self.left = False
                            self.right = False
                            if isinstance(self, frigate):
                                frigate.fireGuns(self)
                            elif isinstance(self,playerN):
                                playerN.fireGuns(self)
                            elif isinstance(self,annoraxN):
                                if self.timer <= 0 and self.annoraxBeamTimer <= 0:
                                    self.firingBeam = 1
                                    self.annoraxBeamTimer = 600
                                annoraxN.fireGuns(self)
                            else:
                                carrier.fireGuns(self)
                            if self.target.y + self.target.height - self.y > 60 + self.target.width:
                                self.y += self.speed
                    elif abs(self.target.y + self.target.height / 2 - self.y - self.height / 2)<= 35:
                        if self.target.x > self.x:
                            self.right = True
                            self.down = False
                            self.left = False
                            self.up = False
                            if isinstance(self, frigate):
                                frigate.fireGuns(self)
                            elif isinstance(self,playerN):
                                playerN.fireGuns(self)
                            elif isinstance(self,annoraxN):
                                if self.timer <= 0  and self.annoraxBeamTimer <= 0:
                                    self.firingBeam = 1
                                    self.annoraxBeamTimer = 600
                                annoraxN.fireGuns(self)
                            else:
                                carrier.fireGuns(self)
                            if self.target.x + self.target.width / 2 - self.x > 60 + self.target.width:
                                self.x += self.speed
                        else:
                            self.right = False
                            self.left = True
                            self.up = False
                            self.down = False
                            if isinstance(self, frigate):
                                frigate.fireGuns(self)
                            elif isinstance(self,playerN):
                                playerN.fireGuns(self)
                            elif isinstance(self,annoraxN):
                                if self.timer <= 0  and self.annoraxBeamTimer <= 0:
                                    self.firingBeam = 1
                                    self.annoraxBeamTimer = 600
                                annoraxN.fireGuns(self)
                            else:
                                carrier.fireGuns(self)
                            if self.x - self.target.width / 2 - self.target.x > 60 + self.target.width:
                                self.x -= self.speed
                    else:
                        self.timer = 24
                        if abs(self.target.x + self.target.width / 2 - self.x - self.width / 2) + 25 > abs(self.target.y + self.target.height / 2 -self.y - self.height / 2):
                            if self.target.y > self.y:
                                self.down = True
                                self.up = False
                                self.left = False
                                self.right = False
                                self.y += self.speed
                            else:
                                self.down = False
                                self.up = True
                                self.left = False
                                self.right = False
                                self.y -= self.speed
                        else:
                            if self.target.x > self.x:
                                self.right = True
                                self.up = False
                                self.left = False
                                self.down = False
                                self.x += self.speed
                            else:
                                self.right = False
                                self.up = False
                                self.left = True
                                self.down = False
                                self.x -= self.speed

        #This is code used by all non-player objects to avoid colliding with other objects
        if not isinstance(self,player) and not isinstance(self,annoraxPlayable):
            
            if self.healthTarget != 0 and self.healthTarget not in powerUpList:
                self.healthTarget = 0
                self.invisCall = 0
                self.amplifyCall = 0
                self.fireCall = 0

            if self.runTimer <= 0:
                if self.health <= 0.52 * self.orgHealth and self.healthTarget != 0 and self.suicideAttack != 1 and self.runTimer <= 0 and len(powerUpList) != 0  or self.healthTarget != 0 and self.suicideAttack != 1 and self.runTimer <= 0 and len(powerUpList) != 0 and (self.invisCall == 1 or self.fireCall == 1 or self.amplifyCall == 1):
                    if self.healthTarget.x > self.x + 25:
                        self.x += self.speed
                        self.up = False
                        self.right = True
                        self.down = False
                        self.left = False
                    elif self.healthTarget.x < self.x - 25:
                        self.x -= self.speed
                        self.up = False
                        self.right = False
                        self.down = False
                        self.left = True
                    elif self.healthTarget.y > self.y + 25:
                        self.y += self.speed
                        self.up = False
                        self.right = False
                        self.down = True
                        self.left = False
                    else:
                        self.y -= self.speed
                        self.up = True
                        self.right = False
                        self.down = False
                        self.left = False
            if self.suicideAttack == 1:
                self.healthTarget = 0
                self.invisCall = 0
                self.fireCall = 0
                self.amplifyCall = 0

            

            for o in [a for a in objectList if not isinstance(a, spaceStation) and not isinstance(a, shield) and not isinstance(a,fighter)]:  



                if o != self and self.suicideAttack != 1 and not(isinstance(self,carrier) and isinstance(o,fighter)) : #Suicide charging enemies will ignore this code for obvious reasons
                    actualDistanceFromTarget = math.hypot((o.x+o.width/2)-(self.x+self.width/2),(o.y+o.height/2)-(self.y+self.height/2)) #Calculates Pythagorean distance from target
                    #breadth = 640 / self.width
                    #Checks if the object must evade the enemy - if runTimer >= 0, then this code will be activated

                    #if o.x + o.width / 2 > self.x + self.width / 2 



                    if actualDistanceFromTarget <= (self.width + self.height + o.width + o.height) / 2.5 and self.invisible <= 0 and o.invisible <= 0:
                        self.runTimer = 10 + random.randint(1,40)
                        #self.trigger += 1
                        #if self.trigger > 15:
                        self.randomNum = 0
                            #self.trigger = 0
                        #Triggers run timer
                    '''
                    if self.fleeTimer >= 1:
                        directions = {"up" : 1 , "right" : 1, "down" : 1 , "left" : 1,}
                        potentialCollisions = [a for a in objectList if math.hypot((a.x+a.width/2)-(self.x+self.width/2),(a.y+a.height/2)-(self.y+self.height/2)) <= (self.width + self.height + o.width + o.height) / 2 ]
                        for a in potentialCollisions:
                            if a.x > self.x and self.x + self.speed + self.width + 55 > a.x:
                                directions["up"] = 0
                            elif a.x < self.x and self.x - self.speed - 55  -self.width < a.x:
                                directions["right"] = 0
                            elif a.y > self.y and self.y + self.speed + self.height + 55 > a.y:
                                directions["down"] = 0
                            elif a.y < self.y and self.y - self.speed - self.height - 55 < a.y:
                                directions["left"] = 0
                    '''



                    if self.runTimer >= 1:
                        directions = [1,1,1,1]
                        if type(self.target) != int:
                            potentialCollisions = [a for a in objectList if math.hypot((a.x+a.width/2)-(self.x+self.width/2),(a.y+a.height/2)-(self.y+self.height/2)) <= (self.width + self.height + o.width + o.height) / 2.5 ]
                            for a in potentialCollisions:
                                if a.y + a.height / 2 < self.y + self.height / 2:
                                    directions[0] = 0
                                if a.y + a.height / 2 > self.y + self.height / 2:
                                    directions[2] = 0
                                if a.x + a.width / 2 > self.x + self.width / 2:
                                    directions[1] = 0
                                if a.x + a.width / 2 < self.x + self.width / 2:
                                    directions[3] = 0
                            
                        self.runTimer -= 1
                        #Decrements the run timer each frame
                        if self.randomNum == 0:
                            self.randomNum = random.randint(1,3)
                            #This random number has 3 possibilities as there are 3 different directions to avoid collision
                        if o.x > self.x and abs(o.y - self.y) <= abs(o.x - self.x): #FLEE RIGHT
                            self.notRight = True
                            if self.randomNum == 1 and not self.notLeft and directions[3] == 1:
                                self.left = True
                                self.down = False
                                self.up = False
                                self.right = False
                                if self.x - self.speed >= 0:
                                    self.x -= self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees left

                            elif self.randomNum == 2 and not self.notDown and directions[2] == 1:
                                self.left = False
                                self.down = True
                                self.up = False
                                self.right = False
                                if self.y + self.speed + self.height <= winHeight:
                                    self.y += self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees down

                            elif self.randomNum == 3 and not self.notUp and directions[0] == 1:
                                self.up = True
                                self.down = False
                                self.left = False
                                self.right = False
                                if self.y - self.speed >= 0:
                                    self.y -= self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees up

                            else:
                                self.randomNum = 0
                            return
                        elif o.x < self.x and abs(o.y - self.y) <= abs(o.x - self.x): #ENEMY IS TO THE LEFT
                            self.notLeft = True
                            if self.randomNum == 1 and not self.notRight and directions[1] == 1:
                                self.left = False
                                self.down = False
                                self.up = False
                                self.right = True
                                if self.x + self.speed  + self.width <= winWidth:
                                    self.x += self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees right

                            elif self.randomNum == 2 and not self.notDown and directions[2] == 1 or directions[1] == 0 and directions[2] == 1:
                                self.left = False
                                self.down = True
                                self.up = False
                                self.right = False
                                if self.y + self.speed + self.height <= winHeight:
                                    self.y += self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees down
                            elif self.randomNum == 3 and not self.notUp and directions[0] == 1 or directions[1] == 0 and directions[0] == 1 and directions[2] == 0:
                                self.up = True
                                self.down = False
                                self.left = False
                                self.right = False
                                if self.y - self.speed >= 0:
                                    self.y -= self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees up
                            else:
                                self.randomNum = 0
                            return

                        elif o.y < self.y and abs(o.y - self.y) >= abs(o.x - self.x): #ABOVE
                            self.notUp = True
                            if self.randomNum == 2 and not self.notLeft and directions[3] == 1:
                                self.left = True
                                self.down = False
                                self.up = False
                                self.right = False
                                if self.x - self.speed >= 0:
                                    self.x -= self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees left

                            elif self.randomNum == 1 and not self.notDown and directions[2] == 1 or directions[2] == 1 and directions[3] == 0:
                                self.left = False
                                self.down = True
                                self.up = False
                                self.right = False
                                if self.y + self.speed + self.height <= winHeight:
                                    self.y += self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees down
                            elif self.randomNum == 3 and not self.notRight and directions[1] == 1 or directions[3] == 0 and directions[2] == 0 and directions[1] == 1:
                                self.up = False
                                self.down = False
                                self.left = False
                                self.right = True
                                if self.x + self.speed + self.width <= winWidth:
                                    self.x += self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees right
                            else:
                                self.randomNum = 0
                            return
                        elif o.y > self.y and abs(o.y - self.y) >= abs(o.x - self.x): #BELOW
                            self.notDown = True
                            if self.randomNum == 2 and not self.notLeft and directions[3] == 1:
                                self.left = True
                                self.down = False
                                self.up = False
                                self.right = False
                                if self.x - self.speed >= 0:
                                    self.x -= self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees left

                            elif self.randomNum == 1 and not self.notUp and directions[0] == 1 or directions[3] == 0 and directions[0] == 1:
                                self.left = False
                                self.down = False
                                self.up = True
                                self.right = False
                                if self.y - self.speed - self.height >= 0:
                                    self.y -= self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees up
                            elif self.randomNum == 3 and not self.notRight and directions[1] == 1 or directions[3] == 0 and directions[0] == 0 and directions[1] == 1:
                                self.up = False
                                self.down = False
                                self.left = False
                                self.right = True
                                if self.x + self.speed + self.width <= winWidth:
                                    self.x += self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees right
                            else:
                                self.randomNum = random.randint(1,3)
                            return
                    else:
                        self.randomNum = 0
#refhere
class annoraxN(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Friendly",60,60,random.randint(50,winWidth),random.randint(50,winHeight),100,100,0.25,6,[],[],False,False,True,False,0,12)

        self.target = 0
        self.rememberCoordinates = 0
        self.rememberTimer = 0
        self.timer = 24
        self.annoraxBeamTimer = 600
        self.slowDownRate = 0.92
        self.slowDownTime = 36
        self.shootTimer = 75
        self.beamAnimTimer = 0
        self.beamAnimCounter = 0
        self.firingBeam = 0
        self.orgSpeed = self.speed
        self.tolerance = 35

    def draw(self,window):

        if self.annoraxBeamTimer > 0:
            self.annoraxBeamTimer -= 1


        if self.left or self.right:
            self.width = 80
            self.height = 30

        else:
            self.width = 30
            self.height = 80

        if self.invisible <= 0:
            self.counter += 1
            if self.up:
                window.blit(annorax[0][self.counter//2], (self.x,self.y))
            elif self.right:
                window.blit(annorax[1][self.counter//2], (self.x,self.y))
            elif self.down:
                window.blit(annorax[2][self.counter//2], (self.x,self.y))
            else:
                window.blit(annorax[3][self.counter//2], (self.x,self.y))
        else:
            if self.up: 
                window.blit(annoraxInvis[0],(self.x,self.y))
            elif self.right:
                window.blit(annoraxInvis[1],(self.x,self.y))
            elif self.down:
                window.blit(annoraxInvis[2],(self.x,self.y))
            else:
                window.blit(annoraxInvis[3],(self.x,self.y))

        if self.counter >= 32:
            self.counter = 0


        if self.firingBeam == 1:

            if self.up:
                self.y -= self.speed
            elif self.right:
                self.x += self.speed
            elif self.down:
                self.y += self.speed
            else:
                self.x -= self.speed

            self.beamAnimCounter += 1

            if self.beamAnimCounter >= 6:
                self.beamAnimCounter = 0

            if self.slowDownTime > 0:
                self.speed *= self.slowDownRate
                self.slowDownTime -= 1
            else:
                self.speed = 0
                self.shootTimer -= 1
                if self.shootTimer > 0:
                    if self.up:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x+self.width//2 - 3, self.y - 6 - a * 8, -1, self.name,self)
                            self.projectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
                    elif self.down:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x+self.width//2 - 3, self.y+self.height+ a * 8 -1, 1, self.name,self)
                            self.projectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
                    elif self.left:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x - 7 - a * 8, self.y+self.height//2 - 2, -1, self.name,self)
                            self.horProjectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
                    else:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x+self.width + a * 8 - 2, self.y + self.height // 2 - 2, 1, self.name,self)
                            self.horProjectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
            if self.shootTimer <= 0: 
                self.shootTimer = 75
                self.speed = self.orgSpeed
                self.slowDownTime = 36
                self.firingBeam = 0 
                self.annoraxBeamTimer = 600
        else:
            if self.speed == 0:
                self.speed = self.orgSpeed
        

    def fireGuns(self):
        if len(self.projectiles) + len(self.horProjectiles) <= 6:
            #Only fires if total number of projectiles <= 4
            if self.up:
                proj = projectile(self.x - 2 ,self.y + 34, -1,self.name,self)
                proj2 = projectile(self.x + self.width - 5, self.y + 36, -1,self.name,self)
                proj3 = projectile(self.x+self.width/2-4, self.y+46,-1,self.name,self )
                #Fires from the correct position on the ship, using the value variables defined above
                #Adds to the projectile list so they can be tracked
            elif self.down:
                proj = projectile(self.x - 2, self.y + 31, 1,self.name,self)
                proj2 = projectile(self.x + self.width - 5, self.y + 31, 1,self.name,self)
                proj3 = projectile(self.x+self.width/2-4, self.y+23,1,self.name,self )
                #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
            elif self.left:
                proj = projectile(self.x + 36, self.y -2, -1,self.name,self)
                proj2 = projectile(self.x + 36, self.y + self.height - 5, -1,self.name,self )
                proj3 = projectile(self.x+44,self.y+self.height/2-4  ,-1,self.name,self )
                #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
            else:
                proj = projectile(self.x+31, self.y-2,1,self.name,self)
                proj2 = projectile(self.x+31,self.y+self.height-5,1,self.name,self )
                proj3 = projectile(self.x+25,self.y+self.height/2-4  ,1,self.name,self )
            self.horProjectiles.append(proj)
            self.horProjectiles.append(proj2)
            self.horProjectiles.append(proj3)
                #Same as above


            pygame.mixer.Channel(random.randint(3,4)).play(shoot2, maxtime=600)
            projectileList.append(proj)
            projectileList.append(proj2)
            projectileList.append(proj3)
            #SEPARATE FIRE PROJECTILES TAB
        if self.fireBoost > 0:
            if len(self.fireProjectiles) <= 0:
                if self.up:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6 , self.y-24,-1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.down:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6, self.y + self.height,1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.left:
                    fireProj = powerfulProjectile(self.x - 24, self.y + self.height // 2 -6 ,-1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                else:
                    fireProj = powerfulProjectile(self.x + self.width, self.y + self.height // 2 -6,1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)

                projectileList.append(fireProj)








        
class annoraxPlayable(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Player ship",60,60,500,500,100,100,0.25,12,[],[],False,False,True,False,0,6)
        #Initialises this player's stats

        self.annoraxBeamTimer = 0
        self.slowDownRate = 0.92
        self.slowDownTime = 36
        self.shootTimer = 75
        self.beamAnimTimer = 0
        self.beamAnimCounter = 0
        self.firingBeam = 0
        self.orgSpeed = self.speed
        self.moving = 1
        self.checkTimer = 30

        self.playerIndicator = 0
        


    def draw(self,window):
        if self.playerIndicator == 0:
            playerMarker = marker(self.x + self.width / 2, self.y - 25, self)
            self.playerIndicator = playerMarker
            
        self.playerIndicator.draw()


        self.counter += 1

        if self.annoraxBeamTimer > 0:
            self.annoraxBeamTimer -= 1

        self.projectileFrequency += 1

        if self.projectileFrequency == 5:
            self.projectileFrequency = 0

        if self.left or self.right:
            self.width = 80
            self.height = 30

        else:
            self.width = 30
            self.height = 80

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.projectileFrequency == 0 or keys[pygame.K_e] and self.projectileFrequency == 0:
            annoraxPlayable.fireGuns(self)
            #Fires guns upon pressing space or e


        #CONTROLS
        if self.firingBeam == 0:
            if self.speed == 0:
                self.speed = self.orgSpeed
            self.moving = 1
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if self.invisible > 0:
                    window.blit(annoraxInvis[0],(self.x,self.y))
                else:
                    window.blit(annorax[0][self.counter//2], (self.x,self.y))
                if self.y - self.speed >= 0:
                    self.y -= self.speed
                self.left = False
                self.right = False
                self.down = False
                self.up = True
                #Goes up
            
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if self.invisible > 0:
                    window.blit(annoraxInvis[2],(self.x,self.y))
                else:
                    window.blit(annorax[2][self.counter//2], (self.x,self.y))            
                if self.y + self.speed + self.height <= winHeight:
                    self.y += self.speed
                self.left = False
                self.right = False
                self.down = True
                self.up = False
                #Goes down

            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.invisible > 0:
                    window.blit(annoraxInvis[3],(self.x,self.y))
                else:
                    window.blit(annorax[3][self.counter//2], (self.x,self.y))
                if self.x - self.speed >= 0:
                    self.x -= self.speed
                self.left = True
                self.right = False
                self.down = False
                self.up = False
                #Goes left

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.invisible > 0:
                    window.blit(annoraxInvis[1],(self.x,self.y))
                else:
                    window.blit(annorax[1][self.counter//2], (self.x,self.y))
                if self.x + self.width + self.speed <= winWidth:
                    self.x += self.speed
                self.left = False
                self.right = True
                self.down = False
                self.up = False
                #Goes right


            else:
                self.moving = 0
                conditions = [self.up,self.right,self.down,self.left]
                if self.invisible > 0:
                    window.blit(annoraxInvis[[conditions.index(c) for c in conditions if c][0]], (self.x,self.y))
                else:
                    window.blit(annorax[[conditions.index(c) for c in conditions if c][0]][self.counter//2], (self.x,self.y))
        else:
            conditions = [self.up,self.right,self.down,self.left]
            if self.invisible > 0:
                window.blit(annoraxInvis[[conditions.index(c) for c in conditions if c][0]], (self.x,self.y))
            else:
                window.blit(annorax[[conditions.index(c) for c in conditions if c][0]][self.counter//2], (self.x,self.y))
                #This line of code displays the correct sprite type and the correct animation, for each state (up, down, left, right) at every frame


        if keys[pygame.K_RETURN] and self.annoraxBeamTimer <= 0:
            self.firingBeam = 1
            self.speed *= 0.8
            self.annoraxBeamTimer = 500

        
        if self.firingBeam == 1:

            self.checkTimer -= 1

            if self.moving == 1:
                if self.up:
                    self.y -= self.speed
                elif self.right:
                    self.x += self.speed
                elif self.down:
                    self.y += self.speed
                else:
                    self.x -= self.speed

            self.beamAnimCounter += 1

            if self.beamAnimCounter >= 6:
                self.beamAnimCounter = 0

            if self.slowDownTime > 0:
                self.speed *= self.slowDownRate
                self.slowDownTime -= 1
            else:
                self.speed = 0
                self.shootTimer -= 1
                if self.shootTimer > 0:
                    if self.up:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x+self.width//2 - 3, self.y - 6 - a * 8, -1, self.name,self)
                            self.projectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
                    elif self.down:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x+self.width//2 - 3, self.y+self.height+ a * 8 -1, 1, self.name,self)
                            self.projectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
                    elif self.left:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x - 7 - a * 8, self.y+self.height//2 - 2, -1, self.name,self)
                            self.horProjectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
                    else:
                        for a in range(8):
                            aPowerfulBeamProject = beam(self.x+self.width + a * 8 - 2, self.y + self.height // 2 - 2, 1, self.name,self)
                            self.horProjectiles.append(aPowerfulBeamProject)
                            projectileList.append(aPowerfulBeamProject)
            if self.shootTimer <= 0 or (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.checkTimer <= 0:
                self.shootTimer = 75
                self.speed = self.orgSpeed
                self.slowDownTime = 36
                self.firingBeam = 0 
                self.checkTimer = 30



        if self.counter >= 32:
            self.counter = 0
        #Resets the animation counter to prevent an indexError

    def fireGuns(self):
        if len(self.projectiles) + len(self.horProjectiles) <= 9:
            #Only fires if total number of projectiles <= 4
            if self.up:
                proj = projectile(self.x - 2 ,self.y + 34, -1,self.name,self)
                proj2 = projectile(self.x + self.width - 5, self.y + 36, -1,self.name,self)
                proj3 = projectile(self.x+self.width/2-4, self.y+46,-1,self.name,self )
                #Fires from the correct position on the ship, using the value variables defined above
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                self.projectiles.append(proj3)
                #Adds to the projectile list so they can be tracked
            elif self.down:
                proj = projectile(self.x - 2, self.y + 31, 1,self.name,self)
                proj2 = projectile(self.x + self.width - 5, self.y + 31, 1,self.name,self)
                proj3 = projectile(self.x+self.width/2-4, self.y+23,1,self.name,self )
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                self.projectiles.append(proj3)
                #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
            elif self.left:
                proj = projectile(self.x + 36, self.y -2, -1,self.name,self)
                proj2 = projectile(self.x + 36, self.y + self.height - 5, -1,self.name,self )
                proj3 = projectile(self.x+44,self.y+self.height/2-4  ,-1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                self.horProjectiles.append(proj3)
                #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
            else:
                proj = projectile(self.x+31, self.y-2,1,self.name,self)
                proj2 = projectile(self.x+31,self.y+self.height-5,1,self.name,self )
                proj3 = projectile(self.x+25,self.y+self.height/2-4  ,1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                self.horProjectiles.append(proj3)
                #Same as above


            pygame.mixer.Channel(random.randint(3,4)).play(shoot2, maxtime=600)
            projectileList.append(proj)
            projectileList.append(proj2)
            projectileList.append(proj3)
            #SEPARATE FIRE PROJECTILES TAB
        if self.fireBoost > 0:
            if len(self.fireProjectiles) <= 0:
                if self.up:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6 , self.y-24,-1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.down:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6, self.y + self.height,1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.left:
                    fireProj = powerfulProjectile(self.x - 24, self.y + self.height // 2 -6 ,-1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                else:
                    fireProj = powerfulProjectile(self.x + self.width, self.y + self.height // 2 -6,1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)

                projectileList.append(fireProj)


                
                


class beam():
    def __init__(self,x,y,side,owner,ownerID):
        #Initialises the stats
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.side = side
        self.speed = 64 * self.side
        self.damage = 5
        self.critChance = 25
        self.owner = owner
        self.ownerID = ownerID
        self.aliveTimer = 165

    def draw(self,window):
        if self.side == 1:
            window.blit(beamAnim[2][self.ownerID.beamAnimCounter], (self.x,self.y)) #Displays the projectile
        else:
            window.blit(beamAnim[0][self.ownerID.beamAnimCounter], (self.x,self.y)) #Displays the projectile

        self.y += self.speed #Moves the projectile 
        if self.y > winHeight or self.y < 0: #If the projectiles exit the map
            #Removes the projectiles
            self.ownerID.projectiles.remove(self) 
            if self in projectileList:
                projectileList.remove(self)
        elif self not in projectileList:
            self.ownerID.projectiles.remove(self)


    #HORIZONTAL PROJECTILES - IDENTICAL LOGIC TO VERTICAL PROJECTILES
    def draw2(self,window):
        if self.side == 1:
            window.blit(beamAnim[1][self.ownerID.beamAnimCounter], (self.x,self.y)) #Displays the projectile
        else:
            window.blit(beamAnim[3][self.ownerID.beamAnimCounter], (self.x,self.y))
        self.x += self.speed #Moves the projectile 
        if self.x > winWidth or self.x < 0:
            self.ownerID.horProjectiles.remove(self)
            if self in projectileList:
                projectileList.remove(self)
        elif self not in projectileList:
            self.ownerID.horProjectiles.remove(self)


class marker():
    def __init__(self,x,y,target):
        self.x = x
        self.y = y
        self.target = target
        self.floating = 0
        self.hoverStatus = 0
    
    def draw(self):


        self.x = self.target.x + self.target.width / 2 - 2
        self.y = self.target.y - 25

        window.blit(markerDraw,(self.x,self.y+self.hoverStatus))

        self.floating += 1


        if self.floating <= 40:
            self.hoverStatus += 0.15
        elif 40 < self.floating <= 80:
            self.hoverStatus -= 0.15
        if self.floating > 80:
            self.floating = 0





class player(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Player ship",64,64,50,50,120,120,0.35,10,[],[],False,False,True,False,0,6)
        #Initialises the player stats

        self.playerIndicator = 0


    def draw(self,window):
        if self.playerIndicator == 0:
            playerMarker = marker(self.x + self.width / 2, self.y - 25, self)
            self.playerIndicator = playerMarker
            
        self.playerIndicator.draw()

        self.counter += 1
        #This variable is the animation counter for the player ship so that the engines can be animated - cycles through each frame

        if self.projectileFrequency > 0:
            self.projectileFrequency -= 1
        #This variable limits how often the player can fire their guns, to prevent them from firing infinitely quickly




        

    


        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.projectileFrequency == 0 or keys[pygame.K_e] and self.projectileFrequency == 0:
            player.fireGuns(self)
            #Fires guns upon pressing space or e

        #CONTROLS
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.invisible > 0:
                window.blit(shippingInvis[0],(self.x,self.y))
            else:
                window.blit(shipping[0][self.counter], (self.x,self.y))
            if self.y - self.speed >= 0:
                self.y -= self.speed
            self.left = False
            self.right = False
            self.down = False
            self.up = True
            #Goes up
        
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.invisible > 0:
                window.blit(shippingInvis[1],(self.x,self.y))
            else:
                window.blit(shipping[1][self.counter], (self.x,self.y))            
            if self.y + self.speed + self.height <= winHeight:
                self.y += self.speed
            self.left = False
            self.right = False
            self.down = True
            self.up = False
            #Goes down

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.invisible > 0:
                window.blit(shippingInvis[2],(self.x,self.y))
            else:
                window.blit(shipping[2][self.counter], (self.x,self.y))
            if self.x - self.speed >= 0:
                self.x -= self.speed
            self.left = True
            self.right = False
            self.down = False
            self.up = False
            #Goes left

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.invisible > 0:
                window.blit(shippingInvis[3],(self.x,self.y))
            else:
                window.blit(shipping[3][self.counter], (self.x,self.y))
            if self.x + self.width + self.speed <= winWidth:
                self.x += self.speed
            self.left = False
            self.right = True
            self.down = False
            self.up = False
            #Goes right

        else:
            conditions = [self.up,self.down,self.left,self.right]
            if self.invisible > 0:
                window.blit(shippingInvis[[conditions.index(c) for c in conditions if c][0]], (self.x,self.y))
            else:
                window.blit(shipping[[conditions.index(c) for c in conditions if c][0]][self.counter], (self.x,self.y))
            #This line of code displays the correct sprite type and the correct animation, for each state (up, down, left, right) at every frame


        if self.counter + 1 >= 10:
            self.counter = 0
        #Resets the animation counter to prevent an indexError

    def fireGuns(self):  
        value = 8
        value2 = 18
        #These values ensure that both projectiles fire from the correct position of the player ship
        #Projectiles will need to be fired from the nacelles
        if len(self.projectiles) + len(self.horProjectiles) <= 4:
            #Only fires if total number of projectiles <= 4
            if self.up:
                proj = projectile(self.x + value-3 ,self.y + value, -1,self.name,self)
                proj2 = projectile(self.x + self.width - 1 -3  - value, self.y + value, -1,self.name,self)
                #Fires from the correct position on the ship, using the value variables defined above
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                #Adds to the projectile list so they can be tracked
            elif self.down:
                proj = projectile(self.x + value-3, self.y + self.height - 2.5 * value, 1,self.name,self)
                proj2 = projectile(self.x + self.width - value - 1-3, self.y + self.height - 2.5 * value, 1,self.name,self)
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
            elif self.left:
                proj = projectile(self.x + value, self.y + value-3, -1,self.name,self)
                proj2 = projectile(self.x + value, self.y + self.height - value - 4, -1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
            else:
                proj = projectile(self.x + self.width - value2 - 1, self.y + value-3, 1,self.name,self)
                proj2 = projectile(self.x + self.width - value2 - 1, self.y + self.height - value-3 - 1, 1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                #Same as above

            pygame.mixer.Channel(random.randint(3,4)).play(shoot2, maxtime=600)
            projectileList.append(proj)
            projectileList.append(proj2)
            self.projectileFrequency = 4
            #SEPARATE FIRE PROJECTILES TAB
        if self.fireBoost > 0:
            if len(self.fireProjectiles) <= 0:
                if self.up:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6 , self.y-24,-1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.down:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6, self.y + self.height,1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.left:
                    fireProj = powerfulProjectile(self.x - 24, self.y + self.height // 2 -6 ,-1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                else:
                    fireProj = powerfulProjectile(self.x + self.width, self.y + self.height // 2 -6,1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)

                projectileList.append(fireProj)

class playerN(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Friendly",64,64,random.randint(50,winWidth),random.randint(50,winHeight),120,120,0.35,6,[],[],False,False,True,False,0,16)

        self.rocketTimer = 0
        self.tolerance = 35


    def draw(self,window):

        self.counter += 1
        self.rocketTimer -= 1




        #This variable is the animation counter for the player ship so that the engines can be animated - cycles through each frame

        if self.projectileFrequency > 0:
            self.projectileFrequency -= 1
        #This variable limits how often the player can fire their guns, to prevent them from firing infinitely quickly

        if self.invisible <= 0:
            if self.up:
                window.blit(shipping[0][self.counter], (self.x,self.y))
            elif self.right:
                window.blit(shipping[3][self.counter], (self.x,self.y))
            elif self.down:
                window.blit(shipping[1][self.counter], (self.x,self.y))
            else:
                window.blit(shipping[2][self.counter], (self.x,self.y))
        else:
            if self.up: 
                window.blit(shippingInvis[0],(self.x,self.y))
            elif self.right:
                window.blit(shippingInvis[3],(self.x,self.y))
            elif self.down:
                window.blit(shippingInvis[1],(self.x,self.y))
            else:
                window.blit(shippingInvis[2],(self.x,self.y))

        if self.counter + 1 >= 10:
            self.counter = 0

    def fireGuns(self):  
        value = 8
        value2 = 18
        #These values ensure that both projectiles fire from the correct position of the player ship
        #Projectiles will need to be fired from the nacelles
        if len(self.projectiles) + len(self.horProjectiles) <= 4:
            #Only fires if total number of projectiles <= 4
            if self.up:
                proj = projectile(self.x + value-3 ,self.y + value, -1,self.name,self)
                proj2 = projectile(self.x + self.width - 1 -3  - value, self.y + value, -1,self.name,self)
                #Fires from the correct position on the ship, using the value variables defined above
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                #Adds to the projectile list so they can be tracked
            elif self.down:
                proj = projectile(self.x + value-3, self.y + self.height - 2.5 * value, 1,self.name,self)
                proj2 = projectile(self.x + self.width - value - 1-3, self.y + self.height - 2.5 * value, 1,self.name,self)
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
            elif self.left:
                proj = projectile(self.x + value, self.y + value-3, -1,self.name,self)
                proj2 = projectile(self.x + value, self.y + self.height - value - 4, -1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
            else:
                proj = projectile(self.x + self.width - value2 - 1, self.y + value-3, 1,self.name,self)
                proj2 = projectile(self.x + self.width - value2 - 1, self.y + self.height - value-3 - 1, 1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                #Same as above

            pygame.mixer.Channel(random.randint(3,4)).play(shoot2, maxtime=600)
            projectileList.append(proj)
            projectileList.append(proj2)
            self.projectileFrequency = 4
            #SEPARATE FIRE PROJECTILES TAB
        if self.fireBoost > 0:
            if len(self.fireProjectiles) <= 0:
                if self.up:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6 , self.y-24,-1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.down:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6, self.y + self.height,1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.left:
                    fireProj = powerfulProjectile(self.x - 24, self.y + self.height // 2 -6 ,-1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                else:
                    fireProj = powerfulProjectile(self.x + self.width, self.y + self.height // 2 -6,1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)

                projectileList.append(fireProj)







class spaceStation():
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,projectiles,horProjectiles,healthRecovery):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.health = health
        self.orgHealth = orgHealth
        self.mitigation = mitigation
        self.projectiles = projectiles
        self.horProjectiles = horProjectiles
        self.healthRecovery = healthRecovery
        self.invisible = 0
        self.orgHealthRecovery = healthRecovery 
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.healthbar = (self.x+1,self.y-0.2*self.height,20,20)
        self.damages = []
        self.alreadyCollided = 0
        self.healthRegenTime = 15
        self.damagedCount = 0
        self.hits = []
        self.suicideAttack = 0
        self.fireProjectiles = []
        self.leeway = 0
        self.amplified = 0
        self.floating = 0
        self.animCounter = 0

    def floatAnimation(self):
        self.floating += 1


        if self.floating <= 40:
            self.y += 0.2
        elif 40 < self.floating <= 80:
            self.y -= 0.2
        if self.floating > 80:
            self.floating = 0



    def basicFunctions(self,window):
        trueHealthPercentage = self.health / self.orgHealth 

        #Calculates the DIMENSIONS of the healthbar - smaller ships will have smaller healthbars and vice versa
        self.healthbar = (self.x + self.width / 4,self.y-0.2*self.height,self.width / 2,self.height / 8)
        self.innerBar = (self.healthbar[0] + 1, self.healthbar[1] + 1, (self.healthbar[2] - 2) * trueHealthPercentage, self.healthbar[3] - 2)
        self.hitbox = (self.x,self.y,self.width,self.height)

        self.healthRecovery -= 1 #depreciates hp recovery cooldown

        spaceStation.floatAnimation(self)

        self.animCounter += 1

        if self.animCounter >= 48:
            self.animCounter = 0

        if self.healthRecovery <= 0 and self.health > 0:
            self.healthRecovery = self.orgHealthRecovery #hp recovery reaches 0, add health and reset cooldown
            if self.health + 1 <= self.orgHealth:
                self.health += 1

        if self.healthRegenTime >= 1:
            self.healthRegenTime -= 1
            if self.health + 0.3125 <= self.orgHealth and self.health != 0:
                self.health += 0.3125

class malevolent(spaceStation):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,projectiles,horProjectiles,healthRecovery):
        super().__init__("Enemy ship",128,128,random.randint(250,winWidth - width - 150),random.randint(150,winHeight - height - 150),2500,2500,0.75,[],[],12)

        self.torpedoTimer = 135
        self.beamTimer = 60
        self.secondBeamTimer = 0
        self.launchTimer = 0
        self.secondTorpTimer = 0
        self.attackTargets = 0
        self.numberOfTimesFired = 0
        self.numberOfBeamsFired = 0
        self.choice = random.randint(5,7)

    def draw(self,window):


        self.torpedoTimer -= 1
        self.beamTimer -= 1
        self.launchTimer -= 1

        window.blit(enemyStation[self.animCounter//3],(self.x,self.y))

        if self.torpedoTimer <= 0:
            self.secondTorpTimer -= 1
            if self.attackTargets == 0:
                self.attackTargets = [a for a in objectList if a.name in alliedTeam]

            if self.secondTorpTimer <= 0 and len(self.attackTargets) != 0:
                choice = random.randint(0,len(self.attackTargets)-1)
                for x in range(4):
                    someTorpedo = torpedo(self.x+attackCoordinates[x][0],self.y+attackCoordinates[x][1],self.name,self,self.attackTargets[choice],2)
                    projectileList.append(someTorpedo)
                    self.projectiles.append(someTorpedo)
                pygame.mixer.Channel(6).play(torpedoFired, maxtime=1805)
                self.secondTorpTimer = 15
                self.numberOfTimesFired += 1

            if self.numberOfTimesFired >= self.choice:
                self.numberOfTimesFired = 0
                self.secondTorpTimer = 0
                self.torpedoTimer = random.randint(95,150)
                self.attackTargets = 0
                self.choice = random.randint(5,7)

        if self.launchTimer <= 0:
            for x in range(5):
                objectList.append(fighter(1,1,1,self.x+48+ random.randint(-45,45),self.y+46+ random.randint(-45,45),1,1,1,1,1,1,1,1,1,1))
            self.launchTimer = 1050

        if self.beamTimer <= 0:
            self.secondBeamTimer -= 1

            if self.secondBeamTimer <= 0:
                for x in range(10):
                    aBeamAttack = enemyProjectile(self.x + BACU[x][0],self.y + BACU[x][1],-1,self.name,self)
                    self.projectiles.append(aBeamAttack)
                    projectileList.append(aBeamAttack)
                for x in range(10):
                    aBeamAttack = enemyProjectile(self.x + BACD[x][0],self.y + BACU[x][1],1,self.name,self)
                    self.projectiles.append(aBeamAttack)
                    projectileList.append(aBeamAttack)
                for x in range(10):
                    aBeamAttack = enemyProjectile(self.x + BACL[x][0],self.y + BACU[x][1],-1,self.name,self)
                    self.horProjectiles.append(aBeamAttack)
                    projectileList.append(aBeamAttack)
                for x in range(10):
                    aBeamAttack = enemyProjectile(self.x + BACR[x][0],self.y + BACU[x][1],1,self.name,self)
                    self.horProjectiles.append(aBeamAttack)
                    projectileList.append(aBeamAttack)

                pygame.mixer.Channel(random.randint(1,2)).play(bigEnemyFire, maxtime=600)

                self.numberOfBeamsFired += 1

                self.secondBeamTimer = 5

        if self.numberOfBeamsFired >= self.choice:
            self.numberOfBeamsFired = 0
            self.secondBeamTimer = 0
            self.beamTimer = random.randint(75,150)
            self.choice = random.randint(5,7)
        

                    


            





            



class friendly(spaceStation):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,projectiles,horProjectiles,healthRecovery):
        super().__init__("Friendly",90,119,random.randint(250,winWidth - width - 150),random.randint(150,winHeight - height - 150),1500,1500,0.65,[],[],12)

        self.attackTarget = 0
        self.volleyTimer = 120
        self.rocketTimer = 30
        self.beamTimer = 30

    def draw(self,window):

        self.volleyTimer -= 1
        self.rocketTimer -= 1
        self.beamTimer -= 1

        window.blit(friendlyStation[self.animCounter//3],(self.x,self.y))




        if self.volleyTimer <= 0:
            self.volleyTimer = 30
            potentialTargets = [a for a in objectList if a.name in enemyTeam]
            if len(potentialTargets) > 5:
                numberOfHits = 5
            else:
                numberOfHits = len(potentialTargets)
            for a in range(numberOfHits):
                aMostPowerfulBullet = torpedo(self.x+self.width/2,self.y + self.height/2,self.name,self,potentialTargets[random.randint(0,len(potentialTargets)-1)],1)
                self.projectiles.append(aMostPowerfulBullet)
                projectileList.append(aMostPowerfulBullet)
            pygame.mixer.Channel(6).play(torpedoFired, maxtime=1805)

        if self.rocketTimer <= 0:
            self.rocketTimer = 48
            potentialTargets = [a for a in objectList if a.name in enemyTeam and a.invisible <= 0]
            if len(potentialTargets) > 5:
                numberOfHits = 5
            else:
                numberOfHits = len(potentialTargets)
            for a in range(numberOfHits):
                aMostPowerfulBullet = rocket(self.x+self.width/2,self.y + self.height/2,self.name,self,potentialTargets[random.randint(0,len(potentialTargets)-1)])
                self.projectiles.append(aMostPowerfulBullet)
                projectileList.append(aMostPowerfulBullet)
            pygame.mixer.Channel(6).play(torpedoFired, maxtime=1805)

        if self.beamTimer <= 0:
            potentialTargets = [a for a in objectList if a.name in enemyTeam and a.x + 55 > self.x + self.width/2 and self.x + self.width/2 + 55 > a.x or a.name in enemyTeam and a.y + 55 > self.y + self.height/2 and self.y + self.height/2 + 55 > a.y  ]
            if len(potentialTargets) > 0:
                self.beamTimer = 4
                currentTarget = potentialTargets[random.randint(0,len(potentialTargets)-1)]
                if abs(currentTarget.y - (self.y + self.height/2)) < 60:
                    if currentTarget.x > self.x:
                        aLessPowerfulBullet = projectile(self.x+self.width/2,self.y+self.height/2,1,self.name,self)
                    else:
                        aLessPowerfulBullet = projectile(self.x+self.width/2,self.y+self.height/2,-1,self.name,self)
                    self.horProjectiles.append(aLessPowerfulBullet)
                elif abs(currentTarget.x - (self.x + self.width/2)) < 60:
                    if currentTarget.y > self.y:
                        aLessPowerfulBullet = projectile(self.x+self.width/2,self.y+self.height/2,1,self.name,self)
                    else:
                        aLessPowerfulBullet = projectile(self.x+self.width/2,self.y+self.height/2,-1,self.name,self)
                    self.projectiles.append(aLessPowerfulBullet)

                pygame.mixer.Channel(random.randint(3,4)).play(shoot2, maxtime=600)
                projectileList.append(aLessPowerfulBullet)
            

















class enemy(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Enemy ship",64,64,random.randint(50,winWidth),random.randint(50,winHeight+height),150,150,0.45,6,[],[],False,False,True,False,0,16)

        self.suicideExplosionTimer = 150 #timer for suiciding enemy ships to hit the player before they are destroyed
        self.torpTimer = random.randint(0,263)

        #Determines the stats for the enemy


    def draw(self,window):
        conditions = [self.up,self.down,self.left,self.right]
        #I added these to a list called conditions so that they would be easier to reference

        self.torpTimer -= 1

        if self.torpTimer <= 0 and self.suicideAttack != 1 and type(self.target) != int:
            if self.up:
                aPowerfulTorpedo = torpedo(self.x+self.width/2,self.y +2,self.name,self,self.target,2)
            elif self.left:
                aPowerfulTorpedo = torpedo(self.x+2,self.y + self.width/2-5,self.name,self,self.target,2)
            elif self.right:
                aPowerfulTorpedo = torpedo(self.x+self.width-2,self.y + self.width/2-5,self.name,self,self.target,2)
            else:
                aPowerfulTorpedo = torpedo(self.x+self.width/2,self.y +self.height-2,self.name,self,self.target,2)

            self.projectiles.append(aPowerfulTorpedo)
            pygame.mixer.Channel(6).play(torpedoFired, maxtime=1805)
            projectileList.append(aPowerfulTorpedo)
            self.torpTimer = 90

        if self.suicideAttack == 1:
            self.healthTarget = 0
            self.invisCall = 0
            self.fireCall = 0
            self.amplifyCall = 0
            self.suicideExplosionTimer -= 1

        if self.suicideExplosionTimer <= 0:
            self.health = 0

        if self.target == 0:
            poTargets = [a for a in objectList if a.name in alliedTeam and not isinstance(a,shield)]
            if len(poTargets) > 0:
                self.target = poTargets[random.randint(0,len(poTargets)-1)]

                

        #DISPLAYS THE CORRECT SHIP IN THE CORRECT STATE IN THE CORRECT ANIMATION COUNTER CORRECTLY
        if self.invisible <= 0:      
            if conditions[2]:
                window.blit(enemyShip[2][self.enemyAnimCounter//2], (self.x,self.y))
            elif conditions[3]:
                window.blit(enemyShip[3][self.enemyAnimCounter//2], (self.x,self.y))
            elif conditions[0]:
                window.blit(enemyShip[0][self.enemyAnimCounter//2], (self.x,self.y))
            elif conditions[1]:
                window.blit(enemyShip[1][self.enemyAnimCounter//2], (self.x,self.y))
            self.enemyAnimCounter += 1
        else:
            if conditions[2]:
                window.blit(enemyShipInvis[2], (self.x,self.y))
            elif conditions[3]:
                window.blit(enemyShipInvis[3], (self.x,self.y))
            elif conditions[0]:
                window.blit(enemyShipInvis[0], (self.x,self.y))
            elif conditions[1]:
                window.blit(enemyShipInvis[1], (self.x,self.y))

        #Increments the animation counter

        if self.enemyAnimCounter >= 34:
            self.enemyAnimCounter = 0
        #Resets the animation counter to prevent an IndexError

        #If below 20% health, set to suicide mode
        if self.target != 0 and self.health / self.orgHealth <= 0.2 and self.suicideAttack == 0 and self.alreadyCollided == 0 and self.target.invisible <= 0:
            self.speed -= self.speed / 2.3
            #The acceleration will be extremely fast, so gives the player some advanced warning by lowering the speed temporarily
            self.healthTarget = 0
            self.invisCall = 0
            self.amplifyCall = 0
            self.fireCall = 0
            self.suicideAttack = 1


   
        attackPatterns = [self.attackPatternLeft,self.attackPatternRight,self.attackPatternTop,self.attackPatternSouth]


        
        if self.invisCall == 0 and self.fireCall == 0 and self.amplifyCall == 0 and self.healthTarget == 0 or self.invisCall == 0 and self.amplifyCall == 0 and self.fireCall == 0 and self.health > self.orgHealth * 0.52: 
            #Attack patterns - enemy will go towards the player, fire and then retreat back so it can fire again- must do this in all directions
            for x in attackPatterns:
                if x == 1:
                    pattern = attackPatterns[attackPatterns.index(x)]
                #Activates the attack patterns
            try:
                #Occasionally this will backfire for an unknown reason, so a try command is needed to prevent a crash
                if pattern == 1:
                    if self.runTimer == 0 and self.part2 != 1:
                        self.runTimer = 14
                        #Borrows the runtimer code to retreat backwards because I'm too lazy to implement unique code
                    if self.part2 == 1 and self.runTimer == 0:
                        #Ready for round 2?
                        self.attackPatternLeft = 0
                        self.attackPatternRight = 0
                        self.attackPatternTop = 0
                        self.attackPatternSouth = 0
                        self.myRand = 0
                        self.part2 = 0
                        #Too lazy to implement new code for attacking, so just let it use regular attack code

                    elif self.myRand == 0:
                        self.myRand = random.randint(2,3) #RandomVar1
                        self.randomNum = self.myRand      #RandomVar2
                        #2 random vars are needed - one stores the random value, the other makes sure that it stays constant per frame (otherwise it would change at each frame)
                    elif self.runTimer == 1 and self.part2 != 1:
                        self.runTimer = 1500
                        self.randomNum = 1
                        #Sets the runtimer to an arbitrarily large number for the overall retreat
                    elif self.runTimer > 1449 and self.runTimer < 1501:
                        #If this is complete, set part2 as 1
                        self.part2 = 1
                    else:
                        if self.part2 == 1:
                            if self.myRand == 2:
                                self.randomNum = 3
                            #Sets the random number to 3 if myRand == 2
                            elif self.myRand == 3:
                                self.randomNum = 2
                            #Sets the random number to 2 if myRand == 3

                            #The reason for these inversions is so that it will go back in the opposite direction it retreated before, so that the overall position relative to player stays the same
                            if self.runTimer > 1000:
                                self.runTimer = 14
                            #Resets the run timer
            except:
                pass



            #AFK TIMER - If the player goes AFK, this code will allow the enemy to just go up to the player to destroy them without any manoeuvres - timer is 70 frames 
            if type(self.target) != int:
                if self.afkTimer == 70:
                    self.enemyMemoryX = self.target.x
                    self.enemyMemoryY = self.target.y
                    self.afkTimer = 69
                    #Remembers the position of the player - For every tick that this does not change, the timer will decrement down to 0
                if not isinstance(self.target, spaceStation) and self.enemyMemoryX == self.target.x and self.enemyMemoryY == self.target.y and self.afkTimer > 0:
                    self.afkTimer -= 1
                #Decrements the tick if player remains AFK
                if self.enemyMemoryX != self.target.x or self.enemyMemoryY != self.target.y:
                    self.afkTimer = 70
                #If player moves, resets the timer

                if self.afkTimer == 0 and self.target in objectList and self.suicideAttack != 1 and self.healthTarget == 0:
                    enemy.fireGuns(self,self.target)
                    #If the timer decrements to 0, the player is AFK and the enemy will move to attack immediately
                    
                if self.suicideAttack == 1:
                    number = 3.5 / self.suicideAcceleration
                    #This variable is responsible for increasing the number of explosions as time progresses
                    if random.randint(1,10) < 3.5 * self.speed / number:
                        self.hits.append(explosionEffect(random.randint(10,self.width // 1.2),random.randint(10,self.height // 1.2),1))
                    #Shows many explosions on the enemy ship for cosmetic effect and to warn the player that it is suicide charging

                    self.speed = self.speed * self.suicideAcceleration
                    #Accelerates the enemy every tick so that the player cannot escape

                    #This code moves the enemy towards the player position in the fastest possible way
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


                #If player is destroyed before the suicide attack can complete, resets the focus so that it is not chasing ghosts
                if self.target != 0 and self.target.health <= 0:
                    self.target = 0
                    self.suicideAttack = 0


                #If not suiciding and not running away from nearby ships, this is the main code function
                if self.runTimer <= 0:
                    if self.suicideAttack != 1 and self.target != 0:
                        #If x-coordinate is the same, examine y coordinate
                        if self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                            #IF THE TARGET IS BELOW
                            if self.target.y > self.y + self.enemyRange:
                                self.down = True
                                self.right = False
                                self.left = False
                                self.up = False
                                enemy.fireGuns(self,self.target)
                            #Triggers attack pattern, if y-coordinate is closer than x-coordinate
                            elif self.target.y > self.y and abs(self.y - self.target.y) > abs(self.x - self.target.x):
                                self.attackPatternSouth = 1
                            #IF THE TARGET IS ABOVE
                            if self.target.y < self.y - self.enemyRange:
                                self.down = False
                                self.right = False
                                self.left = False
                                self.up = True
                                enemy.fireGuns(self,self.target)
                            #Triggers attack pattern, if y-coordinate is closer than x-coordinate
                            elif self.target.y < self.y and abs(self.y - self.target.y) > abs(self.x - self.target.x):
                                self.attackPatternTop = 1
                            
                        #Same as above, but with y-coordinate being the same and x-coordinate being different
                        elif self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                            #Enemy is to the RIGHT
                            if self.target.x > self.x + self.enemyRange:
                                self.down = False
                                self.right = True
                                self.left = False
                                self.up = False
                                enemy.fireGuns(self,self.target)
                            #Triggers attack pattern, if x-coordinate is closer than y-coordinate
                            elif self.target.x > self.x and abs(self.y - self.target.y) < abs(self.x - self.target.x):
                                self.attackPatternLeft = 1
                            #Enemy is to the LEFT
                            if self.target.x < self.x - self.enemyRange:
                                self.down = False
                                self.right = False
                                self.left = True
                                self.up = False
                                enemy.fireGuns(self,self.target)
                            #Triggers attack pattern, if x-coordinate is closer than y-coordinate
                            elif self.target.x < self.x  and abs(self.y - self.target.y) < abs(self.x - self.target.x):
                                self.attackPatternRight = 1

                        #This code triggers if the enemy is not within a similar x or y coordinate - must move to reach a similar x/y-coordinate
                        else:
                            #The firstAttack attribute is set to 0, so that as soon as it reaches a close position it can fire (to prevent the player from strafing)
                            self.firstAttack = 0

                            #Enemy is to the RIGHT, but y-distance is greater than x-distance
                            if self.target.x > self.x and abs(self.target.y - self.y) > abs(self.target.x - self.x):
                                if self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                                    pass
                                else:
                                    self.x += self.speed #Moves right
                                    self.right = True
                                    self.left = False
                                    self.up = False
                                    self.down = False
                            #Enemy is to the LEFT, but y-distance is greater than x-distance
                            elif self.target.x < self.x and abs(self.target.y - self.y) > abs(self.target.x - self.x):
                                if self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                                    pass
                                else:
                                    self.x -= self.speed #Moves left
                                    self.right = False
                                    self.left = True
                                    self.up = False
                                    self.down = False
                            #Enemy is BELOW, but x-distance is greater than y-distance
                            elif self.target.y > self.y and abs(self.target.y - self.y) < abs(self.target.x - self.x):
                                if self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                                    pass
                                else:
                                    self.y += self.speed #Moves down
                                    self.right = False
                                    self.left = False
                                    self.up = False
                                    self.down = True
                            #Enemy is ABOVE, but x-distance is greater than y-distance
                            elif self.target.y < self.y and abs(self.target.y - self.y) < abs(self.target.x - self.x):
                                if self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                                    pass
                                else:
                                    self.y -= self.speed #Moves up
                                    self.right = False
                                    self.left = False
                                    self.up = True
                                    self.down = False



   
    #Reference- ENEMYSHIPFIREGUNS

    def fireGuns(self, target):

        #Regular animation - object does not become invisible when firing
        if self.invisible <= 0:
            if self.left:
                window.blit(enemyShip[2][self.enemyAnimCounter//2], (self.x,self.y))
                self.up = False
                self.down = False
                self.right = False
            elif self.right:
                window.blit(enemyShip[3][self.enemyAnimCounter//2], (self.x,self.y))
                self.left = False
                self.up = False
                self.down = False
            elif self.up:
                window.blit(enemyShip[0][self.enemyAnimCounter//2], (self.x,self.y))
                self.left = False
                self.right = False
                self.down = False
            else:
                window.blit(enemyShip[1][self.enemyAnimCounter//2], (self.x,self.y))
                self.up = False
                self.left = False
                self.right = False
        else:
            if self.left:
                window.blit(enemyShipInvis[2], (self.x,self.y))
                self.up = False
                self.down = False
                self.right = False
            elif self.right:
                window.blit(enemyShipInvis[3], (self.x,self.y))
                self.left = False
                self.up = False
                self.down = False
            elif self.up:
                window.blit(enemyShipInvis[0], (self.x,self.y))
                self.left = False
                self.right = False
                self.down = False
            else:
                window.blit(enemyShipInvis[1], (self.x,self.y))
                self.up = False
                self.left = False
                self.right = False



        
        self.attackTimer -= 1
        #The ship can only fire when the attackTimer is a specific number - this prevents it from firing infinitely

        self.afkTimeDelay += 1
        #This also restricts the ship from firing infinitely, but is reserved for when player is AFK
        #Much lower than regular attack timer

        if self.afkTimeDelay == 10:
            self.afkTimeDelay = 0
        #Resets the time delay so can fire again


        #Can ONLY fire upon these conditions
        if self.afkTimer == 0 and self.runTimer == 0 and self.randomNum == 0 and self.attackPatternLeft != 1 and self.attackPatternRight != 1 and self.attackPatternSouth != 1 and self.attackPatternTop != 1:    
            #Same code as before, but this time if player is AFK
            if target.y + 25 > self.y and target.y - 25 < self.y:
                #AFK player is to the RIGHT
                if target.x > self.x:
                    self.left = False
                    self.right = True
                    self.up = False
                    self.down = False
                    #Can only fire if time delay is 0
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x + self.width, self.y + self.height / 2, 1,self.name,self)
                        self.horProjectiles.append(spaceBullet)

                        projectileList.append(spaceBullet)
                #AFK player is to the LEFT
                elif target.x < self.x:
                    self.left = True
                    self.right = False
                    self.up =  False
                    self.down = False
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x, self.y+ self.height / 2, -1, self.name,self)
                        self.horProjectiles.append(spaceBullet)

                        projectileList.append(spaceBullet)
                #Accounts for any unexpected errors

            #Same as above
            elif target.x + 25 > self.x and target.x - 25 < self.x:
                #AFK player is BELOW
                if target.y > self.y:
                    self.left = False
                    self.right = False
                    self.up = False
                    self.down = True 
                    #Same as above - can only fire when timeDelay = 0
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height, 1, self.name,self)
                        self.projectiles.append(spaceBullet)
                #AFK player is ABOVE
                elif target.y < self.y:
                    self.left = False
                    self.right = False
                    self.up = True
                    self.down = False
                    if self.afkTimeDelay == 0:
                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y, -1, self.name,self)
                        self.projectiles.append(spaceBullet)
                try:
                    projectileList.append(spaceBullet)
                    pygame.mixer.Channel(random.randint(1,2)).play(enemyFire, maxtime=600)

                except:
                    pass
                    #Accounts for unexpected errors
            else:

                #Player is AFK, but not yet in a position to fire - needs to move to the correct position in the fastest possible time
                if target.x > self.x:# and abs(o.y - self.y) < abs(o.x - self.x): 
                    #Above is commented code I implemented earlier which didn't work well, but could still be used later
                    if target.y + 25 > self.y and target.y - 25 < self.y:
                        pass #Do not move if you are already in good position to fire at the AFK player
                    else:
                        #Moves RIGHT to the AFK player
                        self.x += self.speed
                        self.right = True
                        self.left = False
                        self.up = False
                        self.down = False
                elif target.x < self.x:# and abs(o.y - self.y) < abs(o.x - self.x):
                    if target.y + 25 > self.y and target.y - 25 < self.y:
                        pass #Do not move if you are already in good position to fire at the AFK player
                    else:
                        #Moves LEFT to the AFK player
                        self.x -= self.speed
                        self.right = False
                        self.left = True
                        self.up = False
                        self.down = False
                elif target.y > self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                    if target.x + 25 > self.x and target.x - 25 < self.x:
                        pass #Same as above
                    else:
                        #Moves DOWN to the AFK player
                        self.y += self.speed
                        self.right = False
                        self.left = False
                        self.up = False
                        self.down = True
                elif target.y < self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                    if target.x + 25 > self.x and target.x - 25 < self.x:
                        pass #Same as above
                    else:
                        #Moves UP to the AFK player
                        self.y -= self.speed
                        self.right = False
                        self.left = False
                        self.up = True
                        self.down = False

        if self.attackTimer <= 0:
            self.attackTimer = 21
        #Resets attack timer so can fire again

        #player is NOT AFK
        if self.afkTimer > 0:
            #If within shooting range by y-coordinate
            if target.y + 25 > self.y and target.y  - 25 < self.y:
                if target.x > self.x + self.enemyRange: #Player is to the RIGHT
                    self.x += self.speed #Moves towards the enemy while firing to execute attack pattern
                    if self.attackTimer == 19 or self.firstAttack == 0 or self.attackTimer == 8: #Can only fire if attackTimer = 19 or if it's the first attack
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x + self.width, self.y + self.height / 2, 1, self.name,self)
                            self.horProjectiles.append(spaceBullet)
                        else:
                            spaceBullet = enemyProjectile(self.x + self.width, self.y + self.height / 2, 1, self.name,self) 
                            self.horProjectiles.append(spaceBullet)
                        #Fires the projectile against the player, adds the projectile to the local projectile list
                    
                #Player is to the LEFT
                if target.x < self.x - self.enemyRange:
                    self.x -= self.speed #Moves LEFT towards the enemy while firing to execute attack pattern
                    if self.attackTimer == 19 or self.firstAttack == 0  or self.attackTimer == 8: #Can only fire if attackTimer = 19 or if it's the first attack
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x, self.y+ self.height / 2, -1, self.name,self)
                            self.horProjectiles.append(spaceBullet)
                        else:
                            spaceBullet = enemyProjectile(self.x, self.y+ self.height / 2, -1, self.name,self)
                            self.horProjectiles.append(spaceBullet)
                            #Fires the projectile against the player, adds the projectile to the local projectile list
                self.firstAttack = 1 #first attack so that the enemy can shoot as soon as the player is in

            #If within shooting range by x-coordinate
            elif target.x + 25 > self.x and target.x - 25 < self.x:

                #Player is BELOW
                if target.y > self.y + self.enemyRange:
                    self.y += self.speed #Moves towards the player to execute pattern...
                    if self.attackTimer == 19 or self.firstAttack == 0  or self.attackTimer == 8: #Same as above
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x + self.width / 2, self.y + self.height / 2, 1, self.name,self)
                            self.projectiles.append(spaceBullet)
                        else:
                            spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, 1, self.name,self)
                            self.projectiles.append(spaceBullet)
                        #Same as above

                #Player is ABOVE
                if target.y < self.y - self.enemyRange:
                    self.y -= self.speed #...
                    if self.attackTimer == 19 or self.firstAttack == 0  or self.attackTimer == 8: #Same as above
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x + self.width / 2, self.y + self.height / 2, -1, self.name,self)
                            self.projectiles.append(spaceBullet)
                        else:
                            spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, -1, self.name,self)
                            self.projectiles.append(spaceBullet)
                        #...
                self.firstAttack = 1
                #Sets the first attack to 1 so that it cannot fire bullets every single tick of the clock
            
            try:
                projectileList.append(spaceBullet)
                pygame.mixer.Channel(random.randint(1,2)).play(enemyFire, maxtime=600)
                #Adds the projectile to the OVERALL projectile list
            except:
                pass
            #Accounts for any unexpected errors

class carrier(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Enemy ship",96,96,random.randint(150,winWidth-150),random.randint(150,winHeight-150),1000,1000,0.6,2,[],[],False,False,True,False,0,24)

        self.fighterTimer = 0
        self.fighterList = []
        self.torpTimer = 28
        self.tolerance = 87

    def draw(self,window):
        self.counter += 1

        for f in self.fighterList:
            if f.health <= 0:
                self.fighterList.remove(f)

        if self.invisible <= 0:
            if self.up:
                window.blit(carrierBlit[0][self.counter],(self.x,self.y))
            elif self.right:
                window.blit(carrierBlit[1][self.counter],(self.x,self.y))
            elif self.down:
                window.blit(carrierBlit[2][self.counter],(self.x,self.y))
            else:
                window.blit(carrierBlit[3][self.counter],(self.x,self.y))
        else:
            if self.up:
                window.blit(carrierInvis[0],(self.x,self.y))
            elif self.right:
                window.blit(carrierInvis[1],(self.x,self.y))
            elif self.down:
                window.blit(carrierInvis[2],(self.x,self.y))
            else:
                window.blit(carrierInvis[3],(self.x,self.y))


        if self.counter >= 16:
            self.counter = 0 

        if self.target != 0 and self.target.health <= 0:
            self.target = 0

        if self.target == 0:
            potentialTargets = [a for a in objectList if a.name in alliedTeam]
            if len(potentialTargets) > 0:
                self.target = potentialTargets[random.randint(0,len(potentialTargets)-1)]

        self.fighterTimer -= 1
        self.torpTimer -= 1

        if self.fighterTimer <= 0 and len(self.fighterList) < 5:
            aMostAnnoyingEnemy = fighter(1,1,1,self.x+self.width/2,self.y+self.height/2,1,1,1,1,1,1,1,1,1,1)
            objectList.append(aMostAnnoyingEnemy)
            self.fighterList.append(aMostAnnoyingEnemy)
            self.fighterTimer = 180

        if self.torpTimer <= 0:
            decision = random.randint(1,3)
            if decision == 1:
                if self.up:
                    aPowerfulTorpedo = torpedo(self.x+47,self.y+25,self.name,self,self.target,2)
                elif self.right:
                    aPowerfulTorpedo = torpedo(self.x+70,self.y+47,self.name,self,self.target,2)
                elif self.down:
                    aPowerfulTorpedo = torpedo(self.x+47,self.y+70,self.name,self,self.target,2)
                else:
                    aPowerfulTorpedo = torpedo(self.x+25,self.y+47,self.name,self,self.target,2)
            elif decision == 2:
                if self.up:
                    aPowerfulTorpedo = torpedo(self.x+34,self.y+74,self.name,self,self.target,2)
                elif self.right:
                    aPowerfulTorpedo = torpedo(self.x+20,self.y+34,self.name,self,self.target,2)
                elif self.down:
                    aPowerfulTorpedo = torpedo(self.x+60,self.y+20,self.name,self,self.target,2)
                else:
                    aPowerfulTorpedo = torpedo(self.x+74,self.y+60,self.name,self,self.target,2)
            else:
                if self.up:
                    aPowerfulTorpedo = torpedo(self.x+60,self.y+74,self.name,self,self.target,2)
                elif self.right:
                    aPowerfulTorpedo = torpedo(self.x+20,self.y+60,self.name,self,self.target,2)
                elif self.down:
                    aPowerfulTorpedo = torpedo(self.x+34,self.y+20,self.name,self,self.target,2)
                else:
                    aPowerfulTorpedo = torpedo(self.x+74,self.y+34,self.name,self,self.target,2)
            pygame.mixer.Channel(6).play(torpedoFired, maxtime=1805)
            self.projectiles.append(aPowerfulTorpedo)
            projectileList.append(aPowerfulTorpedo)
            self.torpTimer = 28


 





    def fireGuns(self):
        if len(self.projectiles) + len(self.horProjectiles) < 5:
            if self.up:
                projBullet = enemyProjectile(self.x+47, self.y+10,-1,self.name,self )
                projBullet2 = enemyProjectile(self.x+13, self.y+35,-1,self.name,self )
                projBullet3 = enemyProjectile(self.x+4, self.y+55,-1,self.name,self )
                projBullet4 = enemyProjectile(self.x+82, self.y+35,-1,self.name,self )
                projBullet5 = enemyProjectile(self.x+91, self.y+55,-1,self.name,self )
                #Fires from the correct position on the ship, using the value variables defined above
                self.projectiles.append(projBullet)
                self.projectiles.append(projBullet2)
                self.projectiles.append(projBullet3)
                self.projectiles.append(projBullet4)
                self.projectiles.append(projBullet5)
                #Adds to the projectile list so they can be tracked
            elif self.down:
                projBullet = enemyProjectile(self.x+71, self.y+47,1,self.name,self )
                projBullet2 = enemyProjectile(self.x+60, self.y+13,1,self.name,self )
                projBullet3 = enemyProjectile(self.x+40, self.y+4,1,self.name,self )  
                projBullet4 = enemyProjectile(self.x+60, self.y+82,1,self.name,self )   
                projBullet5 = enemyProjectile(self.x+40, self.y+91,1,self.name,self )  
                self.projectiles.append(projBullet)
                self.projectiles.append(projBullet2)
                self.projectiles.append(projBullet3)
                self.projectiles.append(projBullet4)
                self.projectiles.append(projBullet5)
                #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
            elif self.left:
                projBullet = enemyProjectile(self.x+24,self.y+47  ,-1,self.name,self )
                projBullet2 = enemyProjectile(self.x+35,self.y+13  ,-1,self.name,self )
                projBullet3 = enemyProjectile(self.x+55,self.y+4 ,-1,self.name,self )    
                projBullet4 = enemyProjectile(self.x+35,self.y+82 ,-1,self.name,self )    
                projBullet5 = enemyProjectile(self.x+55,self.y+91 ,-1,self.name,self )    
                self.horProjectiles.append(projBullet)
                self.horProjectiles.append(projBullet2)
                self.horProjectiles.append(projBullet3)
                self.horProjectiles.append(projBullet4)
                self.horProjectiles.append(projBullet5)
                #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
            else:
                projBullet = enemyProjectile(self.x+71,self.y+47  ,1,self.name,self )
                projBullet2 = enemyProjectile(self.x+60,self.y+13  ,1,self.name,self )
                projBullet3 = enemyProjectile(self.x+40,self.y+4  ,1,self.name,self )
                projBullet4 = enemyProjectile(self.x+60,self.y+82  ,1,self.name,self )
                projBullet5 = enemyProjectile(self.x+40,self.y+91  ,1,self.name,self )
                self.horProjectiles.append(projBullet)
                self.horProjectiles.append(projBullet2)
                self.horProjectiles.append(projBullet3)
                self.horProjectiles.append(projBullet4)
                self.horProjectiles.append(projBullet5)
                #Same as above

            projectileList.append(projBullet)
            projectileList.append(projBullet2)
            projectileList.append(projBullet3)
            projectileList.append(projBullet4)
            projectileList.append(projBullet5)
            pygame.mixer.Channel(0).play(enemyFire, maxtime=600)
            pygame.mixer.Channel(0).play(enemyFire, maxtime=600)


            #SEPARATE FIRE PROJECTILES TAB
            if self.fireBoost > 0:
                if len(self.fireProjectiles) <= 0:
                    if self.up:
                        fireProj = powerfulProjectile(self.x + self.width // 2 - 6 , self.y-24,-1 , self.name,self)
                        self.projectiles.append(fireProj)
                        self.fireProjectiles.append(fireProj)
                    elif self.down:
                        fireProj = powerfulProjectile(self.x + self.width // 2 - 6, self.y + self.height,1 , self.name,self)
                        self.projectiles.append(fireProj)
                        self.fireProjectiles.append(fireProj)
                    elif self.left:
                        fireProj = powerfulProjectile(self.x - 24, self.y + self.height // 2 -6 ,-1 , self.name,self)
                        self.horProjectiles.append(fireProj)
                        self.fireProjectiles.append(fireProj)
                    else:
                        fireProj = powerfulProjectile(self.x + self.width, self.y + self.height // 2 -6,1 , self.name,self)
                        self.horProjectiles.append(fireProj)
                        self.fireProjectiles.append(fireProj)

                    projectileList.append(fireProj)

    
        

        














class fighter(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("EnemyS",32,32,x,y,32,32,0.15,10,[],[],False,False,True,False,0,28)

        self.shootingTimer = 16
        self.fired = 0
        self.numberOfTimesFired = 0
        self.runPhase1 = 9999
        self.runPhase2 = -1
        self.shootingTime = 7
        self.patterns = [0,0,0,0]
        self.decision = 0
        self.reversed = 0

    def draw(self,window):

        self.counter += 1

        if self.invisible <= 0:
            if self.up:
                window.blit(fighterBlit[0][self.counter//2],(self.x,self.y))
            elif self.right:
                window.blit(fighterBlit[1][self.counter//2],(self.x,self.y))
            elif self.down:
                window.blit(fighterBlit[2][self.counter//2],(self.x,self.y))
            else:
                window.blit(fighterBlit[3][self.counter//2],(self.x,self.y))
        else:
            if self.up:
                window.blit(fighterInvis[0],(self.x,self.y))
            elif self.right:
                window.blit(fighterInvis[1],(self.x,self.y))
            elif self.down:
                window.blit(fighterInvis[2],(self.x,self.y))
            else:
                window.blit(fighterInvis[3],(self.x,self.y))

        if self.counter >= 32:
            self.counter = 0 

        if self.target != 0 and self.target.health <= 0:
            self.target = 0
            

            


        if self.target == 0:
            potentialTargets = [a for a in objectList if a.name in alliedTeam]
            if len(potentialTargets) > 0:
                self.target = potentialTargets[random.randint(0,len(potentialTargets)-1)]

        if self.shootingTimer <= 0: 
            self.fired = 0

        if self.runPhase1 <= 0 and self.runPhase2 == -1 and self.target != 0 :
            self.runPhase2 = int(300 / (abs(self.target.x  + self.target.width / 2 - self.x - self.width / 2 )+1) ) * self.speed

        if self.runPhase2 > 0:
            self.runPhase2 -= 1

        if self.runTimer <= 0 and self.healthTarget == 0:


            if self.patterns[0] == 1:
                if self.reversed == 1 and self.runPhase2 ==0 and self.runPhase1 == 0:
                    self.patterns[0] = 0
                    self.decision = 0
                    self.numberOfTimesFired = 0
                    self.fired = 0
                    self.runPhase2 = -1
                    self.runPhase1 = 9999
                    self.reversed = 0
                if self.runPhase1 > 0:
                    self.runPhase1 -= 1
                    self.x += self.speed * self.decision
                    if self.decision * self.speed > 0:
                        self.right = True
                        self.left = False
                        self.up = False
                        self.down = False
                    else:
                        self.left = True
                        self.right = False
                        self.down = False
                        self.up = False
                elif self.runPhase2 > 0:
                    if self.y + self.width + self.speed < winHeight:
                        self.y += self.speed
                    else:
                        self.reversed = 1
                        self.runPhase2 = 0
                    self.down = True
                    self.up = False
                    self.left = False
                    self.right = False
                elif self.runPhase2 == 0:
                    self.decision -= 2 * self.decision
                    self.runPhase1 = 10
                    self.reversed = 1
                else: 
                    self.reversed = 1
                    self.runPhase2 = 0
                    self.runPhase1 = 0

            if self.patterns[2] == 1:
                if self.reversed == 1 and self.runPhase2 ==0 and self.runPhase1 == 0:
                    self.patterns[2] = 0
                    self.decision = 0
                    self.numberOfTimesFired = 0
                    self.fired = 0
                    self.runPhase2 = -1
                    self.runPhase1 = 9999
                    self.reversed = 0
                if self.runPhase1 > 0:
                    self.runPhase1 -= 1
                    self.x += self.speed * self.decision
                    if self.decision * self.speed > 0:
                        self.right = True
                        self.left = False
                        self.up = False
                        self.down = False
                    else:
                        self.left = True
                        self.right = False
                        self.down = False
                        self.up = False
                elif self.runPhase2 > 0:
                    if self.y - self.speed > 0:
                        self.y -= self.speed
                    else:
                        self.reversed = 1
                        self.runPhase2 = 0
                    self.down = False
                    self.up = True
                    self.left = False
                    self.right = False
                elif self.runPhase2 == 0:
                    self.decision -= 2 * self.decision
                    self.runPhase1 = 10
                    self.reversed = 1
                else: 
                    self.reversed = 1
                    self.runPhase2 = 0
                    self.runPhase1 = 0

            if self.patterns[1] == 1:
                if self.reversed == 1 and self.runPhase2 ==0 and self.runPhase1 == 0:
                    self.patterns[1] = 0
                    self.decision = 0
                    self.numberOfTimesFired = 0
                    self.fired = 0
                    self.runPhase2 = -1
                    self.runPhase1 = 9999
                    self.reversed = 0
                if self.runPhase1 > 0:
                    self.runPhase1 -= 1
                    self.y += self.speed * self.decision
                    if self.decision * self.speed > 0:
                        self.right = False
                        self.left = False
                        self.up = False
                        self.down = True
                    else:
                        self.left = False
                        self.right = False
                        self.down = False
                        self.up = True
                elif self.runPhase2 > 0:
                    if self.x - self.speed > 0:
                        self.x -= self.speed
                    else:
                        self.reversed = 1
                        self.runPhase2 = 0
                    self.down = False
                    self.up = False
                    self.left = True
                    self.right = False
                elif self.runPhase2 == 0:
                    self.decision -= 2 * self.decision
                    self.runPhase1 = 10
                    self.reversed = 1
                else: 
                    self.reversed = 1
                    self.runPhase2 = 0
                    self.runPhase1 = 0

            if self.patterns[3] == 1:
                if self.reversed == 1 and self.runPhase2 ==0 and self.runPhase1 == 0:
                    self.patterns[3] = 0
                    self.decision = 0
                    self.numberOfTimesFired = 0
                    self.fired = 0
                    self.runPhase2 = -1
                    self.runPhase1 = 9999
                    self.reversed = 0
                if self.runPhase1 > 0:
                    self.runPhase1 -= 1
                    self.y += self.speed * self.decision
                    if self.decision * self.speed > 0:
                        self.right = False
                        self.left = False
                        self.up = False
                        self.down = True
                    else:
                        self.left = False
                        self.right = False
                        self.down = False
                        self.up = True
                elif self.runPhase2 > 0:
                    if self.x + self.width + self.speed <= winWidth:
                        self.x += self.speed
                    else:
                        self.reversed = 1
                        self.runPhase2 = 0
                    self.down = False
                    self.up = False
                    self.left = False
                    self.right = True
                elif self.runPhase2 == 0:
                    self.decision -= 2 * self.decision
                    self.runPhase1 = 10
                    self.reversed = 1
                else: 
                    self.reversed = 1
                    self.runPhase2 = 0
                    self.runPhase1 = 0





        if len([a for a in self.patterns if a == 1]) == 0 and self.target != 0:
            if abs(self.y + self.height / 2 - self.target.y - self.target.height / 2) <= 25 and abs(self.target.x - self.x) > 140:
                self.shootingTimer -= 1
                if self.target.x - self.x > 140 and self.numberOfTimesFired < 3: # right
                    self.x += self.speed
                    self.right = True
                    self.up = False
                    self.down = False
                    self.left = False
                    if self.fired == 0:
                        self.fired = 1
                        fighter.fireGuns(self)
                        self.shootingTimer = self.shootingTime
                        self.numberOfTimesFired += 1
                elif self.x - self.target.x > 140 and self.numberOfTimesFired < 3: # left
                    self.x -= self.speed
                    self.left = True
                    self.up = False
                    self.right = False
                    self.down = False
                    if self.fired == 0:
                        self.fired = 1
                        fighter.fireGuns(self)
                        self.shootingTimer = self.shootingTime
                        self.numberOfTimesFired += 1
            elif abs(self.x + self.width / 2 - self.target.x - self.target.width / 2) <= 25 and abs(self.target.y - self.y) > 140:
                self.shootingTimer -= 1
                if self.target.y - self.y > 140 and self.numberOfTimesFired < 3: # below
                    self.y += self.speed
                    self.right = False
                    self.up = False
                    self.down = True
                    self.left = False
                    if self.fired == 0:
                        fighter.fireGuns(self)
                        self.shootingTimer = self.shootingTime
                        self.fired = 1
                        self.numberOfTimesFired += 1
                elif self.y - self.target.y > 140 and self.numberOfTimesFired < 3: # above
                    self.y -= self.speed
                    self.left = False
                    self.up = True
                    self.right = False
                    self.down = False
                    if self.fired == 0:
                        self.fired = 1
                        fighter.fireGuns(self)
                        self.shootingTimer = self.shootingTime
                        self.numberOfTimesFired += 1

            else:
                if self.target.x > self.x:# and abs(o.y - self.y) < abs(o.x - self.x):
                    if self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                        pass
                    else:
                        self.x += self.speed #Moves RIGHT
                        self.right = True
                        self.left = False
                        self.up = False
                        self.down = False
                elif self.target.x < self.x:# and abs(o.y - self.y) < abs(o.x - self.x):
                    if self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                        pass
                    else:
                        self.x -= self.speed #MOVES LEFT
                        self.right = False
                        self.left = True
                        self.up = False
                        self.down = False
                elif self.target.y > self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                    if self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                        pass
                    else:
                        self.y += self.speed #MOVES DOWN
                        self.right = False
                        self.left = False
                        self.up = False
                        self.down = True
                elif self.target.y < self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                    if self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                        pass
                    else:
                        self.y -= self.speed #MOVES UP
                        self.right = False
                        self.left = False
                        self.up = True
                        self.down = False
                        
            if (self.numberOfTimesFired >= 3 and self.decision == 0) or math.hypot(self.target.x+self.target.width/2-self.x-self.width/2,self.target.y+self.target.height/2-self.y-self.height/2) < 155:
                self.decision = random.randint(3,4)
                if self.decision == 3:
                    self.decision = -1
                else:
                    self.decision = 1

                self.runPhase1 = 10

                
                if abs(self.y + self.height / 2 - self.target.y - self.target.height / 2) <= 35 and self.x > self.target.x: #enemy is left
                    self.patterns[3] = 1
                elif abs(self.y + self.height / 2 - self.target.y - self.target.height / 2) <= 35 and self.x < self.target.x: #enemy is right
                    self.patterns[1] = 1
                elif abs(self.x + self.width / 2 - self.target.x - self.target.width / 2) <= 35 and self.y > self.target.y: #enemy is above
                    self.patterns[0] = 1

                else:
                    self.patterns[2] = 1

                
            



    def fireGuns(self):
        #Only fires if total number of projectiles <= 4
        if self.up:
            projBullet = enemyProjectile(self.x+self.width/2-1, self.y-5,-1,self.name,self )
            projBullet2 = enemyProjectile(self.x+30, self.y+16,-1,self.name,self )
            projBullet3 = enemyProjectile(self.x+1, self.y+16,-1,self.name,self )
            #Fires from the correct position on the ship, using the value variables defined above
            self.projectiles.append(projBullet)
            self.projectiles.append(projBullet2)
            self.projectiles.append(projBullet3)
            #Adds to the projectile list so they can be tracked
        elif self.down:
            projBullet = enemyProjectile(self.x+self.width/2-1, self.y+self.height,1,self.name,self )
            projBullet2 = enemyProjectile(self.x+30, self.y+15,1,self.name,self )
            projBullet3 = enemyProjectile(self.x+1, self.y+15,1,self.name,self )   
            self.projectiles.append(projBullet)
            self.projectiles.append(projBullet2)
            self.projectiles.append(projBullet3)
            #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
        elif self.left:
            projBullet = enemyProjectile(self.x-8,self.y+self.height/2  ,-1,self.name,self )
            projBullet2 = enemyProjectile(self.x+16,self.y+30  ,-1,self.name,self )
            projBullet3 = enemyProjectile(self.x+16,self.y+1 ,-1,self.name,self )    
            self.horProjectiles.append(projBullet)
            self.horProjectiles.append(projBullet2)
            self.horProjectiles.append(projBullet3)
            #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
        else:
            projBullet = enemyProjectile(self.x+self.width,self.y+self.height/2  ,1,self.name,self )
            projBullet2 = enemyProjectile(self.x+15,self.y+30  ,1,self.name,self )
            projBullet3 = enemyProjectile(self.x+15,self.y+1  ,1,self.name,self )
            self.horProjectiles.append(projBullet)
            self.horProjectiles.append(projBullet2)
            self.horProjectiles.append(projBullet3)
            #Same as above

        pygame.mixer.Channel(random.randint(1,2)).play(littleShoot, maxtime=600)
        projectileList.append(projBullet)
        projectileList.append(projBullet2)
        projectileList.append(projBullet3)
        #SEPARATE FIRE PROJECTILES TAB
        if self.fireBoost > 0:
            if len(self.fireProjectiles) <= 0:
                if self.up:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6 , self.y-24,-1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.down:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6, self.y + self.height,1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.left:
                    fireProj = powerfulProjectile(self.x - 24, self.y + self.height // 2 -6 ,-1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                else:
                    fireProj = powerfulProjectile(self.x + self.width, self.y + self.height // 2 -6,1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)

                projectileList.append(fireProj)







                

                








class frigate(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("EnemyS",48,48,random.randint(50,winWidth),random.randint(50,winHeight),48,48,0.25,5,[],[],False,False,True,False,0,28)

        self.target = 0
        self.tolerance = 35


    def draw(self,window):

        self.counter += 1

        if self.invisible > 0:
            if self.up:
                window.blit(frigateInvis[0],(self.x,self.y))
            elif self.right:
                window.blit(frigateInvis[1],(self.x,self.y))
            elif self.down:
                window.blit(frigateInvis[2],(self.x,self.y))
            else:
                window.blit(frigateInvis[3],(self.x,self.y))
        else:
            if self.up:
                window.blit(frigateAnim[0][self.counter//2],(self.x,self.y))
            elif self.right:
                window.blit(frigateAnim[1][self.counter//2],(self.x,self.y))
            elif self.down:
                window.blit(frigateAnim[2][self.counter//2],(self.x,self.y))
            else:
                window.blit(frigateAnim[3][self.counter//2],(self.x,self.y))

        if self.counter >= 32:
            self.counter = 0

    def fireGuns(self):
        if len(self.projectiles) + len(self.horProjectiles) <= 1:
            #Only fires if total number of projectiles <= 4
            if self.up:
                projBullet = enemyProjectile(self.x+self.width/2-1, self.y-5,-1,self.name,self )
                #Fires from the correct position on the ship, using the value variables defined above
                self.projectiles.append(projBullet)
                #Adds to the projectile list so they can be tracked
            elif self.down:
                projBullet = enemyProjectile(self.x+self.width/2-1, self.y+self.height,1,self.name,self )
                self.projectiles.append(projBullet)
                #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
            elif self.left:
                projBullet = enemyProjectile(self.x-8,self.y+self.height/2  ,-1,self.name,self )
                self.horProjectiles.append(projBullet)
                #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
            else:
                projBullet = enemyProjectile(self.x+self.width,self.y+self.height/2  ,1,self.name,self )
                self.horProjectiles.append(projBullet)
                #Same as above

            pygame.mixer.Channel(random.randint(1,2)).play(enemyFire, maxtime=600)
            projectileList.append(projBullet)
            #SEPARATE FIRE PROJECTILES TAB
        if self.fireBoost > 0:
            if len(self.fireProjectiles) <= 0:
                if self.up:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6 , self.y-24,-1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.down:
                    fireProj = powerfulProjectile(self.x + self.width // 2 - 6, self.y + self.height,1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.left:
                    fireProj = powerfulProjectile(self.x - 24, self.y + self.height // 2 -6 ,-1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                else:
                    fireProj = powerfulProjectile(self.x + self.width, self.y + self.height // 2 -6,1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)

                projectileList.append(fireProj)








class miner(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("EnemyS",48,48,random.randint(50,winWidth),random.randint(50,winHeight),48,48,0.2,6,[],[],False,False,True,False,0,36) 
        #Initialises miner stats

        #All attributes will be explained where they are used
        self.timingVariable = 0    
        self.direction = 0
        self.mapEdgeConstraint = 0
        self.mineTimer = 0
        self.mineTimer2 = 0
        self.mineSpeedDeceleration = 0.9875
        self.mineStatus = 0
        self.orgSpeed = self.speed
        self.mineTimeout = 0
        self.mineCooldown = 450
        self.target = 0 
        self.projectiles = []
        self.givenThreshold = 90
        self.animationCount = 0
        self.attackDecision = random.randint(0,1) #Initial decision is random, see attackDecision attribute later
        self.rememberOrgSpeed = 0



    #THE FIREGUNS CODE FOR THE MINER SHIP IS VIRTUALLY IDENTICAL TO THAT OF THE ENEMY SHIP - Search "Enemyshipfireguns"" via CTRL+F
    def fireGuns(self,target):
        if self.invisible <= 0:
            if self.up:
                window.blit(minerBlit[2][self.animationCount//3],(self.x,self.y))
                self.down = False
                self.left = False
                self.right = False     
            elif self.down:
                window.blit(minerBlit[3][self.animationCount//3],(self.x,self.y))
                self.up = False
                self.left = False
                self.right = False     
            elif self.left:
                window.blit(minerBlit[0][self.animationCount//3],(self.x,self.y))
                self.up = False
                self.down = False
                self.right = False     
            else:
                window.blit(minerBlit[1][self.animationCount//3],(self.x,self.y))
                self.up = False
                self.down = False
                self.left = False
                self.right = True  
        else:
            if self.up:
                window.blit(minerBlitInvis[1],(self.x,self.y))
                self.down = False
                self.left = False
                self.right = False     
            elif self.down:
                window.blit(minerBlitInvis[0],(self.x,self.y))
                self.up = False
                self.left = False
                self.right = False     
            elif self.left:
                window.blit(minerBlitInvis[2],(self.x,self.y))
                self.up = False
                self.down = False
                self.right = False     
            else:
                window.blit(minerBlitInvis[3],(self.x,self.y))
                self.up = False
                self.down = False
                self.left = False
                self.right = True  


        self.attackTimer -= 1

        if self.attackTimer < 0:
            self.firstAttack = 0
            self.attackTimer = 20

        if self.runTimer <= 0:
            if target.y + 25 > self.y and target.y - 25 < self.y:
                if target.x > self.x:
                    if target.x - self.x > self.givenThreshold:
                        self.x += self.speed 
                    if self.attackTimer == 12 or self.firstAttack == 0:
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x + self.width, self.y + self.height / 2, 1, self.name,self)
                        else:
                            spaceBullet = enemyProjectile(self.x + self.width, self.y + self.height / 2, 1, self.name,self)
                        self.horProjectiles.append(spaceBullet)
                    
                elif target.x < self.x:
                    if self.x - target.x > self.givenThreshold:
                            self.x -= self.speed 
                    if self.attackTimer == 12 or self.firstAttack == 0:
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x, self.y+ self.height / 2, -1, self.name,self)
                        else:
                            spaceBullet = enemyProjectile(self.x, self.y+ self.height / 2, -1, self.name,self)
                        self.horProjectiles.append(spaceBullet)
                self.firstAttack = 1

            elif target.x + 25 > self.x and target.x - 25 < self.x:
                if target.y > self.y:
                    if target.y - self.y > self.givenThreshold:
                        self.y += self.speed
                    if self.attackTimer == 12 or self.firstAttack == 0:
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x + self.width / 2, self.y + self.height / 2, 1, self.name,self)
                        else:
                            spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, 1, self.name,self)
                        self.projectiles.append(spaceBullet)

                elif target.y < self.y:
                    if self.y - target.y > self.givenThreshold:
                        self.y -= self.speed
                    if self.attackTimer == 12 or self.firstAttack == 0:
                        if self.fireBoost > 0 and len(self.projectiles) + len(self.horProjectiles) <= 0:
                            spaceBullet = powerfulProjectile(self.x + self.width / 2, self.y + self.height / 2, -1, self.name,self)
                        else:
                            spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height / 2, -1, self.name,self)
                        self.projectiles.append(spaceBullet)
                self.firstAttack = 1

            
            
            try:
                projectileList.append(spaceBullet)
            except:
                pass 

    #No comments above as this is duplicate code
    

    def draw(self,window):
        #Draws the miner ship as usual


        self.animationCount += 1
        if self.animationCount >= 42:
            self.animationCount = 0
            #Resets the miner animation count to prevent IndexError

        #Displays the miner ship and its animation correctly 
        if self.invisible <= 0:
            if self.up:
                window.blit(minerBlit[2][self.animationCount//3],(self.x,self.y))
                self.down = False
                self.left = False
                self.right = False     
            elif self.down:
                window.blit(minerBlit[3][self.animationCount//3],(self.x,self.y))
                self.up = False
                self.left = False
                self.right = False     
            elif self.left:
                window.blit(minerBlit[0][self.animationCount//3],(self.x,self.y))
                self.up = False
                self.down = False
                self.right = False     
            else:
                window.blit(minerBlit[1][self.animationCount//3],(self.x,self.y))
                self.up = False
                self.down = False
                self.left = False
                self.right = True  
        else:
            if self.up:
                window.blit(minerBlitInvis[1],(self.x,self.y))
                self.down = False
                self.left = False
                self.right = False     
            elif self.down:
                window.blit(minerBlitInvis[0],(self.x,self.y))
                self.up = False
                self.left = False
                self.right = False     
            elif self.left:
                window.blit(minerBlitInvis[2],(self.x,self.y))
                self.up = False
                self.down = False
                self.right = False     
            else:
                window.blit(minerBlitInvis[3],(self.x,self.y))
                self.up = False
                self.down = False
                self.left = False
                self.right = True 

        if self.runTimer <= 0: 

            if self.healthTarget != 0 and (self.health < self.orgHealth * 0.52 or self.invisCall == 1 or self.fireCall == 1 or self.amplifyCall == 1):# or self.healthTarget != 0 and self.invisCall == 1 or self.healthTarget != 0 and self.fireCall == 1:
                if self.speed != self.orgSpeed:
                    self.rememberOrgSpeed = self.speed
                    self.speed = self.orgSpeed
            else:
                if self.rememberOrgSpeed != 0:
                    self.speed = self.rememberOrgSpeed
                    self.rememberOrgSpeed = 0
                if self.mineStatus == 1:
                    miner.deployMine(self)
                    #Deploys a mine if the conditional attribute, mineStatus, is satisfied

                #The attack decision attr determines whether the miner will choose to attack the player or travel around the map to set mines

                elif self.mineStatus == 0 and self.attackDecision != 1 and len(mineList) < 4 * minerCount and self.runTimer <= 0: 
                    if self.mineTimeout >= 1:
                        self.mineTimeout -= 1
                        #The cooldown for deploying a mine decrements by 1 each tick of the clock
                    
                    #Determines which direction the miner will go
                    if self.direction == 0:
                        self.mapEdgeConstraint = random.randint(100,650)
                        #Randomly determines how far in that direction the miner will travel
                        self.timingVariable = 50 + random.randint(10,500)
                        #Randomly determines for how long in that direction the miner will travel (minimum 50 frames)
                        self.direction = random.randint(1,4)
                        #Randomly determines which direction the miner will travel
                        
                        #This code examines which direction has been chosen, then goes in that direction
                        if self.direction == 1:
                            self.up = True
                            self.down = False
                            self.left = False
                            self.right = False
                        elif self.direction == 2:
                            self.down = True
                            self.up = False
                            self.left = False
                            self.right = False
                        elif self.direction == 3:
                            self.left = True
                            self.up = False
                            self.down = False
                            self.right = False
                        else:
                            self.right = True
                            self.up = False
                            self.down = False
                            self.left = False
                    
                    #IF FACING A DIRECTION AND NOT RUNNING
                    elif self.direction != 0:
                        #Uses a random variable to prevent the player from predicting when mines will be deployed
                        if random.randint(1,125) == 69 and self.mineTimeout == 0 and len(mineList) < 4 * minerCount: 
                            #Cannot deploy mines if there are more than 4x the number of mines as miners
                            self.mineTimer = 120
                            self.mineStatus = 1
                            return

                        #IF FACING A DIRECTION, NOT RUNNING, MOVES IN THAT DIRECTION
                        if self.direction == 1 and self.y - self.speed - self.mapEdgeConstraint >= 0:
                            self.y -= self.speed
                            self.up = True
                            self.down = False
                            self.left = False
                            self.right = False
                        elif self.direction == 2 and self.y + self.speed + self.height + self.mapEdgeConstraint <= winHeight:
                            self.y += self.speed
                            self.up = False
                            self.down = True
                            self.left = False
                            self.right = False
                        elif self.direction == 3 and self.x - self.speed - self.mapEdgeConstraint >= 0:
                            self.x -= self.speed
                            self.up = False
                            self.down = False
                            self.left = True
                            self.right = False
                        elif self.direction == 4 and self.x + self.speed + self.width + self.mapEdgeConstraint <= winWidth:
                            self.x += self.speed
                            self.up = False
                            self.down = False
                            self.left = False
                            self.right = True
                        else:
                            self.direction = 0 #Removes the direction
                        #End of above statement


                    if self.timingVariable >= 1:
                        self.timingVariable -= 1
                        #Decrements the timing variable
                    else:
                        self.direction = 0
                        #If the timing variable expires, sets new direction

                #ATTACK MODE       
                else:
                    if self.mineTimeout >= 1:
                        self.mineTimeout -= 1
                    #Decrements the mine cooldown attr

                    if self.target != 0 and self.target.health <= 0:
                        self.target = 0
                    #Sets target as neutral if previous target has been destroyed, so it does not chase ghosts

                    if random.randint(1,125) == 69 and self.mineTimeout == 0 and len(mineList) < 4 * minerCount:
                            self.mineTimer = 120
                            self.mineStatus = 1
                            return
                        
                    #Above code reused for this status, otherwise the miner would never deploy mines in attack mode


                    #SELECTS A TARGET
                    if self.target == 0:
                        poTargets = [a for a in objectList if a.name in alliedTeam and not isinstance(a,shield)]
                        if len(poTargets) > 0:
                            self.target = poTargets[random.randint(0,len(poTargets)-1)]

                
                    #THE CODE BELOW IS IDENTICAL IN STRUCTURE TO THE CODE FOR THE ENEMY SHIP - Search "Enemy(Ship)" via CTRL + F
                    if self.invisCall == 0 and self.target != 0 and self.healthTarget == 0 and self.fireCall == 0 and self.amplifyCall == 0 or self.amplifyCall == 0 and self.fireCall == 0 and self.health > self.orgHealth * 0.52 and self.target !=0 and self.invisCall == 0 : 
                        if abs(self.target.x - self.x) < 25 and self.runTimer < 1:
                            if self.target.y < self.y: #ENEMY IS BELOW
                                self.up = True
                                self.down = False
                                self.left = False
                                self.right = False
                                miner.fireGuns(self,self.target)
                            elif self.target.y > self.y: #ENEMY IS ABOVE
                                self.up = False
                                self.down = True
                                self.left = False
                                self.right = False
                                miner.fireGuns(self,self.target)
                        elif abs(self.target.y - self.y) < 25 and self.runTimer < 1:
                            if self.target.x > self.x: #ENEMY IS TO THE RIGHT
                                self.right = True
                                self.left = False
                                self.up = False
                                self.down = False
                                miner.fireGuns(self,self.target)
                            elif self.target.x < self.x: #ENEMY IS TO THE LEFT
                                self.left = True
                                self.right = False
                                self.up = False
                                self.down = False
                                miner.fireGuns(self,self.target)
                        else:
                            #moving towards the target

                            #Same y-coordinate, different x-coordinates
                            if self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                                if self.target.x > self.x: #ENEMY IS TO THE RIGHT
                                    self.left = False
                                    self.right = True
                                    self.up = False
                                    self.down = False
                                    if self.afkTimeDelay == 0:
                                        spaceBullet = enemyProjectile(self.x + self.width, self.y + self.height / 2, 1,self.name,self)
                                        self.horProjectiles.append(spaceBullet)
                                if self.target.x < self.x: # ENEMY IS TO THE LEFT
                                    self.left = True
                                    self.right = False
                                    self.up =  False
                                    self.down = False
                                    if self.afkTimeDelay == 0:
                                        spaceBullet = enemyProjectile(self.x, self.y+ self.height / 2, -1, self.name,self)
                                        self.horProjectiles.append(spaceBullet)

                                    projectileList.append(spaceBullet)

                            #Same x-coordinate, different y-coordinates
                            elif self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                                if self.target.y > self.y: #ENEMY IS BELOW
                                    self.left = False
                                    self.right = False
                                    self.up = False
                                    self.down = True 
                                    if self.afkTimeDelay == 0: #Fires the projectile
                                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y + self.height, 1, self.name,self)
                                        self.projectiles.append(spaceBullet)
                                if self.target.y < self.y: #ENEMY IS ABOVE
                                    self.left = False
                                    self.right = False
                                    self.up = True
                                    self.down = False
                                    if self.afkTimeDelay == 0: #Fires the projectile
                                        #Adds projectile to local list
                                        spaceBullet = enemyProjectile(self.x + self.width / 2, self.y, -1, self.name,self)
                                        self.projectiles.append(spaceBullet)
                                    #Adds projectile to the OVERALL list
                                    projectileList.append(spaceBullet)
                            elif self.runTimer <= 0:
                                #Not yet in position to attack, moving to target
                                if self.target.x > self.x:# and abs(o.y - self.y) < abs(o.x - self.x):
                                    if self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                                        pass
                                    else:
                                        self.x += self.speed #Moves RIGHT
                                        self.right = True
                                        self.left = False
                                        self.up = False
                                        self.down = False
                                elif self.target.x < self.x:# and abs(o.y - self.y) < abs(o.x - self.x):
                                    if self.target.y + 25 > self.y and self.target.y - 25 < self.y:
                                        pass
                                    else:
                                        self.x -= self.speed #MOVES LEFT
                                        self.right = False
                                        self.left = True
                                        self.up = False
                                        self.down = False
                                elif self.target.y > self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                                    if self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                                        pass
                                    else:
                                        self.y += self.speed #MOVES DOWN
                                        self.right = False
                                        self.left = False
                                        self.up = False
                                        self.down = True
                                elif self.target.y < self.y:# and abs(o.y - self.y) > abs(o.x - self.x):
                                    if self.target.x + 25 > self.x and self.target.x - 25 < self.x:
                                        pass
                                    else:
                                        self.y -= self.speed #MOVES UP
                                        self.right = False
                                        self.left = False
                                        self.up = True
                                        self.down = False


                        



    def deployMine(self):
        if self.runTimer == 0: #If not running away

            #IF MOVING UP
            if self.up:
                self.down = False
                self.left = False
                self.right = False  
                if self.y - self.speed >= 0: #Checks if it can move left
                    self.y -= self.speed  
                else:
                    self.direction = 0
                    self.mineStatus = 0
                    self.speed = self.orgSpeed
                    if self.mineTimer <= 0:
                        self.mineTimeout = self.mineCooldown #Adds the cooldown again and stops
                    return
            
            #IF MOVING DOWN
            elif self.down:
                self.up = False
                self.left = False
                self.right = False
                if self.y + self.speed + self.height <= winHeight: #Checks if it can move down
                    self.y += self.speed   
                else:
                    self.direction = 0
                    self.mineStatus = 0
                    self.speed = self.orgSpeed
                    if self.mineTimer <= 0:
                        self.mineTimeout = self.mineCooldown #Adds the cooldown again and stops
                    return  

            #IF MOVING LEFT
            elif self.left:
                self.up = False
                self.down = False
                self.right = False  
                if self.x - self.speed >= 0: #Checks if it can move left
                    self.x -= self.speed   
                else:
                    self.direction = 0
                    self.mineStatus = 0
                    self.speed = self.orgSpeed
                    if self.mineTimer <= 0:
                        self.mineTimeout = self.mineCooldown #Same as above
                    return

            #IF MOVING RIGHT
            else:
                self.up = False
                self.down = False
                self.left = False
                self.right = True
                if self.x + self.speed + self.width <= winWidth: #Checks if it can move right 
                    self.x += self.speed
                else:
                    self.direction = 0
                    self.mineStatus = 0
                    self.speed = self.orgSpeed
                    if self.mineTimer <= 0:
                        self.mineTimeout = self.mineCooldown #...
                    return

            self.mineTimer -= 1
            #Decrements the mineTImer


            if self.mineTimer > 0:
                self.speed = self.speed * self.mineSpeedDeceleration
                #For every tick of the Minetimer, decelerates the ship so it can deploy the mine
            elif self.mineTimer == 0:
                mineList.append(mine(self.x + self.width / 2,self.y + self.height / 2,self.name))
                #Deploys the actual mine 
            elif self.mineTimer < 0:
                self.mineTimer2 += 1
                self.speed = self.speed / self.mineSpeedDeceleration
                #Now that the mine is deployed, begins to re-accelerate the miner ship back to original speed
            if self.mineTimer2 > 120:
                #Resets speed back to original, in case it is not already back at full speed
                self.speed = self.orgSpeed
                self.mineStatus = 0
                self.mineTimer = 0
                self.mineTimer2 = 0
                self.mineTimeout = self.mineCooldown
                # ^ - RESETS ALL NECESSARY CONDITIONAL ATTRIBUTES
                if self.attackDecision == 0:
                    self.attackDecision = 1
                    #If previously scanning the map, begins attacking
                    return
                if self.attackDecision == 1:
                    self.attackDecision = 0
                    #If previously attacking, begins scanning the map
                    return
                return
        else:
            #Resets all necessary attributes
            if self.mineTimer <= 0:
                self.mineTimeout = self.mineCooldown
                #resets the cooldown
            self.mineStatus = 0
            self.mineTimer = 0
            self.mineTimer2 = 0
            self.speed = self.orgSpeed
            #resets variables


class shield():
    def __init__(self, name , x , y , orientation, actualWidth,  actualHeight, health,orgHealth,healthRecovery,orgHealthRecovery, owner):
        self.name = name
        self.x = x
        self.y = y    
        self.orientation = orientation
        self.actualWidth = actualWidth
        self.actualHeight = actualHeight
        self.width = 1
        self.height = 1
        self.health = health
        self.orgHealth = orgHealth
        self.healthRecovery = healthRecovery
        self.orgHealthRecovery = orgHealthRecovery
        self.owner = owner
        self.underAttackTime = 0
        self.invisible = 0
        self.damages = []
        self.hits = []
        self.alreadyCollided = 0
        self.projectiles = []
        self.horProjectiles = []
        self.fireProjectiles = []
        self.mitigation = 0.1
        self.leeway = 10
        self.floating = 0

        if self.orientation in [1,3]:
            self.width = self.actualWidth
            self.height = self.actualHeight
        else:
            self.width = self.actualHeight
            self.height = self.actualWidth

        self.hitbox = (self.x,self.y,self.width,self.height)

    def floatAnimation(self):
        self.floating += 1


        if self.floating <= 40:
            self.y += 0.2
        elif 40 < self.floating <= 80:
            self.y -= 0.2
        if self.floating > 80:
            self.floating = 0

    def basicFunctions(self,window):

        if self.underAttackTime > 0:
            self.underAttackTime -= 1

        shield.floatAnimation(self)

        self.healthRecovery -= 1

        if self.healthRecovery <= 0:
            self.healthRecovery = self.orgHealthRecovery #hp recovery reaches 0, add health and reset cooldown
            if self.health + 1 <= self.orgHealth:
                self.health = self.orgHealth

        if self.owner.health <= 0:
            objectList.remove(self) 


class enemyS(shield):
    def __init__(self,name,x,y,orientation,actualWidth,actualHeight,health,orgHealth,healthRecovery,orgHealthRecovery,owner):
        super().__init__("EnemyS",x,y,orientation,150,150,220,220,420,420,owner)

        self.animCounter = 0

    def draw(self,window):
        if self.animCounter >= 20:
            self.animCounter = 0

        if self.health > 0 and self.underAttackTime == 0:
            window.blit(enemyShields[self.animCounter],(self.x,self.y))

        elif self.health > 0: #UNDER ATTACK BLITS
            window.blit(enemyShieldsUA,(self.x,self.y))



class friendlyS(shield):
    def __init__(self, name , x , y , orientation, actualWidth,  actualHeight, health,orgHealth,healthRecovery,orgHealthRecovery,owner):
        super().__init__("Friendly",x,y,orientation,16,119,100,100,360,360,owner)

        self.animCounter = 0

    def draw(self,window):
        self.animCounter += 1

        
        if self.animCounter >= 72:
            self.animCounter = 0

        if self.health > 0 and self.underAttackTime == 0:
            if self.orientation == 0:
                window.blit(shields[0][self.animCounter//3],(self.x,self.y))
            elif self.orientation == 1:
                window.blit(shields[1][self.animCounter//3],(self.x,self.y))
            elif self.orientation == 2:
                window.blit(shields[2][self.animCounter//3],(self.x,self.y))
            else:
                window.blit(shields[3][self.animCounter//3],(self.x,self.y))

        elif self.health > 0: #UNDER ATTACK BLITS
            if self.orientation == 0:
                window.blit(shieldsUA[0],(self.x,self.y))
            elif self.orientation == 1:
                window.blit(shieldsUA[1],(self.x,self.y))
            elif self.orientation == 2:
                window.blit(shieldsUA[2],(self.x,self.y))
            else:
                window.blit(shieldsUA[3],(self.x,self.y))









    

class mine():
    def __init__(self,x,y,owner):
        #Initialises all attributes and their stats
        self.x = x
        self.y = y
        self.owner = owner
        self.invisTimer = 350
        self.cloakingCheck = 0
        self.cloakingAnim = 0
        self.blinkTimer = 0
        self.blinkPeriod = 90
        self.blinking = 0
        self.blinkingTime = 12 
        self.radius = 32
        self.explosionDamage = 50
        self.health = 20

    #Draws the mine
    def draw(self,window):
        global currentLives
        #Checks if it is time for the mine to cloak
        if self.cloakingCheck == 0:
            if self.invisTimer >= 1:
                window.blit(mineBlitStill, (self.x,self.y))
                #Displays the mine before activation, as the mine has not yet activated and cloaked
                self.invisTimer -= 1
            elif self.invisTimer == 0: #Time to cloak
                try:
                    #Shows the mine cloaking animation
                    window.blit(mineBlitAnim[self.cloakingAnim // 3],(self.x,self.y))
                    self.cloakingAnim += 1
                except:
                    self.cloakingCheck = 1
                #Try-except to account for any unexpected errors
        
        else:
            #MINE IS NOW ACTIVATED
            for o in [a for a in objectList if a.name in alliedTeam]:
                if math.hypot(abs(self.x-o.x)-8,abs(self.y-o.y)-8) <= self.radius:
                    #If the player gets within a certain radius
                    BOOM.append(shipExploding(self.x,self.y))
                    #Displays the mine explosion
                    #Displays the healthbar of the damaged player
                    if o.invisible <= 0:
                        if o.health > self.explosionDamage:
                            o.health -= self.explosionDamage
                            o.damagedCount = 100
                            #Damages the player for the given damage stat
                        else:
                            o.health = 0
                            
                    if self in mineList:        
                        mineList.remove(self)
                    #Removes the mine from the overall tracking list


            


            #DISPLAYS THE MINE BLINKING so the player can see it
            if self.blinking >= 1:
                window.blit(mineBlitBlink,(self.x,self.y))
                self.blinking -= 1
                #Decrements the actual blinking duration 
            

            if self.blinkTimer == 0:
                #Resets the blink cooldown
                self.blinking = self.blinkingTime
                self.blinkTimer = self.blinkPeriod
            else:
                self.blinkTimer -= 1
                #Decrements the blink timer





class enemyProjectile():
    def __init__(self,x,y,side,owner,ownerID):
        #Initialises the projectile and its stats
        self.x = x
        self.y = y
        self.width = 1
        self.height = 12
        self.speed = 25 * side
        self.damage = 4
        self.critChance = 20
        self.owner = owner
        self.ownerID = ownerID
        self.aliveTimer = 165
        
        if isinstance(self.ownerID, malevolent):
            self.damage = 7
    
        if self.owner == "EnemyS":
            #I was too lazy to give the miner its own projectile, so I just nerfed its stats if the projectile comes from a miner
            self.speed = 20 * side
            self.damage = 3
            self.critChance = 10

        if self.ownerID.amplified > 0:
            self.speed *= 1.75
            self.damage *= 1.75
            self.critChance *= 1.75


    #Drawing the projectiles vertically
    def draw(self,window):
        if isinstance(self.ownerID,fighter):
            window.blit(fighterProjectiles[1],(self.x,self.y))
        else:
            window.blit(enemyProjectiles[0], (self.x,self.y))
        self.y += self.speed  #Moves the projectile by the speed value
        if self.y > winHeight or self.y < 0:
            if self in projectileList:
                projectileList.remove(self)
            #Removes the projectile if it goes out of bounds to reduce any potential lag
            #Accounts for any unexpected errors
        if self not in projectileList:
            #if removed from the projectileList, must also be removed from the local lists
            self.ownerID.projectiles.remove(self)
                        #Removes the projectiles from the owner's local projectile list
            #Same as above

    #Drawing the projectiles horizontally
    def draw2(self,window):
        #IDENTICAL STRUCTURE AS ABOVE, JUST HORIZONTAL
        if isinstance(self.ownerID,fighter):
            window.blit(fighterProjectiles[0],(self.x,self.y))
        if not isinstance(self.ownerID,fighter):
            window.blit(enemyProjectiles[1], (self.x,self.y))
        self.x += self.speed
        if self in projectileList and (self.x > winWidth or self.x < 0):
            projectileList.remove(self)
        if self not in projectileList:
            self.ownerID.horProjectiles.remove(self)

class powerfulProjectile():
    def __init__(self,x,y,side,owner,ownerID):
        #Initialises the projectile and its stats
        self.x = x
        self.y = y
        self.width = 25
        self.height = 13
        self.side = side
        self.speed = 20 * self.side
        self.damage = 25
        self.critChance = 50
        self.owner = owner
        self.ownerID = ownerID
        self.aliveTimer = 165

        if self.ownerID.amplified > 0:
            self.speed *= 1.75
            self.damage *= 1.75
            self.critChance *= 1.75

        

    #Drawing the projectiles vertically
    def draw(self,window):
        if self.side == -1:
            window.blit(fireProjectile[0],(self.x,self.y))
        else:
            window.blit(fireProjectile[1],(self.x,self.y))   

        self.y += self.speed  #Moves the projectile by the speed value
        if self.y > winHeight or self.y < 0:
            if self in projectileList:
                projectileList.remove(self)
                #Removes the projectile if it goes out of bounds to reduce any potential lag

            #Accounts for any unexpected errors
        if self not in projectileList:
            #if removed from the projectileList, must also be removed from the local lists
            if self in self.ownerID.projectiles:
                self.ownerID.projectiles.remove(self)
            if self in self.ownerID.fireProjectiles:
                self.ownerID.fireProjectiles.remove(self)
                    #Removes the projectiles from the owner's local projectile list                  
            #Same as above

    #Drawing the projectiles horizontally
    def draw2(self,window):
        #IDENTICAL STRUCTURE AS ABOVE, JUST HORIZONTAL
        if self.side == -1:
            window.blit(fireProjectile[2],(self.x,self.y))
        else:
            window.blit(fireProjectile[3],(self.x,self.y))

        self.x += self.speed
        if self.x > winWidth or self.x < 0:
            if self in projectileList:
                projectileList.remove(self)

        if self not in projectileList:
            if self in self.ownerID.horProjectiles:
                self.ownerID.horProjectiles.remove(self)
            if self in self.ownerID.fireProjectiles:
                self.ownerID.fireProjectiles.remove(self)
class powerUp():
    def __init__(self,name,x,y,animCounterRefresh):
        self.name = name
        self.x = x
        self.y = y
        self.animCounterRefresh = animCounterRefresh
        self.animCounterH = 0
        self.timeRemaining = 800
        self.floating = 0

    def floatAnimation(self):
        self.floating += 1


        if self.floating <= 40:
            self.y += 0.2
        elif 40 < self.floating <= 80:
            self.y -= 0.2
        if self.floating > 80:
            self.floating = 0




class buff():
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        self.animCounter = 0
        self.timeRemaining = 800
        self.floating = 0

    def floatAnimation(self):
        self.animCounter += 1

        if self.animCounter >= 54:
            self.animCounter = 0

        if self.floating <= 40:
            self.y += 0.25
        elif 40 < self.floating <= 80:
            self.y -= 0.25
        if self.floating > 80:
            self.floating = 0

        if self.timeRemaining <= 0:
            buffList.remove(self)

        

class reinforcements(buff):
    def __init__(self,name,x,y):
        super().__init__("help",random.randint(20,winWidth-20),random.randint(20,winHeight - 20))

    def draw(self,window):

        window.blit(reinforcementsBlit[self.animCounter//2],(self.x,self.y))

        self.timeRemaining -= 1
        self.floating += 1
        
        for o in [a for a in objectList if a.name in alliedTeam]:
            if math.hypot(o.x + o.width / 2- self.x, o.y + o.height / 2- self.y) < 55:
                for x in range(random.randint(2,5)):
                    if random.randint(1,2) == 1:
                        objectList.append(annoraxN(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
                    else:
                        objectList.append(playerN(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
                if self in buffList:
                    pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
                    buffList.remove(self)
                        

class extraLife(buff):
    def __init__(self,name,x,y):
        super().__init__("lives",random.randint(20,winWidth-20),random.randint(20,winHeight - 20))

    def draw(self,window):
        global currentLives

        window.blit(healthBuffBlit[self.animCounter//2],(self.x,self.y))

        self.timeRemaining -= 1
        self.floating += 1


        for o in [a for a in objectList if a.name in alliedTeam]:
            if math.hypot(o.x + o.width / 2- self.x, o.y + o.height / 2- self.y) < 55:
                o.health = o.orgHealth
                currentLives += 1
                if self in buffList:
                    pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
                    buffList.remove(self)


class extraScore(buff):
    def __init__(self,name,x,y):
        super().__init__("score",random.randint(20,winWidth-20),random.randint(20,winHeight - 20))

    def draw(self,window):
        global score

        window.blit(scoreBlit[self.animCounter//2],(self.x,self.y))

        self.timeRemaining -= 1
        self.floating += 1


        for o in [a for a in objectList if a.name in alliedTeam]:
            if math.hypot(o.x + o.width / 2- self.x, o.y + o.height / 2- self.y) < 55:
                score += 25000
                if self in buffList:
                    pygame.mixer.Channel(7).play(powerUpEffect, maxtime=600)
                    buffList.remove(self)


    
class invisPowerUp(powerUp):
    def __init__(self,name,x,y,animCounterRefresh):
        super().__init__("invis",x,y,52)

        self.distanceList = []
        self.nameList = []
        self.target = 0

    def draw(self,window):
        global score
        self.animCounterH += 1
        self.timeRemaining -= 1
        if self.animCounterH >= self.animCounterRefresh: 
            self.animCounterH = 0

        
        window.blit(invis[int(self.animCounterH)],(self.x,self.y))

        if self.timeRemaining <= 0:
            powerUpList.remove(self)

        if self.target != 0 and self.target.health <= 0:
            self.target = 0

        
        if len(self.distanceList) > 0 and self.target == 0: 
            self.target = self.nameList[self.distanceList.index(min(self.distanceList))]
            self.target.healthTarget = self
            self.target.invisCall = 1

        for o in [a for a in objectList if not isinstance(a, shield) and not isinstance(a, spaceStation)]:
            if o.healthTarget == 0 and o.invisible <= 0 and o.runTimer <= 0:
                self.distanceList.append(math.hypot(o.x-self.x,o.y-self.y))
                self.nameList.append(o)





            if math.hypot(o.x-self.x,o.y-self.y) < 45:
                o.invisible += 501
                if o.name in alliedTeam:
                    score += 1500
                try:
                    pygame.mixer.Channel(7).play(powerUpEffect, maxtime=1805)
                    powerUpList.remove(self)
                except:
                    pass


class firePowerUp(powerUp):
    def __init__(self,name,x,y,animCounterRefresh):
        super().__init__("fire",x,y,52)

        self.distanceList = []
        self.nameList = []
        self.target = 0


    def draw(self,window):
        global score
        self.animCounterH += 1
        self.timeRemaining -= 1
        if self.animCounterH >= self.animCounterRefresh: 
            self.animCounterH = 0

        
        window.blit(firePower[int(self.animCounterH)],(self.x,self.y))

        if self.timeRemaining <= 0:
            powerUpList.remove(self)

        if self.target != 0 and self.target.health <= 0:
            self.target = 0

        
        if len(self.distanceList) > 0 and self.target == 0: 
            self.target = self.nameList[self.distanceList.index(min(self.distanceList))]
            self.target.healthTarget = self
            self.target.fireCall = 1

        for o in [a for a in objectList if not isinstance(a,spaceStation) and not isinstance(a, shield)]:
            if o.healthTarget == 0 and o.invisible <= 0 and o.runTimer <= 0:
                self.distanceList.append(math.hypot(o.x-self.x,o.y-self.y))
                self.nameList.append(o)

            if math.hypot(o.x-self.x,o.y-self.y) < 45:
                o.fireBoost += 751
                if o.name in alliedTeam:
                    score += 1500
                try:
                    pygame.mixer.Channel(7).play(powerUpEffect, maxtime=1805)
                    powerUpList.remove(self)
                except:
                    pass



class amplifyPowerUp(powerUp):
    def __init__(self,name,x,y,animCounterRefresh):
        super().__init__("amplify",x,y,52)

        self.distanceList = []
        self.nameList = []
        self.target = 0

    def draw(self,window):
        global score
        self.animCounterH += 1
        self.timeRemaining -= 1
        if self.animCounterH >= self.animCounterRefresh: 
            self.animCounterH = 0

        
        window.blit(amplify[int(self.animCounterH)],(self.x,self.y))

        if self.timeRemaining <= 0:
            powerUpList.remove(self)

        if self.target != 0 and self.target not in objectList:
            self.target = 0

        
        if len(self.distanceList) > 0 and self.target == 0: 
            self.target = self.nameList[self.distanceList.index(min(self.distanceList))]
            self.target.healthTarget = self
            self.target.amplifyCall = 1

        for o in [a for a in objectList if not isinstance(a,spaceStation) and not isinstance(a, shield)]:
            if o.healthTarget == 0 and o.invisible <= 0 and o.runTimer <= 0:
                self.distanceList.append(math.hypot(o.x-self.x,o.y-self.y))
                self.nameList.append(o)

            if math.hypot(o.x-self.x,o.y-self.y) < 45:
                if o.amplified <= 0:
                    o.mitigation *= 1.75
                    o.speed *= 1.75
                    o.orgSpeed = o.speed
                    o.orgHealth *= 1.75
                    o.health *= 1.75
                    o.orgHealthRecovery /= 2.5
                o.amplified += 756
                if o.name in alliedTeam:
                    score += 750
                try:
                    pygame.mixer.Channel(7).play(powerUpEffect, maxtime=1805)
                    powerUpList.remove(self)
                except:
                    pass






class healthPowerUp(powerUp):
    def __init__(self,name,x,y,animCounterRefresh):
        super().__init__("health",x,y,52)

    def draw(self,window):
        global score
        self.animCounterH += 1
        self.timeRemaining -= 1
        if self.animCounterH >= self.animCounterRefresh: 
            self.animCounterH = 0

        
        window.blit(health[int(self.animCounterH)],(self.x,self.y))

        if self.timeRemaining <= 0:
            powerUpList.remove(self)


        for o in objectList:
            if math.hypot(o.x-self.x,o.y-self.y) < 45 and o.health != o.orgHealth:
                o.healthRegenTime += 500
                o.damagedCount = 500
                o.health += 40 + 0.5 * o.orgHealth
                if o.name in alliedTeam:
                    score += 750
                if o.health > o.orgHealth:
                    o.health = o.orgHealth
                o.damagedCount = 75
                try:
                    pygame.mixer.Channel(7).play(powerUpEffect, maxtime=1805)
                    powerUpList.remove(self)
                except:
                    pass




class explosionEffect():
    def __init__(self,x,y,type):
        #Initialises the necessary attributes for the explosion
        self.x = x
        self.y = y
        self.type = type
        self.animCounter = 0
        self.randomCheck = 0
        self.randNum = 0 
        self.randNum2 = 0
        #The above random numbers are explained at the beginning of the source code



class shipExploding():
    #Initialises the necessary attributes for the ship explosion
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.boomCycle = 0
        #boomCycle is just the animation counter so the animation can properly render at each given frame

        pygame.mixer.Channel(5).play(shipExplosionFX, maxtime=1805)

    def draw(self,window):
        window.blit(shipExplosion[int(self.boomCycle//9)], (self.x,self.y))
        #Each animation frame is shown 9 times per frame so that it can be seen for a reasonable period of time
        self.boomCycle += 3
        #Standardises the ship explosion rates - previously, the speed of the ship explosion would be dependent on the number of objects in the objectList
        if self.boomCycle >= 90:
            BOOM.remove(self)
            #The animation cycle is finished, so remove from the BOOM list to indicate that it is gone

class damage():
    #The damage is the actual numbers that show above the hit ship to show how much damage was dealt
    def __init__(self,damageCaused,responsibleProjectile,damageOwner,damageOwnerX,isCrit):
        #Initialises the necessary variables - all will be explained where they are used
        self.y = 0
        self.damageCaused = damageCaused
        self.responsibleProjectile = responsibleProjectile
        self.damageOwner = damageOwner
        self.damageOwnerX = damageOwnerX #I have absolutely no idea what this attribute is for, but if I remove it, the game crashes
        self.distance = 2
        self.failCheck = 0
        self.isCrit = isCrit
        self.yCo = 0
        self.corrected = 0
        self.difference = 0
    


    def draw(self,window):
        #Each ship has a damage list
        if self in self.damageOwner.damages and self.damageOwner.damages.index(self) != 0 and self.distance == 0:
            self.distance = self.damageOwner.damages.index(self) - 1
            self.y -= 3
            #The damage numbers go up vertically so that new numbers can be shown
            self.failCheck += 3
            #failCheck in case numbers do not work properly


        try:
            if self.damageOwner.damages[self.damageOwner.damages.index(self)-1].yCo + 10 > self.yCo:
                #If a new damage number is above one of the previous damage numbers, an error has occurred and must be corrected
                self.difference =  10 - abs(self.damageOwner.damages[self.damageOwner.damages.index(self)-1].yCo - self.yCo)
                self.corrected = 1
                #Corrects the error
        except:
            pass
        #Unexpected errors may occur

        try:
            #If the distance to be travelled (upwards) is greater than the index of the damage
            if self.distance > self.damageOwner.damages.index(self):
                self.y -= 3 #Moves the damage up in y-coordinate
                self.failCheck += 3 #Adds 3 to the failCheck in case new damage arrives quickly
            self.distance = self.damageOwner.damages.index(self)
        except:
            for d in self.damageOwner.damages:
                try:
                    #Applies the same code as above, but for multi-digit values (such as 11 or 5! damage)
                    if self in d:
                        if self.distance > self.damageOwner.damages.index(d):
                            self.y -= 3
                            self.failCheck += 3
                        self.distance = self.damageOwner.damages.index(d)
                except:
                    pass

        self.yCo = self.damageOwner.y + self.y - 16 * self.distance #Updates the y-coordinate

        if self.corrected == 1:
            if isinstance(self.damageOwner.damages[self.damageOwner.damages.index(self)-1], list):
                self.damageOwner.damages[self.damageOwner.damages.index(self)-1][0].yCo -= self.difference
                self.damageOwner.damages[self.damageOwner.damages.index(self)-1][1].yCo -= self.difference
            else:
                self.damageOwner.damages[self.damageOwner.damages.index(self)-1].yCo -= self.difference
            #Corrects the error mentioned earlier
            
        #THE CODE BELOW DISPLAYS THE CORRECT DAMAGES CORRECTLY (most of the time)
        if self.damageOwnerX == 1: 
            window.blit(damageCounterAllied[self.damageCaused], (self.damageOwner.x+7.5 + self.damageOwner.width * 0.85,self.yCo))
            if self.isCrit == 1: #Adds an exclamation mark if it's a critical hit
                window.blit(damageCounterAllied[10], (self.damageOwner.x+15 + self.damageOwner.width * 0.85,self.yCo))

        else:
            window.blit(damageCounterAllied[self.damageCaused], (self.damageOwner.x + self.damageOwner.width * 0.85,self.yCo))
            if self.isCrit == 1: #If critical hit
                window.blit(damageCounterAllied[10], (self.damageOwner.x+7.5 + self.damageOwner.width * 0.85,self.yCo))

        self.y -= 0.5 #Moves the damages upwards to fit for new damages

        #If the damages are at so far up, removes the damages
        if self.y < -20 - self.failCheck:
            #Removes single-digit damages
            try:
                self.damageOwner.damages.remove(self)
            except:
                #Removes double-digit damages
                for d in self.damageOwner.damages:
                    try:
                        if self in d:
                            self.damageOwner.damages.remove(d)
                    except:
                        pass


class torpedo():
    def __init__(self,x,y,owner,ownerID,target,option):
        self.x = x
        self.y = y
        self.owner = owner
        self.ownerID = ownerID
        self.target = target
        self.option = option
        self.animCounter = 0
        self.width = 16
        self.height = 16
        self.speed = 25
        self.damage = 20
        self.critChance = 25
        self.aliveTimer = 165
        self.ratioX = 0
        self.ratioY = 0
        if self.target != 0:
            self.ratioX = abs(self.target.x + self.target.width / 2- self.x) / ( abs(self.target.x + self.target.width / 2 - self.x) + abs(self.target.y + self.target.height / 2 - self.y))
            self.ratioY = abs(self.target.y + self.target.height / 2 - self.y) / (abs(self.target.y + self.target.height / 2 - self.y) + abs(self.target.x + self.target.width / 2 - self.x))
        self.horizontalSide = 0
        self.verticalSide = 0

        if self.target != 0:
            if self.target.x > self.x:
                self.horizontalSide = 1
            else:
                self.horizontalSide = -1
            
            if self.target.y > self.y:
                self.verticalSide = 1
            else:
                self.verticalSide = - 1

        if self.owner == "Enemy":
            self.damage = 12
            self.speed = 20
            self.critChance = 15

        if self.ownerID.amplified > 0:
            self.speed *= 1.75
            self.damage *= 1.75
            self.critChance *= 1.75

    def draw(self,window):


        self.animCounter += 1

        window.blit(torpedoAnimation[self.animCounter], (self.x,self.y)) if self.option == 1 else window.blit(enemyTorpAnimation[self.animCounter], (self.x,self.y))

        if self.animCounter >= 18:
            self.animCounter = 0

        self.x += self.speed * self.horizontalSide * self.ratioX
        self.y += self.speed * self.verticalSide * self.ratioY


    
        if self.x > winWidth or self.x < 0 or self.y > winHeight or self.y < 0:
            if self in projectileList:
                projectileList.remove(self)

        if self not in projectileList:
            self.ownerID.projectiles.remove(self)


class rocket():
    def __init__(self,x,y,owner,ownerID,target):
        self.x = x
        self.y = y
        self.owner = owner
        self.ownerID = ownerID
        self.target = target
        self.width = 25
        self.height = 11
        self.speed = 16
        self.damage = 15
        self.critChance = 20
        self.animCounter = 0
        self.aliveTimer = 300
        self.up = False
        self.right = False
        self.left = True
        self.down = False
        self.tolerance = 0.51
        self.targetless = 0
        self.performanceCheck = 0

        if self.ownerID.amplified > 0:
            self.speed *= 1.75
            self.damage *= 1.75
            self.critChance *= 1.75

    def draw(self,window):

        self.animCounter += 1
        self.performanceCheck -= 1

        if self.up:
            window.blit(rocketAnimation[0][self.animCounter],(self.x,self.y))
        elif self.right:
            window.blit(rocketAnimation[1][self.animCounter],(self.x,self.y))
        elif self.down:
            window.blit(rocketAnimation[2][self.animCounter],(self.x,self.y))
        else:
            window.blit(rocketAnimation[3][self.animCounter],(self.x,self.y))

        if self.animCounter >= 22:
            self.animCounter = 0


        if self.target not in objectList or self.target.invisible > 0:
            self.targetless = 1
        if self.targetless == 0:
            



            if self.performanceCheck <= 0:
                self.ratioX = abs(self.target.x + self.target.width / 2- self.x) / ( abs(self.target.x + self.target.width / 2 - self.x) + abs(self.target.y + self.target.height / 2 - self.y))
                self.ratioY = abs(self.target.y + self.target.height / 2 - self.y) / (abs(self.target.y + self.target.height / 2 - self.y) + abs(self.target.x + self.target.width / 2 - self.x))
                self.performanceCheck = 5


            if self.target.x + self.target.width / 2 > self.x + self.target.width / 3:
                self.x += self.speed * self.ratioX
                if self.ratioY <= self.tolerance:
                    self.up = False
                    self.right = True
                    self.down = False
                    self.left = False
            if self.target.x + self.target.width / 2 < self.x - self.target.width / 3:
                self.x -= self.speed * self.ratioX
                if self.ratioY <= self.tolerance:
                    self.up = False
                    self.right = False
                    self.down = False
                    self.left = True
            if self.target.y + self.target.height / 2 > self.y + self.target.width / 3:
                self.y += self.speed * self.ratioY
                if self.ratioX <= self.tolerance:
                    self.up = False
                    self.right = False
                    self.down = True
                    self.left = False
            if self.target.y + self.target.height / 2 < self.y - self.target.width / 3:
                self.y -= self.speed * self.ratioY
                if self.ratioX <= self.tolerance:
                    self.up = True
                    self.right = False
                    self.down = False
                    self.left = False

        else:
            if self.up:
                self.y -= self.speed
            elif self.down:
                self.y += self.speed
            elif self.left:
                self.x -= self.speed
            else:
                self.x += self.speed


        if self.x > winWidth or self.x < 0 or self.y > winHeight or self.y < 0:
            if self in projectileList:
                projectileList.remove(self)

        if self not in projectileList:
            self.ownerID.projectiles.remove(self)


            






class projectile():
    def __init__(self,x,y,side,owner,ownerID):
        #Initialises the stats
        self.x = x
        self.y = y
        self.width = 1
        self.height = 12
        self.side = side
        self.speed = 30 * self.side
        self.damage = 5
        self.critChance = 25
        self.owner = owner
        self.ownerID = ownerID
        self.aliveTimer = 165

        if self.ownerID.amplified > 0:
            self.speed *= 1.75
            self.damage *= 1.75
            self.critChance *= 1.75

    #VERTICAL PROJECTILES
    def draw(self,window):
        if self.side == 1:
            window.blit(bullet, (self.x,self.y)) #Displays the projectile
        else:
            window.blit(bullet4, (self.x,self.y)) #Displays the projectile

        self.y += self.speed #Moves the projectile 
        if self.y > winHeight or self.y < 0: #If the projectiles exit the map
            #Removes the projectiles
            self.ownerID.projectiles.remove(self) 
            if self in projectileList:
                projectileList.remove(self)
        elif self not in projectileList:
            self.ownerID.projectiles.remove(self)


    #HORIZONTAL PROJECTILES - IDENTICAL LOGIC TO VERTICAL PROJECTILES
    def draw2(self,window):
        if self.side == 1:
            window.blit(bullet2, (self.x,self.y)) #Displays the projectile
        else:
            window.blit(bullet3, (self.x,self.y))
        self.x += self.speed #Moves the projectile 
        if self.x > winWidth or self.x < 0:
            self.ownerID.horProjectiles.remove(self)
            if self in projectileList:
                projectileList.remove(self)
        elif self not in projectileList:
            self.ownerID.horProjectiles.remove(self)



        
#Defines the player
play = annoraxPlayable(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)  




#mining = miner(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)  
#objectList.append(mining)

'''
station = friendly(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
objectList.append(station)

shieldUp1 = friendlyS(1,station.x,station.y-24,0,1,1,1,1,1,1,station)
objectList.append(shieldUp1)

shieldRight1 = friendlyS(1,station.x+station.width+4,station.y,1,1,1,1,1,1,1,station)
objectList.append(shieldRight1)

shieldDown1 = friendlyS(1,station.x,station.y+station.height,2,1,1,1,1,1,1,station)
objectList.append(shieldDown1)

shieldLeft1 = friendlyS(1,station.x-20,station.y,3,1,1,1,1,1,1,station)
objectList.append(shieldLeft1)
'''



'''
powerUpList.append(healthPowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...
powerUpList.append(invisPowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...
powerUpList.append(firePowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...
'''

#powerUpList.append(amplifyPowerUp("amplify",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...

#buffList.append(reinforcements(1,1,1))

#enemia = enemy(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)  
#objectList.append(enemia)




evilStation = malevolent(1,1,1,1,1,1,1,1,1,1,1)


print("Your object list contains" , objectList)


# MAINLOOP

pygame.mixer.music.load(mainMusic)
#pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


station = 693


running = True
while running:
    clock.tick(30)
    #pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If the quit button is pressed
            running = False
            

    noDuplicates = 0 #Damages may be printed twice, this variable prevents this from occurring

    if random.randint(1,500) == 69 and len(powerUpList) < 10:
        decision = random.randint(1,4)
        if decision == 1 and upgrades[2] == 1:
            powerUpList.append(healthPowerUp("health",random.randint(50,winWidth-50),random.randint(50,winHeight-50),1)) #16x16 dimensions
        elif decision == 2 and upgrades[3] == 1:
            powerUpList.append(invisPowerUp("invis",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #16x16 dimensions
        elif decision == 3 and upgrades[4] == 1:
            powerUpList.append(firePowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...
        elif decision == 4 and upgrades[5] == 1:
            powerUpList.append(amplifyPowerUp("amplify",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) # ...



    if upgrades[1] == 1 and random.randint(1,1750) == 69 and len(buffList) < 10:
        decision = random.randint(1,3)
        if decision == 1:
            buffList.append(reinforcements(1,1,1))
        elif decision == 2:
            buffList.append(extraLife(1,1,1))
        else:
            buffList.append(extraScore(1,1,1))


    if random.randint(1,15721) == -4 and evilStation not in objectList:
        evilStation = malevolent(1,1,1,1,1,1,1,1,1,1,1)
        someShield = enemyS(1,evilStation.x-6,evilStation.y-6,1,1,1,1,1,1,1,evilStation)
        objectList.append(evilStation)
        objectList.append(someShield)



    firstCheck = 0

    #COUNT VARIABLES to determine players vs enemies
    count = 1
    count2 = 0



    for o in objectList:
        if isinstance(o,enemy) or isinstance(o,miner) or isinstance(o,frigate) or isinstance(o, fighter) or isinstance(o, carrier) or isinstance(o, malevolent):
            count += 1
        if isinstance(o, annoraxN) or isinstance(o, playerN):
            count2 += 1


    #SHIPSELECTION

    #If no more enemy players are present

    if count == 1:
        for x in range(random.randint(0,enemyChoice)):
            objectList.append(miner(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
        for x in range(random.randint(0,enemyChoice)):
            objectList.append(enemy(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
        for x in range(random.randint(0,enemyChoice+1)):
            objectList.append(frigate(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
        for x in range(random.randint(0,enemyChoice//7)):
            aBigCarrier = carrier(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
            objectList.append(aBigCarrier)
        if random.randint(-6,1) > 0:
            evilStation = malevolent(1,1,1,1,1,1,1,1,1,1,1)
            someShield = enemyS(1,evilStation.x-6,evilStation.y-6,1,1,1,1,1,1,1,evilStation)
            objectList.append(evilStation)
            objectList.append(someShield)
             


        


    if play not in objectList and currentLives > 0:
        if upgrades[0] == 1:
            play = annoraxPlayable(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
            objectList.append(play)
        else:
            play = player(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
            #play.invisible = 4003404334
            objectList.append(play)




    if count2 == 0: #If player is destroyed, respawns them
        for x in range(random.randint(0,alliedChoice)):
            objectList.append(playerN(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
        for x in range(random.randint(0,alliedChoice )):
            objectList.append(annoraxN(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))

        #station = friendly(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
        '''
        objectList.append(station)

        shieldUp1 = friendlyS(1,station.x,station.y-24,0,1,1,1,1,1,1,station)
        objectList.append(shieldUp1)

        shieldRight1 = friendlyS(1,station.x+station.width+4,station.y,1,1,1,1,1,1,1,station)
        objectList.append(shieldRight1)

        shieldDown1 = friendlyS(1,station.x,station.y+station.height,2,1,1,1,1,1,1,station)
        objectList.append(shieldDown1)

        shieldLeft1 = friendlyS(1,station.x-20,station.y,3,1,1,1,1,1,1,station)
        objectList.append(shieldLeft1)
        '''




    #If ships are at or below 0 hp, displays the explosion and removes them from the ObjectList
    for o in [badger for badger in objectList if not isinstance(badger,shield)]:
        if o.invisible >= 1:
            o.invisible -= 1
        if o.amplified > 1:
            o.amplified -= 1
        if o.amplified == 1:
            o.mitigation /= 1.75
            o.speed /= 1.75
            o.orgSpeed = o.speed
            o.orgHealth /= 1.75
            o.health /= 1.75
            o.orgHealthRecovery *= 2.5
            o.amplified = 0
        if o.health <= 0:
            BOOM.append(shipExploding(o.x,o.y))
            if isinstance(o, enemy):
                score += 1500
                enemyKills += 1
            elif isinstance(o, frigate):
                score+= 500
                frigateKills += 1
            elif isinstance(o, miner):
                score += 500
                minerKills += 1
            elif isinstance(o, carrier):
                score += 7500
            elif isinstance(o, fighter):
                score += 250
            elif isinstance(o,malevolent):
                score += 30000
            elif (isinstance(o, player) or isinstance(o, annoraxPlayable)) and currentLives > 0:
                currentLives -= 1
            objectList.remove(o)  



    #OBJECT-PROJECTILE COLLISION CHECKING CODE
    for p in projectileList:
        p.aliveTimer -= 1
        if isinstance(p, powerfulProjectile) and p.ownerID.health <= 0:
            projectileList.remove(p)

        for o in objectList: #n^2 complexity, but irrelevant when accounting for the small number of ships present-
            if not (o == evilStation and someShield.health > 0 ) and (p.owner in alliedTeam and o.name in enemyTeam or p.owner in enemyTeam and o.name in alliedTeam):

                if p.aliveTimer <= 0 and p in projectileList and not isinstance(o,spaceStation) and not isinstance(o, shield):
                    if p in o.fireProjectiles:
                        o.fireProjectiles.remove(p)
                    projectileList.remove(p)
                if o.invisible <= 0:
                    if p.x > o.hitbox[0] and p.x < o.hitbox[2] + o.x + o.leeway and p in projectileList: 
                        #If co-ordinates are the same
                        if p.y > o.hitbox[1] and p.y < o.y + o.hitbox[3] + o.leeway:
                            #If hitboxes intersect
                            #Removes the projectile and causes damage
                            if not isinstance(o,spaceStation) and not isinstance(o,shield) and o.target != 0 and math.hypot(o.target.x - p.ownerID.x, o.target.y - p.ownerID.y) < 560:
                                o.target = p.ownerID
                            if not isinstance(p, powerfulProjectile) and o.health > 0:
                                projectileList.remove(p)
                            if p.damage > 0 and o.health > 0:


                                #Checks the crit chance against a random number
                                if p.critChance >= random.randint(1,100):
                                    criticalStrike = 1
                                else:
                                    criticalStrike = 0
                                #Determines if a critical hit has occurred
                            
                                mitigation = 1 - o.mitigation 
                                #Checks the mitigation level of the hit object

                                if o.health > p.damage and criticalStrike == 0:
                                    #If the object has more hp than the projectile has damage
                                
                                    overallDamage = p.damage + random.randint(-1,1)
                                    overallDamage = int(overallDamage * mitigation) #Has to account for mitigation
                                    currentHealth = o.health
                                    o.health -= overallDamage   #Damages the object
                                    if o.name in enemyTeam:
                                        score += int(abs(currentHealth - o.health) ** 2)
                                    o.damagedCount = 100 #Displays the healthbar for 100 ticks 
                                elif o.health > p.damage * 1.5 and criticalStrike == 1: #ON CASE OF CRITICAL STRIKE - All critical hits deal 50% more damage
                                    overallDamage = int(p.damage * 1.5 + random.randint(-1,1))
                                    overallDamage = int(overallDamage * mitigation) #Same as above
                                    currentHealth = o.health
                                    o.health -= overallDamage #Same as above
                                    if o.name in enemyTeam:
                                        score += int( (currentHealth - o.health) ** 2)

                                    o.damagedCount = 100 #...
                                else:
                                    o.health = 0
                                    #If projectile deals more damage than object has hp remaining, it is destroyed
                            
                                #DISPLAYS DAMAGE
                                for c in str(overallDamage): 
                                    # This is NOT n^3 complexity
                                    # damage numbers are just an extension of the projectiles colliding with objects
                                    # which are already accounted for

                                    #FOR DOUBLE-DIGIT DAMAGES
                                    if len(str(overallDamage)) == 2 and noDuplicates == 0 and overallDamage > 0:
                                        damageNumber = [damage(int(str(overallDamage)[0]),p.owner,o,0,criticalStrike),damage(int(str(overallDamage)[1]),p.owner,o,1,criticalStrike)]
                                        o.damages.append(damageNumber)
                                        noDuplicates = 1
                                        #Sets the noDuplicates variable to 1 to avoid any duplicate entries occurrirng

                                    #FOR SINGLE-DIGIT DAMAGES
                                    elif len(str(overallDamage)) == 1 and noDuplicates == 0: 
                                        damageNumber = damage(int(c),p.owner,o,0,criticalStrike)
                                        o.damages.append([damageNumber])
                                        noDuplicates = 1
                                        #Same as above
                            pygame.mixer.Channel(random.randint(1,2)).play(explosionSoundFX2, maxtime=600)
                            if not isinstance(o, shield):            
                                if isinstance(p,powerfulProjectile):
                                    o.hits.append(explosionEffect(p.x,p.y,1))
                                    o.hits.append(explosionEffect(p.x,p.y,2))
                                    o.hits.append(explosionEffect(p.x,p.y,1))
                                if not isinstance(p, torpedo) and not isinstance(p, rocket):
                                    o.hits.append(explosionEffect(p.x,p.y,1))
                                else:
                                    o.hits.append(explosionEffect(p.x,p.y,2))
                            else:
                                o.underAttackTime = 5

    #OBJECT-OBJECT COLLISION CHECKING CODE
    for ob in [a for a in objectList if a.name in alliedTeam]:
        for otherOb in [a for a in objectList if a.name in enemyTeam]: #n^2 complexity yet again, but again small number of ships overrides this
            if not isinstance(ob, shield) and not isinstance(otherOb,shield) and ob.x + ob.width / 2 > otherOb.hitbox[0] and ob.x < otherOb.hitbox[2] + otherOb.x and ob.invisible <= 0 and otherOb.invisible <= 0: 
                if ob.y  + ob.height / 2 > otherOb.hitbox[1] and ob.y < otherOb.y + otherOb.hitbox[3]:
                    #Checks to see if the ships colliding are not the same ship, co-ordinates match + hitboxes intersect

                    #Applies for suicide attacks

                    #Same as before, but already collided
                    if otherOb.suicideAttack == 1 and otherOb.alreadyCollided <= 0:
                        ob.health -= otherOb.orgHealth 
                        ob.health -= 35
                        otherOb.health = 0
                        ob.damagedCount = 130

                    #NOT a suicide-based collision 
                    else:
                        otherOb.alreadyCollided = 45 #Prevents suicide attack damage from occurring for 45 frames after end of collision
                        totalHp = ob.orgHealth + otherOb.orgHealth
                        ob.health -= totalHp // 54
                        ob.damagedCount = 130
                        otherOb.damagedCount = 130
                        otherOb.health -= totalHp // 54
                        if ob.health <= 0 and isinstance(o, player):
                            currentLives -= 1
                    
                    #Displays explosions on both ships - 2 per frame that they are in collision with each other
                    for x in range(5):
                        ob.hits.append(explosionEffect(ob.x,ob.y,1))
                        otherOb.hits.append(explosionEffect(otherOb.x,otherOb.y,1))
                


    noDuplicates = 0


        


    

    drawWindow()

    pygame.display.flip()



if score > highScore:
    f = open("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/gamesave.txt","w").close()
    f = open("C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/gamesave.txt","r+")
    f.write(str(score))
    f.close()






pygame.quit() #This is the end
