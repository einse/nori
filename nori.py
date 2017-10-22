# -*- coding: utf-8 -*-

import curses
from russian import to_russian, to_latin

text = ':'
term = '*'
alist = []
results = []

while term != '':
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
    term = screen.getstr(1, 2, 76)
    term = to_russian(term)
    # data = load_files()
    # count_of_found = search(term, data)
    alist.append(term)
    # results.append(count_of_found)
    
curses.endwin()
