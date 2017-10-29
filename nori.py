from bearlibterminal import terminal as t
from search import search
from load import load_files

term = ' '
list_of_terms = []
list_of_strings = load_files('./files')
results_strings = []
results_counters = []

message = 'Strings loaded: ' + str(len(list_of_strings))

t.open()
t.set('input.filter=[keyboard, close]')
while term != '':
    t.clear()
    i = 0
    while i < 10 and i < len(list_of_terms):
        t.printf(0, 2+i, list_of_terms[-(i+1)])
        i = i + 1
    t.printf(0, 1, message)
    t.refresh()
    
    len_, term = t.read_str(0, 0, '', 76)
    list_of_terms.append(term)
    
    if len(results_counters) > 0:
        list_of_strings = results_strings
    results_strings = search(term, list_of_strings)
    count_of_found = len(results_strings)
    results_counters.append(count_of_found)
    
    message = str(count_of_found)
t.close()
