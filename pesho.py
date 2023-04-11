import pygame

#CONSTANTS
SIZE = [320 * 16 // 16, 180 * 16 // 16]
WINDOW_FLAGS = pygame.RESIZABLE | pygame.SCALED
MENU_BACKGROUND = pygame.image.load("Untitled.png")
MENU_BACKGROUND = pygame.transform.scale(MENU_BACKGROUND, SIZE)

#VARIABLES
run:bool = True
surface = pygame.display.set_mode(SIZE, vsync=True, flags=WINDOW_FLAGS)
is_fullscreen: bool = False

pygame.display.set_caption('Crpyt of Thieves')

class Menu:
	def __init__(self) -> None:
		pass
	
	def handle_event(self, event: pygame.event.Event):
		return self
	
	def update(self, delta_time: int) -> None:
		pass
	
	def draw(self) -> None:
		surface.blit(MENU_BACKGROUND, [0, 0], MENU_BACKGROUND.get_rect())

def toggle_fullscreen() -> None:
	global is_fullscreen
	is_fullscreen = not is_fullscreen
	pygame.display.set_mode(SIZE, vsync = True, flags = WINDOW_FLAGS | (pygame.FULLSCREEN * is_fullscreen))
        
screen = Menu()

while run:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                run = False
            case pygame.KEYDOWN if event.key == pygame.K_F11:
                toggle_fullscreen()
            case _:
                screen = screen.handle_event(event)
    screen.draw()
    pygame.display.flip()