import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_fl=pg.transform.flip(bg_img,True,False)
    kk=pg.image.load("ex01/fig/3.png")
    kk_fl=pg.transform.flip(kk,True,False)
    kk_rt=pg.transform.rotozoom(kk_fl,10,1.0)
    kk_rt_a=pg.transform.rotozoom(kk_fl,3,1.0)
    kk_rt_b=pg.transform.rotozoom(kk_fl,6,1.0)
    kk_lst=[kk_fl,kk_rt_a,kk_rt_b,kk_rt,kk_rt_b,kk_rt_a]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x=tmr%3200
        screen.blit(bg_img, [800-x, 0])
        screen.blit(bg_img_fl,[2400-x,0])
        screen.blit(bg_img_fl,[-800-x,0])
        screen.blit(kk_lst[tmr%4],[300,200])

        pg.display.update()
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()