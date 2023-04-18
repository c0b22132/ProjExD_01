import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("1kai/ex01/fig/pg_bg.jpg")
    kokaton=pg.image.load("1kai/ex01/fig/3.png")
    kk_fl=pg.transform.flip(kokaton,True,False)
    kk_rt=pg.transform.rotate(kk_fl,10)
    kk_rt_n=pg.transform.rotate(kk_fl,5)
    kk_lst=[kk_fl,kk_rt_n,kk_rt,kk_rt_n]

    tmr = 0
    bg_x=0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x=tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img,[1600-x,0])
        screen.blit(kk_lst[tmr%4],[300,200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()