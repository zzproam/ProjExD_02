import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1400,750


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_flip = pg.transform.flip(kk_img, True, False)
    kk_img = [kk_img,
              kk_img_flip,
              pg.transform.rotozoom(kk_img_flip, 100, 1.0),
              pg.transform.rotozoom(kk_img_flip, -100, 1.0),
              pg.transform.rotozoom(kk_img, -35, 1.0),
              pg.transform.rotozoom(kk_img, 35, 1.0),
              pg.transform.rotozoom(kk_img_flip, 40, 1.0),
              pg.transform.rotozoom(kk_img_flip, -40, 1.0)]
    clock = pg.time.Clock()
    

    #dot rect
    """dot = pg.Surface((20, 20))
    pg.draw.circle(dot, (255, 0, 0), (10, 10), 10)
    dot.set_colorkey((0, 0, 0))
    dot_rct = dot.get_rect()
    dot_rct.center = random.uniform(0,1590),random.uniform(0,890)"""

    #bird rect
    bird_rct = kk_img[0].get_rect()
    bird_rct.center = 900,400

    tmr = 0
    b = 0
    vx = +5
    vy = +5
    dots = []
    accs = [a for a in range(1, 11)]
    for r in range(1, 11):
        dot = pg.Surface((20*r, 20*r))
        pg.draw.circle(dot, (255, 0, 0), (10*r, 10*r), 10*r)
        dots.append(dot)
    dot = dots[min(tmr//500, 9)]
    #dot.set_colorkey((0, 0, 0))
    dot_rct = dot.get_rect()
    dot_rct.center = random.uniform(0,1590),random.uniform(0,890)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img[b], bird_rct)
        screen.blit(dot,dot_rct)
        
        

        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        dot = dots[min(tmr//500, 9)]
        dot.set_colorkey((0, 0, 0))
        dot_rct.move_ip(avx,avy)


        if dot_rct.left < 0:
            vx = +5
        if dot_rct.right > WIDTH:
            vx = -5
        if dot_rct.top < 0:
            vy = +5
        if dot_rct.bottom > HEIGHT:
            vy = -5
        
        #bird's moving
        key_total = [0,0]
        key_lst = pg.key.get_pressed()

        if key_lst[pg.K_UP]: key_total[1] -= 5
        if key_lst[pg.K_DOWN]: key_total[1] += 5   
        if key_lst[pg.K_LEFT]: key_total[0] -= 5
        if key_lst[pg.K_RIGHT]: key_total[0] += 5

        if key_total==[0,-5]:
            bird_rct.move_ip(0,-5)
            b = 2
        elif key_total==[0,+5]:
            bird_rct.move_ip(0,+5)
            b = 3
        elif key_total==[-5,0]:
            bird_rct.move_ip(-5,0)
            b = 0    
        elif key_total==[+5,0]:
            bird_rct.move_ip(+5,0)
            b = 1

        elif key_total==[-5,-5]:
            bird_rct.move_ip(-5,-5)
            b = 4
        elif key_total==[+5,-5]:
            bird_rct.move_ip(+5,-5)
            b = 6
        elif key_total==[-5,+5]:
            bird_rct.move_ip(-5,+5)
            b = 5
        elif key_total==[+5,+5]:
            bird_rct.move_ip(+5,+5)
            b = 7

        
        
        if bird_rct.left < 0:
            bird_rct.left = 0
        if bird_rct.right > WIDTH:
            bird_rct.right = WIDTH
        if bird_rct.top < 0:
            bird_rct.top = 0
        if bird_rct.bottom > HEIGHT:
            bird_rct.bottom = HEIGHT
        if bird_rct.colliderect(dot_rct):
            return
        """
        print("bird's move key:",key_total)
        print("bird:",bird_rct)
        print("dot:",dot_rct)"""
        print("speed:",avx,avy)
        print(dots)
        print(tmr)
        print(dot)

        tmr += 1
        pg.display.update()
        clock.tick(50)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()