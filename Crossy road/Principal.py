import sys, pygame, util
from pygame.locals import *
from Gallina import *
from Carro import *
from random import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Crossy road" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg');
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    gallina = Gallina()
    carro = [Carro((100,80),randint(1,10)),
             Carro((100,150),randint(1,10)),
             Carro((200,220),randint(1,10)),
             Carro((300,300),randint(1,10)),
             Carro((100,350),randint(1,10))]
    
    while True:
        fuente = pygame.font.Font(None,25)
        texto_puntos = fuente.render("Puntos: "+str(gallina.puntos),1,(0,0,0))
        
        gallina.update()
        for n in carro:
            n.update()
        
        for n in carro:
            if gallina.rect.colliderect(n.rect):
                gallina.image = gallina.imagenes[1]
                if gallina.vida > 0:
                    gallina.vida=gallina.vida-1
                n.velocidad=randint(1,10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(gallina.image, gallina.rect)
        screen.blit(texto_puntos,(100,450))
        for n in carro:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)

      
if __name__ == '__main__':
      game()
