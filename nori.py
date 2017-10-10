# -*- coding: utf-8 -*-

import curses
from russian import to_russian, to_latin

text = ':'
to_add = '*'
alist = []

while to_add != '':
    screen = curses.initscr()
    # curses.noecho(); curses.cbreak()
    
    screen.clear()
    screen.border(0)
    # screen.addstr(4, 2, text)
    i = 0
    while i < 10 and i < len(alist):
        latin = to_latin(alist[-(i+1)])
        screen.addstr(3+i, 2, latin)
        i = i + 1
    hits_message = 'No hits.'
    screen.addstr(2, 2, hits_message)
    screen.refresh()
    
    # x = screen.getch()
    to_add = screen.getstr(1, 2, 76)
    to_add = to_russian(to_add)
    alist.append(to_add)
    text = text + ', ' + to_add
    
curses.endwin()
