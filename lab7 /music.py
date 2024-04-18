import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((735, 510))
done = False
songs = ['/Users/dilnazesenkyzy/Desktop/pp2/f.mp3', '/Users/dilnazesenkyzy/Desktop/pp2/lean.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
background_image = pygame.image.load("/Users/dilnazesenkyzy/Desktop/pp2/back.JPG")
background_rect = background_image.get_rect()

while not done:
    if i == 3:
        background_image = pygame.image.load('/Users/dilnazesenkyzy/Desktop/pp2/back.JPG')
        background_rect = background_image.get_rect()
        screen.blit(background_image, background_rect)
    else:
        background_image = pygame.image.load("/Users/dilnazesenkyzy/Desktop/pp2/back.JPG")
        background_rect = background_image.get_rect()
        screen.blit(background_image, background_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if a:
                    pygame.mixer.music.stop()
                    a = False
                else:
                    pygame.mixer.music.play()
                    a = True

    pygame.display.flip()
