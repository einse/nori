from bearlibterminal import terminal as t
from search import search
from load import load_files

term = ' '
list_of_terms = []
list_of_strings = load_files('./files')
list_of_results = []
list_of_counters_for_each_term = []
height_of_input_field = 1
height_of_status_bar = 1
height_of_header = height_of_input_field + height_of_status_bar
count_of_results = 0
count_of_rows = 25
count_of_terms_visible = 4
count_of_results_visible = count_of_rows - height_of_header - \
                           count_of_terms_visible
input_prompt = ''


message = 'Strings loaded: ' + str(len(list_of_strings))

t.open()
t.set('input.filter=[keyboard, close]')
while term != '':
    t.clear()
    i = 0
    while i < count_of_terms_visible and i < len(list_of_terms):
        t.printf(0, height_of_header+i, list_of_terms[-(i+1)])
        i = i + 1
    i = 0
    while i < count_of_results_visible and i < len(list_of_results):
        t.printf(0, height_of_header+count_of_terms_visible+i, \
                 list_of_results[i])
        i = i + 1
    t.printf(0, 1, message)
    t.refresh()
    
    len_, term = t.read_str(0, 0, input_prompt, 76)
    list_of_terms.append(term)
    
    if len(list_of_counters_for_each_term) > 0:
        list_of_strings = list_of_results
    list_of_results = search(term, list_of_strings)
    count_of_results = len(list_of_results)
    list_of_counters_for_each_term.append(count_of_results)
    
    message = 'Count: ' + str(count_of_results)
t.close()
