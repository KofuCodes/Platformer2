import math
import sys

from level import Level
from settings import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
sett = Settings()
screen = pygame.display.set_mode((sett.screen_width, sett.screen_height))
sett.screen = screen
clock = pygame.time.Clock()
current_level = sett.level_name
level = Level(levels[current_level], screen, sett)

in_game = False

dash_charge = pygame.Rect((20, sett.screen_height - 50), (200, 30))


def run_game():
    global current_level, level, in_game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        in_game = False

    screen.fill("black")
    if current_level != sett.level_name or sett.reload_level:
        sett.reload_level = False
        current_level = sett.level_name
        level = Level(levels[current_level], screen, sett)
    else:
        level.run()

        if sett.charge['dash'] < 120:
            sett.charge['dash'] += 2

        dash_charge.width = (sett.charge['dash'] / 120) * 200

        font = pygame.font.Font("./graphics/ui/ARCADEPI.TTF", 32)
        text = font.render("Score: {0}".format(sett.score), True, (255, 255, 255))

        textRect = text.get_rect()

        textRect.topleft = (20, 20)

        screen.blit(text, textRect)

        # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((17, sett.screen_height - 53), (206, 36)))
        # pygame.draw.rect(screen, (0, 80, 180), dash_charge)

        dash_bar = pygame.image.load("./graphics/ui/dash_bar/{0}.png".format(math.floor(sett.charge['dash'] / 30)))
        dash_bar = pygame.transform.scale_by(dash_bar, 4)
        screen.blit(dash_bar, (20, sett.screen_height - 80))


while True:
    if in_game:
        run_game()
    else:
        mouse = pygame.mouse.get_pos()
        height = screen.get_height()
        width = screen.get_width()
        color_light = (49, 43, 86)
        color_dark = (39, 33, 76)
        playfont = pygame.font.Font("./graphics/ui/ARCADEPI.TTF", 35)
        playtext = playfont.render('Play', True, (255, 255, 255))
        namefont = pygame.font.Font("./graphics/ui/ARCADEPI.TTF", 100)
        nametext = namefont.render("GAME NAME", True, (255, 255, 255))
        bg_0 = pygame.transform.scale_by(pygame.image.load("./graphics/background/0.png"), 4)
        bg_1 = pygame.transform.scale_by(pygame.image.load("./graphics/background/1.png"), 4)
        bg_2 = pygame.transform.scale_by(pygame.image.load("./graphics/background/2.png"), 4)
        bg_top = pygame.transform.scale_by(pygame.image.load("./graphics/background/top.png"), 4)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 75 <= mouse[0] <= width / 2 + 75 and height / 2 + 100 <= mouse[1] <= height / 2 + 150:
                    in_game = True

        screen.blit(bg_0, (0, height - 488))
        screen.blit(bg_1, (0, height - 488))
        screen.blit(bg_2, (0, height - 488))
        screen.blit(bg_top, (0, height - 720))

        if width / 2 - 75 <= mouse[0] <= width / 2 + 75 and height / 2 + 100 <= mouse[1] <= height / 2 + 150:
            pygame.draw.rect(screen, color_light, (width / 2 - 75, height / 2 + 100, 150, 50))
        else:
            pygame.draw.rect(screen, color_dark, (width / 2 - 75, height / 2 + 100, 150, 50))

        screen.blit(playtext, (width / 2 - 46, height / 2 + 107.5))
        screen.blit(nametext, (width / 2 - (nametext.get_size()[0] / 2), height / 2 - (nametext.get_size()[1] / 2)))

    pygame.display.update()
    clock.tick(60)
