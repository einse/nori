# -*- coding: utf-8 -*-

q2j = {'q': u'й', 'w': u'ц', 'e': u'у', 'r': u'к',
     't': u'е', 'y': u'н', 'u': u'г', 'i': u'ш',
     'o': u'щ', 'p': u'з', '{': u'х', '}': u'ъ',
     'a': u'ф', 's': u'ы', 'd': u'в', 'f': u'а',
     'g': u'п', 'h': u'р', 'j': u'о', 'k': u'л',
     'l': u'д', ';': u'ж', "'": u'э',
     'z': u'я', 'x': u'ч', 'c': u'с', 'v': u'м',
     'b': u'и', 'n': u'т', 'm': u'ь', ',': u'б',
     '.': u'ю', '`': u'ё'
}

def to_russian(string):
    string_in_russian = u''
    for latin in string:
        try:
            cyrillic = q2j[latin]
        except:
            cyrillic = u'' + latin
        string_in_russian = string_in_russian + cyrillic
    return string_in_russian

u2a = {u'й': 'j', u'ц': 'c', u'у': 'u', u'к': 'k',
     u'е': 'e', u'н': 'n', u'г': 'g', u'ш': 's',
     u'щ': 's', u'з': 'z', u'х': 'h', u'ъ': '`',
     u'ф': 'f', u'ы': 'y', u'в': 'v', u'а': 'a',
     u'п': 'p', u'р': 'r', u'о': 'o', u'л': 'l',
     u'д': 'd', u'ж': 'z', u'э': 'e',
     u'я': 'a', u'ч': 'c', u'с': 's', u'м': 'm',
     u'и': 'i', u'т': 't', u'ь': '`', u'б': 'b',
     u'ю': 'u', u'ё': 'o'
     }

def to_latin(string_in_russian):
    ascii_string = ''
    for cyrillic in string_in_russian:
        try:
            latin = u2a[cyrillic]
        except:
            latin = u'' + cyrillic
        ascii_string = ascii_string + latin
    return ascii_string
