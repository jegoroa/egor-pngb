from pygame import*
mixer.init()
mixer.music.load("muzika.mp3")
mixer.music.play()

WIDTH = 960  #ширина игрового окна
HEIGHT = 720 #высота игрового окна
win=display.set_mode((WIDTH, HEIGHT))

color = (124,234,78)
win.fill(color)

running = True
while running:
    for e in event.get():
        if e.type==QUIT:
            exit()
    display.update()


