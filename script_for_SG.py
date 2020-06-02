# -*- coding: utf-8 -*-
#version 2.1.0.010620
import pyscreenshot as ig
import pyautogui as pg
from time import sleep
import datetime
from os import sys

#MoveTo x1:1749; y1:935
#Color [255, 230, 130]
#testcolor [40, 44, 52]
#ColorFild x1:1551, y1:341; x2:1553, y2:343

#
programm_ranning = True
answer_color = [255, 230, 130]#Color of frame(when appear do_something())
version = '2.1.0.010620'
#

class AutoClicker():
    def __init__(self, answer_color, programm_ranning, version):
        self.answer = ''
        self.answer_color = answer_color
        self.programm_ranning = programm_ranning
        self.ver = version


    def move_click(self):
        if self.answer == 'Auto':
            pg.moveTo(1749, 935)
            pg.click(button='left')
        else:
            pg.click(button='left')
        print(datetime.datetime.now())


    def is_color(self):
        image = ig.grab(backend= 'mss', childprocess = False)
        color = list(image.getpixel((2399 + 1551, 407)))
        print(color)
        if color == answer_color:
            print(datetime.datetime.now())
            self.move_click()

            return False
        else:

            return True


    def is_start(self):
        check = True
        while check:
            check = self.is_color()


    def main(self):
        while self.programm_ranning:
            self.answer = pg.confirm(text='Знаешь или как?',
                                title='AutoClicker {}'.format(self.ver),
                                buttons=['OK', 'Cancel', 'Aoto'])
            
            if self.answer == 'OK' or self.answer == 'Auto':
                print('Signal1')
                self.is_start()
            else:
                sys.exit()

            sleep(1)


AutoClicker(answer_color, programm_ranning, version).main()



