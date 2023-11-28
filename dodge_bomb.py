import sys
import pygame as pg
import random
import math

WIDTH, HEIGHT = 1400,750


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    bg_img_2=pg.transform.flip(bg_img, True, False)
    ending = pg.image.load("ex02/fig/9.png")
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
              pg.transform.rotozoom(kk_img_flip, -40, 1.0),
              pg.transform.rotozoom(ending, 0, 2.0)]
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
    
    bi = 0

    vx = 5
    vy = 5
    dots = []
    count = 1000000

    accs = [a for a in range(1, 11)]
    for r in range(1, 11):
        dot = pg.Surface((20*r, 20*r))
        pg.draw.circle(dot, (255,0,0), (10*r, 10*r), 10*r)
        dots.append(dot)
    dot = dots[min(tmr//500, 9)]
    #dot.set_colorkey((0, 0, 0))
    dot_rct = dot.get_rect()
    dot_rct.center = random.uniform(0,1590),random.uniform(0,890)

    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        #new function
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])  # 練習４：背景画像の表示
        screen.blit(bg_img_2, [1600-x, 0])  # 練習６：動く背景画像
        screen.blit(bg_img_2, [3200-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        
        #screen.blit(bg_img, [0, 0])
        screen.blit(kk_img[bi], bird_rct)
        screen.blit(dot,dot_rct)
        
        
        
        db_vector = dot_rct[0]-bird_rct[0],dot_rct[1]-bird_rct[1]
        db_dis = round(math.sqrt(db_vector[0]**2 + db_vector[1]**2))
        if db_dis >= 500:
            norm_factor = math.sqrt(db_vector[0]**2 + db_vector[1]**2)
            vx = -db_vector[0] / norm_factor * 5 
            vy = -db_vector[1] / norm_factor * 5
        else:
            if dot_rct.left < 0:
                vx = +5
            if dot_rct.right > WIDTH:
                vx = -5
            if dot_rct.top < 0:
                vy = +5
            if dot_rct.bottom > HEIGHT:
                vy = -5
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        dot = dots[min(tmr//500, 9)]
        dot.set_colorkey((0, 0, 0))
        dot_rct.move_ip(avx,avy)
        
        #bird's moving
        key_total = [0,0]
        key_lst = pg.key.get_pressed()

        #new function_2
        if key_lst[pg.K_UP]: key_total[1] -= 5
        if key_lst[pg.K_DOWN]: key_total[1] += 5   
        if key_lst[pg.K_LEFT]: key_total[0] -= 5
        if key_lst[pg.K_RIGHT]: key_total[0] += 5

        if key_total==[0,-5]:
            bird_rct.move_ip(0,-5)
            bi = 2
        elif key_total==[0,+5]:
            bird_rct.move_ip(0,+5)
            bi = 3
        elif key_total==[-5,0]:
            bird_rct.move_ip(-5,0)
            bi = 0    
        elif key_total==[+5,0]:
            bird_rct.move_ip(+5,0)
            bi = 1

        elif key_total==[-5,-5]:
            bird_rct.move_ip(-5,-5)
            bi = 4
        elif key_total==[+5,-5]:
            bird_rct.move_ip(+5,-5)
            bi = 6
        elif key_total==[-5,+5]:
            bird_rct.move_ip(-5,+5)
            bi = 5
        elif key_total==[+5,+5]:
            bird_rct.move_ip(+5,+5)
            bi = 7

        
        
        if bird_rct.left < 0:
            bird_rct.left = 0
        if bird_rct.right > WIDTH:
            bird_rct.right = WIDTH
        if bird_rct.top < 0:
            bird_rct.top = 0
        if bird_rct.bottom > HEIGHT:
            bird_rct.bottom = HEIGHT


        if bird_rct.colliderect(dot_rct):
            bi = 8
            count = tmr
            
        """
        print("bird's move key:",key_total)
        
        print("speed:",avx,avy)
        
        print(tmr)
        
        print("dot:",dot_rct)
        print("bird:",bird_rct)
        #print("dot:",dot_rct[0],dot_rct[1])"""

        print(dots)
        print(dot)


        tmr += 1
        pg.display.update()
        clock.tick(50)
        if tmr == count + 2:
            return
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()