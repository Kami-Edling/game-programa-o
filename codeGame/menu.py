import pygame

# Certifique-se de que const.py está na mesma pasta que menu.py
from codeGame.const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE

pygame.init()

if pygame.get_init():
    print("Pygame initialization com success!")
else:
    print("Error ao initializer o Pygame.")

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu.png')
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def run(self):
        pygame.mixer_music.load('./assets/loading-main-menu-145077.mp3')
        pygame.mixer_music.play(-1)

        running = True  # Adicionado para controlar o loop
        while running:
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, text="Summer Beach", text_color=(255, 128, 0), text_center_pos=(self.window.get_width() / 2, 70))
            self.menu_text(50, text="Find Objects", text_color=(255, 128, 0), text_center_pos=(self.window.get_width() / 2, 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, text_center_pos=(self.window.get_width() / 2, 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Alterado para sair do loop
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, antialiasing=True):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, antialiasing, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


        

