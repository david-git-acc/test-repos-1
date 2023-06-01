import random
import math
import pygame  #Importing necessary modules
pygame.init()

count = 1 #This variable makes sure that all ship explosions have the same animation duration, as well as tracking the number of enemies
minerCount = 0 #Keeps track of the number of miners, so that the number of mines doesn't go over 4 times the overall number of miners
criticalStrike = 0 #Checks whether a given strike is a critical hit or not
winWidth = 1920 #Screen sizes
winHeight = 1080
window = pygame.display.set_mode((winWidth,winHeight))
projectileList = [] #Tracks all projectiles
objectList = [] #Tracks all objects
powerUpList = [] #Tracks all powerups
BOOM = [] #Tracks all explosions
mineList = [] #...
healthCall = 0 #tracks which ship will go for health boost
score = 0
enemyKills = 0
minerKills = 0
frigateKills = 0
spacing = 30
currentLives = 3
lifeSpacing = 58

alliedTeam = ["Player ship" , "Friendly station","friendlyShield", "Player annorax", "Annorax"]
enemyTeam = ["Enemy ship","Miner","Frigate"]

pygame.display.set_caption("Secondary test")

#These are the sprite images loaded from the Computer
shipping = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/U10.png"),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/D10.png"),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/L10.png"),], [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/R10.png"),]]
shippingInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Uinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Dinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Linvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/engines/invis/Rinvis.png"),]
background = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/background.jpg")
scoreground = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/originalScoreTest2.png")
bullet = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile.png")
bullet2 = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile2.png")
bullet3 = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile3.png")
bullet4 = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/projectile4.png")
enemyShip = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/U17.png")],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/S17.png")],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/L17.png")],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/R17.png")]]
enemyShipInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Uinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Sinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Linvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/animations/invisible/Rinvis.png"),]
explosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/E9.png")]
shipExplosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/shipExplosion/REAL/TS11.png")]
largerExplosion = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/explosion/TBE9.png"),]
enemyProjectiles = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/verEnemyProjectile.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemy/horEnemyProjectile.png")]
damageCounterAllied = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/0.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/10.png")]
minerBlit = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/L15.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/R15.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/U15.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/S15.png"),]]
minerBlitInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Sinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Uinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Linvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/shipEngines/invis/Rinvis.png"),]
mineBlitStill = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb.png")
mineBlitAnim = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bomb13.png"),]
mineBlitBlink = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/miner/bomb/bombBlink.png")
health = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h25.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h26.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h27.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h28.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h29.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h30.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h31.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h32.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h33.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h34.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h35.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h36.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h37.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h38.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h39.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h40.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h41.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h42.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h43.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h44.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h45.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h46.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h47.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h48.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h49.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h50.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h51.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/health/h52.png"),]
invis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i25.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i26.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i27.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i28.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i29.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i30.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i31.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i32.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i33.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i34.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i35.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i36.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i37.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i38.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i39.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i40.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i41.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i42.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i43.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i44.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i45.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i46.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i47.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i48.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i49.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i50.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i51.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invis/i52.png"),]
firePower = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f25.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f26.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f27.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f28.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f29.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f30.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f31.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f32.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f33.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f34.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f35.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f36.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f37.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f38.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f39.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f40.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f41.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f42.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f43.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f44.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f45.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f46.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f47.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f48.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f49.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f50.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f51.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fire/f52.png"),]
fireProjectile = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPU.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPS.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPL.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/PPR.png")]
friendlyStation = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/stationAnim/FS17.png"),]
shields = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SU25.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SR25.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SD25.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldAnim/SL25.png"),],]
shieldsUA = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldUpUA.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldRightUA.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldDownUA.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/stations/shieldLeftUA.png"),]
torpedoAnimation = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/torpedo/ST19.png"),]
enemyTorpAnimation = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/enemyTorpedo/ET19.png"),]
rocketAnimation = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROU23.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROR23.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROS23.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/rocket/ROL23.png"),]]
scoreCounter = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b0.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/damageCounters/alliedDamage/b9.png"),]
lifePic = pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/lives.png")
healthyActivated = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h25.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h26.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h27.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h28.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h29.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h30.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h31.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h32.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h33.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h34.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h35.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h36.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h37.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h38.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h39.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h40.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h41.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h42.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h43.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h44.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h45.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h46.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h47.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h48.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h49.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h50.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h51.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/healthActivated/h52.png"),]
invisActivated = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i25.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i26.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i27.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i28.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i29.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i30.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i31.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i32.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i33.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i34.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i35.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i36.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i37.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i38.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i39.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i40.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i41.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i42.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i43.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i44.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i45.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i46.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i47.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i48.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i49.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i50.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i51.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/invisActivated/i52.png"),]
fireActivated = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f17.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f18.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f19.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f20.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f21.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f22.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f23.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f24.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f25.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f26.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f27.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f28.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f29.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f30.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f31.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f32.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f33.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f34.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f35.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f36.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f37.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f38.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f39.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f40.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f41.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f42.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f43.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f44.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f45.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f46.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f47.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f48.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f49.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f50.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f51.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/powerups/fireActivated/f52.png"),]
annorax = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AU17.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AR17.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AS17.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/AL17.png"),]]
annoraxInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/up.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/right.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/down.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/annorax/annoraxInvis/left.png"),]
frigateAnim = [[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRU17.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRR17.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRD17.png"),],[pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL1.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL2.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL3.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL4.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL5.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL6.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL7.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL8.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL9.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL10.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL11.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL12.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL13.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL14.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL15.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL16.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/FRL17.png"),]]
frigateInvis = [pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRUinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRRinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRDinvis.png"),pygame.image.load(r"C:/Users/david/Desktop/Schoolwork/Y12 Web Tech/My own work/python oop pygame/test2/art/frigate/frigateInvis/FRLinvis.png"),]
healthAnimCounter = 0
invisAnimCounter = 0
fireAnimCounter = 0



clock = pygame.time.Clock()


def drawWindow():
    #Draws the window each frame
    global healthAnimCounter
    global invisAnimCounter
    global fireAnimCounter
    global count
    global minerCount
    global healthCall
    window.blit(background,(0,0))
    window.blit(scoreground,(winWidth-400,winHeight-253))

    for x in range(len(str(score))):
        window.blit(scoreCounter[int(str(score)[x])],(winWidth - 406 + x * spacing, winHeight - 200))

    for x in range(len(str(enemyKills))):
        window.blit(scoreCounter[int(str(enemyKills)[x])],(winWidth - 108 + x * spacing, winHeight - 192))

    for x in range(len(str(minerKills))):
        window.blit(scoreCounter[int(str(minerKills)[x])],(winWidth - 108 + x * spacing, winHeight - 128))

    for x in range(len(str(frigateKills))):
        window.blit(scoreCounter[int(str(frigateKills)[x])],(winWidth - 108 + x * spacing, winHeight - 69))

    if currentLives > 0:
        for x in range(currentLives):
            window.blit(lifePic,(winWidth - 396 + x * lifeSpacing,winHeight-71))


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
            d.draw(window) if not isinstance(d,list) else [a.draw(window) for a in d]
            #If only a single digit worth of damage, draws window normally
            #Else, it draws every item in the list (there are multiple digit damages, eg 11 or 5!)
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
            try:
                #Red element for the (255,255,255) structure
                redElement = int(2.55 / trueHealthPercentage ** 8)
            except:
                #If above code fails, set the red to 255
                redElement = 255
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

        #Draws all explosions and projectiles per frame



    count = 1
    minerCount = 0

    pygame.display.update()

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
        self.invisible = 0
        self.fireBoost = 0
        self.fireProjectiles = []
        self.leeway = 0
        self.fleeTimer = 0
        self.currentFleeDirection = 0
        self.notGoingAnywhere = 0
        self.trigger = 0
        #Any unexplained attributes will be done so where they are used

    #All basic functions
    def basicFunctions(self,window):
        tupleEvasion = self.healthbar[2] - 2 #Unless I write this as a separate variable, BODMAS will not be performed correctly
        trueHealthPercentage = self.health / self.orgHealth 

        #Calculates the DIMENSIONS of the healthbar - smaller ships will have smaller healthbars and vice versa
        if isinstance(self, annoraxPlayable) or isinstance(self, annoraxN):
            self.healthbar = (self.x + 60 / 4,self.y-0.2*60,60 / 2,60 / 8)
        else:
            self.healthbar = (self.x + self.width / 4,self.y-0.2*self.height,self.width / 2,self.height / 8)
        self.innerBar = (self.healthbar[0] + 1, self.healthbar[1] + 1, tupleEvasion * trueHealthPercentage, self.healthbar[3] - 2)
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
            if self.health + 0.3125 <= self.orgHealth and self.health != 0:
                self.health += 0.3125

        if self.fireBoost > 0:
            self.fireBoost -= 1



        if isinstance(self,annoraxN) or isinstance(self,frigate):
            if self.target == 0:
                if isinstance(self,annoraxN):
                    poTargets = [a for a in objectList if a.name in enemyTeam]
                else:
                    poTargets = [a for a in objectList if a.name in alliedTeam]
                if len(poTargets) > 0:
                    self.target = poTargets[random.randint(0,len(poTargets)-1)]

            if self.target not in objectList:
                self.target = 0
            elif self.healthTarget == 0 and self.runTimer <= 0:
                if abs(self.target.x + self.target.width / 2 - self.x - self.width / 2) <= 35:
                    if self.target.y < self.y:
                        self.down = False
                        self.up = True
                        self.left = False
                        self.right = False
                        if isinstance(self, frigate):
                            frigate.fireGuns(self)
                        else:
                            annoraxN.fireGuns(self)
                        if self.y - self.target.y > 150:
                            self.y -= self.speed
                    else:
                        self.up = False
                        self.down = True
                        self.left = False
                        self.right = False
                        if isinstance(self, frigate):
                            frigate.fireGuns(self)
                        else:
                            annoraxN.fireGuns(self)
                        if self.target.y - self.y > 150:
                            self.y += self.speed
                elif abs(self.target.y + self.target.height / 2 - self.y - self.height / 2)<= 35:
                    if self.target.x > self.x:
                        self.right = True
                        self.down = False
                        self.left = False
                        self.up = False
                        if isinstance(self, frigate):
                            frigate.fireGuns(self)
                        else:
                            annoraxN.fireGuns(self)
                        if self.target.x - self.x > 150:
                            self.x += self.speed
                    else:
                        self.right = False
                        self.left = True
                        self.up = False
                        self.down = False
                        if isinstance(self, frigate):
                            frigate.fireGuns(self)
                        else:
                            annoraxN.fireGuns(self)
                        if self.x - self.target.x > 150:
                            self.x -= self.speed
                else:
                    if abs(self.target.x - self.x) >= abs(self.target.y-self.y):
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
                self.fireCall = 0

            if self.health <= 0.52 * self.orgHealth and self.healthTarget != 0 and self.suicideAttack != 1 and self.runTimer <= 0 and len(powerUpList) != 0 or self.healthTarget != 0 and self.suicideAttack != 1 and self.runTimer <= 0 and len(powerUpList) != 0 and self.invisCall == 1 or self.healthTarget != 0 and self.suicideAttack != 1 and self.runTimer <= 0 and len(powerUpList) != 0 and self.fireCall == 1:
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
                elif self.healthTarget.y < self.y - 25:
                    self.y -= self.speed
                    self.up = True
                    self.right = False
                    self.down = False
                    self.left = False
            if self.suicideAttack == 1:
                self.healthTarget = 0
                self.invisCall = 0
                self.fireCall = 0

            

            for o in [a for a in objectList if not isinstance(a, spaceStation) and not isinstance(a, shield)]:  



                if o != self and self.suicideAttack != 1: #Suicide charging enemies will ignore this code for obvious reasons
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

                            elif self.randomNum == 1 and not self.notDown and directions[2] == 1:
                                self.left = False
                                self.down = True
                                self.up = False
                                self.right = False
                                if self.y + self.speed + self.height <= winHeight:
                                    self.y += self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees down
                            elif self.randomNum == 3 and not self.notRight and directions[1] == 1:
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

                            elif self.randomNum == 1 and not self.notUp and directions[0] == 1:
                                self.left = False
                                self.down = False
                                self.up = True
                                self.right = False
                                if self.y - self.speed - self.height >= 0:
                                    self.y -= self.speed
                                else:
                                    self.randomNum = 0
                                #Object flees up
                            elif self.randomNum == 3 and not self.notRight and directions[1] == 1:
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

class annoraxN(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Annorax",60,60,random.randint(50,winWidth),random.randint(50,winHeight),100,100,0.25,6,[],[],False,False,True,False,0,12)

        self.target = 0
        self.rememberCoordinates = 0
        self.rememberTimer = 0

    def draw(self,window):

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
        


    def fireGuns(self):
        if len(self.projectiles) + len(self.horProjectiles) <= 6:
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
        super().__init__("Player annorax",60,60,500,500,100,100,0.25,12,[],[],False,False,True,False,0,12)
        #Initialises this player's stats


    def draw(self,window):

        self.counter += 1

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
            conditions = [self.up,self.right,self.down,self.left]
            if self.invisible > 0:
                window.blit(annoraxInvis[[conditions.index(c) for c in conditions if c][0]], (self.x,self.y))
            else:
                window.blit(annorax[[conditions.index(c) for c in conditions if c][0]][self.counter//2], (self.x,self.y))
            #This line of code displays the correct sprite type and the correct animation, for each state (up, down, left, right) at every frame


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






class player(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Player ship",64,64,50,50,120,120,0.35,10,[],[],False,False,True,False,0,16)
        #Initialises the player stats


    def draw(self,window):


        self.counter += 1
        #This variable is the animation counter for the player ship so that the engines can be animated - cycles through each frame

        self.projectileFrequency += 1
        #This variable limits how often the player can fire their guns, to prevent them from firing infinitely quickly

        if self.projectileFrequency == 5:
            self.projectileFrequency = 0
            #Limits the frequency of firing

        

    


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
                proj = projectile(play.x + value-3 ,play.y + value, -1,self.name,self)
                proj2 = projectile(play.x + self.width - 1 -3  - value, play.y + value, -1,self.name,self)
                #Fires from the correct position on the ship, using the value variables defined above
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                #Adds to the projectile list so they can be tracked
            elif self.down:
                proj = projectile(play.x + value-3, play.y + self.height - 2.5 * value, 1,self.name,self)
                proj2 = projectile(play.x + self.width - value - 1-3, play.y + self.height - 2.5 * value, 1,self.name,self)
                self.projectiles.append(proj)
                self.projectiles.append(proj2)
                #Same as above - the 2.5x modifier is because you are now firing from the opposite direction
            elif self.left:
                proj = projectile(play.x + value, play.y + value-3, -1,self.name,self)
                proj2 = projectile(play.x + value, play.y + self.height - value - 4, -1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                #Same as above, minor modifications made to guarantee that the projectiles fire from the nacelles 
            else:
                proj = projectile(play.x + self.width - value2 - 1, play.y + value-3, 1,self.name,self)
                proj2 = projectile(play.x + self.width - value2 - 1, play.y + self.height - value-3 - 1, 1,self.name,self )
                self.horProjectiles.append(proj)
                self.horProjectiles.append(proj2)
                #Same as above

            projectileList.append(proj)
            projectileList.append(proj2)
            #SEPARATE FIRE PROJECTILES TAB
        if self.fireBoost > 0:
            if len(self.fireProjectiles) <= 0:
                if self.up:
                    fireProj = powerfulProjectile(play.x + play.width // 2 - 6 , play.y-24,-1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.down:
                    fireProj = powerfulProjectile(play.x + play.width // 2 - 6, play.y + play.height,1 , self.name,self)
                    self.projectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                elif self.left:
                    fireProj = powerfulProjectile(play.x - 24, play.y + play.height // 2 -6 ,-1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)
                else:
                    fireProj = powerfulProjectile(play.x + play.width, play.y + play.height // 2 -6,1 , self.name,self)
                    self.horProjectiles.append(fireProj)
                    self.fireProjectiles.append(fireProj)

                projectileList.append(fireProj)

                    

        
            #Adds to the OVERALL projectile list so they can be tracked



class spaceStation():
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,projectiles,horProjectiles,healthRecovery,leftShieldHP,northShieldHP,rightShieldHP,southShieldHP,shieldDistance):
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
        self.leftShieldHP = leftShieldHP
        self.northShieldHP = northShieldHP
        self.rightShieldHP = rightShieldHP
        self.southShieldHP = southShieldHP
        self.shieldDistance = shieldDistance 
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

    def basicFunctions(self,window):
        tupleEvasion = self.healthbar[2] - 2 #Unless I write this as a separate variable, BODMAS will not be performed correctly
        trueHealthPercentage = self.health / self.orgHealth 

        #Calculates the DIMENSIONS of the healthbar - smaller ships will have smaller healthbars and vice versa
        self.healthbar = (self.x + self.width / 4,self.y-0.2*self.height,self.width / 2,self.height / 8)
        self.innerBar = (self.healthbar[0] + 1, self.healthbar[1] + 1, tupleEvasion * trueHealthPercentage, self.healthbar[3] - 2)
        self.hitbox = (self.x,self.y,self.width,self.height)

        self.healthRecovery -= 1 #depreciates hp recovery cooldown

        if self.healthRecovery <= 0:
            self.healthRecovery = self.orgHealthRecovery #hp recovery reaches 0, add health and reset cooldown
            if self.health + 1 <= self.orgHealth:
                self.health += 1

        if self.healthRegenTime >= 1:
            self.healthRegenTime -= 1
            if self.health + 0.3125 <= self.orgHealth and self.health != 0:
                self.health += 0.3125



class friendly(spaceStation):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,projectiles,horProjectiles,healthRecovery,leftShieldHP,northShieldHP,rightShieldHP,southShieldHP,shieldDistance):
        super().__init__("Friendly station",90,119,random.randint(150,winWidth - width),random.randint(150,winHeight - height - 150),1500,1500,0.65,[],[],12,500,500,500,500,15)

        self.attackTarget = 0
        self.animCounter = 0
        self.volleyTimer = 120
        self.rocketTimer = 30
        self.beamTimer = 30

    def draw(self,window):

        self.animCounter += 1
        self.volleyTimer -= 1
        self.rocketTimer -= 1
        self.beamTimer -= 1

        window.blit(friendlyStation[self.animCounter//3],(self.x,self.y))

        if self.animCounter >= 48:
            self.animCounter = 0

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
            projectileList.append(aPowerfulTorpedo)
            self.torpTimer = 90

        if self.suicideAttack == 1:
            self.healthTarget = 0
            self.invisCall = 0
            self.fireCall = 0
            self.suicideExplosionTimer -= 1

        if self.suicideExplosionTimer <= 0:
            self.health = 0

        for o in objectList:
            allegianceCheck = o.name in alliedTeam
            if allegianceCheck:
                pythagDistance = math.hypot(o.x - self.x, o.y - self.y)
            try:
                #Initially, only wanted to set hostile if within 1900metres, this code is irrelevant
                if allegianceCheck and pythagDistance < 1900 and self.enraged != 1:
                    self.target = objectList[objectList.index(o)]
                    self.enraged = 1
                    break
            except:
                pass

                

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
        if self.health / self.orgHealth <= 0.2 and self.suicideAttack == 0 and self.alreadyCollided == 0 and self.target.invisible <= 0:
            self.speed -= self.speed / 2.3
            #The acceleration will be extremely fast, so gives the player some advanced warning by lowering the speed temporarily
            self.healthTarget = 0
            self.invisCall = 0
            self.fireCall = 0
            self.suicideAttack = 1


   
        attackPatterns = [self.attackPatternLeft,self.attackPatternRight,self.attackPatternTop,self.attackPatternSouth]



        if self.invisCall == 0 and self.fireCall == 0 and self.healthTarget == 0 or self.invisCall == 0 and self.fireCall == 0 and self.health > self.orgHealth * 0.52: 
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
                if self.target not in objectList:
                    self.enraged = 0
                    self.suicideAttack = 0


                #If not suiciding and not running away from nearby ships, this is the main code function
                if self.runTimer <= 0 and self.suicideAttack != 1:
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

                    #In case of unexpected errors



   
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
                #Adds the projectile to the OVERALL projectile list
            except:
                pass
            #Accounts for any unexpected errors

class frigate(ship):
    def __init__(self,name,width,height,x,y,health,orgHealth,mitigation,speed,projectiles,left,right,up,down,healthRecovery):
        super().__init__("Frigate",48,48,random.randint(50,winWidth),random.randint(50,winHeight),48,48,0.25,5,[],[],False,False,True,False,0,28)

        self.target = 0


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
        super().__init__("Miner",48,48,random.randint(50,winWidth),random.randint(50,winHeight),40,40,0.2,6,[],[],False,False,True,False,0,36) 
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

        if self.healthTarget != 0 and self.health < self.orgHealth * 0.52 or self.healthTarget != 0 and self.invisCall == 1 or self.healthTarget != 0 and self.fireCall == 1:
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
                elif self.direction != 0 and self.runTimer == 0:
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

                if self.target not in objectList:
                    self.target = 0
                #Sets target as neutral if previous target has been destroyed, so it does not chase ghosts

                if random.randint(1,125) == 69 and self.mineTimeout == 0 and len(mineList) < 4 * minerCount:
                        self.mineTimer = 120
                        self.mineStatus = 1
                        return
                    
                #Above code reused for this status, otherwise the miner would never deploy mines in attack mode


                #SELECTS A TARGET
                if self.target == 0:
                    for o in objectList:
                        if o.name in alliedTeam:
                            self.target = objectList[objectList.index(o)]

            
                #THE CODE BELOW IS IDENTICAL IN STRUCTURE TO THE CODE FOR THE ENEMY SHIP - Search "Enemy(Ship)" via CTRL + F
                if self.invisCall == 0 and self.target != 0 and self.healthTarget == 0 and self.fireCall == 0 or self.fireCall == 0 and self.health > self.orgHealth * 0.52 and self.target !=0 and self.invisCall == 0 : 
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

        if self.orientation in [1,3]:
            self.width = self.actualWidth
            self.height = self.actualHeight
        else:
            self.width = self.actualHeight
            self.height = self.actualWidth

        self.hitbox = (self.x,self.y,self.width,self.height)

    def basicFunctions(self,window):

        if self.underAttackTime > 0:
            self.underAttackTime -= 1

        self.healthRecovery -= 1

        if self.healthRecovery <= 0:
            self.healthRecovery = self.orgHealthRecovery #hp recovery reaches 0, add health and reset cooldown
            if self.health + 1 <= self.orgHealth:
                self.health = self.orgHealth

        if self.owner not in objectList:
            objectList.remove(self) 






class friendlyS(shield):
    def __init__(self, name , x , y , orientation, actualWidth,  actualHeight, health,orgHealth,healthRecovery,orgHealthRecovery,owner):
        super().__init__("friendlyShield",x,y,orientation,16,119,100,100,360,360,owner)

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
        
        if self.owner == "Miner" or self.owner == "Frigate":
            #I was too lazy to give the miner its own projectile, so I just nerfed its stats if the projectile comes from a miner
            self.speed = 20 * side
            self.damage = 2.5
            self.critChance = 5

    #Drawing the projectiles vertically
    def draw(self,window):
        window.blit(enemyProjectiles[0], (self.x,self.y))
        self.y += self.speed  #Moves the projectile by the speed value
        if self.y > winHeight or self.y < 0 or self.ownerID not in objectList:
            try:
                projectileList.remove(self)
                #Removes the projectile if it goes out of bounds to reduce any potential lag
            except:
                pass
            #Accounts for any unexpected errors
        if self not in projectileList:
            #if removed from the projectileList, must also be removed from the local lists
            try:
                for o in objectList: #Searches the objectList to find the owner so that the projectile can be removed
                    if self in o.projectiles:
                        o.projectiles.remove(self)
                        #Removes the projectiles from the owner's local projectile list
            except:
                pass
            #Same as above

    #Drawing the projectiles horizontally
    def draw2(self,window):
        #IDENTICAL STRUCTURE AS ABOVE, JUST HORIZONTAL
        window.blit(enemyProjectiles[1], (self.x,self.y))
        self.x += self.speed
        if self.x > winWidth or self.x < 0 or self.ownerID not in objectList:
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

        

    #Drawing the projectiles vertically
    def draw(self,window):
        if self.side == -1:
            window.blit(fireProjectile[0],(self.x,self.y))
        else:
            window.blit(fireProjectile[1],(self.x,self.y))   

        self.y += self.speed  #Moves the projectile by the speed value
        if self.y > winHeight or self.y < 0 or self.ownerID not in objectList:
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
        if self.x > winWidth or self.x < 0 or self.ownerID not in objectList and self in projectileList:
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

        if self.target != 0 and self.target not in objectList:
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

        if self.target != 0 and self.target not in objectList:
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
                o.healthRegenTime = 500
                o.damagedCount = 500
                o.health += 40 + 0.5 * o.orgHealth
                if o.name in alliedTeam:
                    score += 1500
                if o.health > o.orgHealth:
                    o.health = o.orgHealth
                o.damagedCount = 75
                try:
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
        self.ratioX = abs(self.target.x + self.target.width / 2- self.x) / ( abs(self.target.x + self.target.width / 2 - self.x) + abs(self.target.y + self.target.height / 2 - self.y))
        self.ratioY = abs(self.target.y + self.target.height / 2 - self.y) / (abs(self.target.y + self.target.height / 2 - self.y) + abs(self.target.x + self.target.width / 2 - self.x))
        self.horizontalSide = 0
        self.verticalSide = 0


        if self.target.x > self.x:
            self.horizontalSide = 1
        else:
            self.horizontalSide = -1
        
        if self.target.y > self.y:
            self.verticalSide = 1
        else:
            self.verticalSide = - 1

        if self.owner == "Enemy ship":
            self.damage = 12
            self.speed = 20
            self.critChance = 15

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

        if self.targetless == 0:
            
            if self.target not in objectList or self.target.invisible > 0:
                self.targetless = 1

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

    #VERTICAL PROJECTILES
    def draw(self,window):
        if self.side == 1:
            window.blit(bullet, (self.x,self.y)) #Displays the projectile
        else:
            window.blit(bullet4, (self.x,self.y)) #Displays the projectile

        self.y += self.speed #Moves the projectile 
        if self.y > winHeight or self.y < 0 or self.ownerID not in objectList: #If the projectiles exit the map
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
        if self.x > winWidth or self.x < 0 or self.ownerID not in objectList:
            self.ownerID.horProjectiles.remove(self)
            if self in projectileList:
                projectileList.remove(self)
        elif self not in projectileList:
            self.ownerID.horProjectiles.remove(self)



        
#Adds the player - stats set to 1 as they are already determined in the classes themselves
play = annoraxPlayable(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)  
#objectList.append(play) 



#mining = miner(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)  
#objectList.append(mining)

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





powerUpList.append(healthPowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...
powerUpList.append(invisPowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...
powerUpList.append(firePowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...

#enemia = enemy(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)  
#objectList.append(enemia)







print("Your object list contains" , objectList)


running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If the quit button is pressed
            running = False
    noDuplicates = 0 #Damages may be printed twice, this variable prevents this from occurring

    if random.randint(1,500) == 69 and len(powerUpList) < 10:
        decision = random.randint(1,3)
        if decision == 1:
            powerUpList.append(healthPowerUp("health",random.randint(50,winWidth-50),random.randint(50,winHeight-50),1)) #16x16 dimensions
        elif decision == 2:
            powerUpList.append(invisPowerUp("invis",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #16x16 dimensions
        elif decision == 3:
            powerUpList.append(firePowerUp("fire",random.randint(50,winWidth-50),random.randint(50,winHeight - 50),1)) #...



    #COUNT VARIABLES to determine players vs enemies
    count = 1
    count2 = 0
    for o in objectList:
        if isinstance(o,enemy) or isinstance(o,miner) or isinstance(o,frigate):
            count += 1
        if isinstance(o, player) or isinstance(o,annoraxPlayable) or isinstance(o, annoraxN):
            count2 += 1




    #If no more enemy players are present
    if count == 1:
        for x in range(random.randint(3,15)):
            objectList.append(miner(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
        for x in range(random.randint(3,15)):
            objectList.append(enemy(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
        for x in range(random.randint(3,15)):
            objectList.append(frigate(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))

    if count2 == 0: #If player destroys, respawns them
        play = annoraxPlayable(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
        #objectList.append(play)
        for x in range(3):
            objectList.append(annoraxN(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
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


        
    #If ships are at or below 0 hp, displays the explosion and removes them from the ObjectList
    for o in [badger for badger in objectList if not isinstance(badger,shield)]:
        if o.invisible >= 1:
            o.invisible -= 1
        if o.health <= 0:
            BOOM.append(shipExploding(o.x,o.y))
            if isinstance(o, enemy):
                score += 3000
                enemyKills += 1
            elif isinstance(o, frigate):
                score+= 1000
                frigateKills += 1
            elif isinstance(o, miner):
                score += 1000
                minerKills += 1
            elif isinstance(o, player) or isinstance(o, annoraxPlayable):
                currentLives -= 1
            objectList.remove(o)  

    #OBJECT-PROJECTILE COLLISION CHECKING CODE
    for p in projectileList:
        p.aliveTimer -= 1
        for o in objectList: #n^2 complexity, but irrelevant when accounting for the small number of ships present
            if p.owner in alliedTeam and o.name in enemyTeam or p.owner in enemyTeam and o.name in alliedTeam:

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
                                        score += int(0.43 * (currentHealth - o.health) ** 1.5)
                                    o.damagedCount = 100 #Displays the healthbar for 100 ticks 
                                elif o.health > p.damage * 1.5 and criticalStrike == 1: #ON CASE OF CRITICAL STRIKE - All critical hits deal 50% more damage
                                    overallDamage = int(p.damage * 1.5 + random.randint(-1,1))
                                    overallDamage = int(overallDamage * mitigation) #Same as above
                                    currentHealth = o.health
                                    o.health -= overallDamage #Same as above
                                    if o.name in enemyTeam:
                                        score += int(0.43 * (currentHealth - o.health) ** 1.5)

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
                                    if len(str(overallDamage)) == 2 and noDuplicates == 0:
                                        damageNumber = [damage(int(str(overallDamage)[0]),p.owner,o,0,criticalStrike),damage(int(str(overallDamage)[1]),p.owner,o,1,criticalStrike)]
                                        o.damages.append(damageNumber)
                                        noDuplicates = 1
                                        #Sets the noDuplicates variable to 1 to avoid any duplicate entries occurrirng

                                    #FOR SINGLE-DIGIT DAMAGES
                                    elif len(str(overallDamage)) == 1 and noDuplicates == 0: 
                                        damageNumber = damage(int(c),p.owner,o,0,criticalStrike)
                                        o.damages.append(damageNumber)
                                        noDuplicates = 1
                                        #Same as above
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
                    for x in range(2):
                        ob.hits.append(explosionEffect(ob.x,ob.y,1))
                        otherOb.hits.append(explosionEffect(otherOb.x,otherOb.y,1))
                


    noDuplicates = 0


        




    drawWindow()


pygame.quit() #This is the end
