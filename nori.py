import curses
from russian import to_russian, to_latin
from search import search
from load import load_files

term = ' '
list_of_terms = []
list_of_strings = load_files('./files')
results_strings = []
results_counters = []

message = 'Strings loaded: ' + str(len(list_of_strings))

screen = curses.initscr()
while term != '':
    # curses.noecho(); curses.cbreak()
    
    screen.clear()
    screen.border(0)
    # screen.addstr(4, 2, text)
    i = 0
    while i < 10 and i < len(list_of_terms):
        screen.addstr(3+i, 2, to_latin(list_of_terms[-(i+1)]))
        i = i + 1
    screen.addstr(2, 2, message)
    screen.refresh()
    
    # x = screen.getch()
    term = screen.getstr(1, 2, 76)
    term = to_russian(term)
    list_of_terms.append(term)
    
    if len(results_counters) > 0:
        list_of_strings = results_strings
    results_strings = search(term, list_of_strings)
    count_of_found = len(results_strings)
    results_counters.append(count_of_found)
    
    message = str(count_of_found)
    
curses.endwin()
