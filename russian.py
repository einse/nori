q2j = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к',
     't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш',
     'o': 'щ', 'p': 'з', '{': 'х', '}': 'ъ',
     'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а',
     'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л',
     'l': 'д', ';': 'ж', "'": 'э',
     'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м',
     'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б',
     '.': 'ю', '`': 'ё'
}

def to_russian(bytes_):
    string = bytes_.decode('utf-8')
    string_in_russian = ''
    for latin in string:
        try:
            cyrillic = q2j[latin]
        except:
            cyrillic = '' + latin
        string_in_russian = string_in_russian + cyrillic
    return string_in_russian

u2a = {'й': 'j', 'ц': 'c', 'у': 'u', 'к': 'k',
     'е': 'e', 'н': 'n', 'г': 'g', 'ш': 's',
     'щ': 's', 'з': 'z', 'х': 'h', 'ъ': '`',
     'ф': 'f', 'ы': 'y', 'в': 'v', 'а': 'a',
     'п': 'p', 'р': 'r', 'о': 'o', 'л': 'l',
     'д': 'd', 'ж': 'z', 'э': 'e',
     'я': 'a', 'ч': 'c', 'с': 's', 'м': 'm',
     'и': 'i', 'т': 't', 'ь': '`', 'б': 'b',
     'ю': 'u', 'ё': 'o'
     }

def to_latin(string_in_russian):
    ascii_string = ''
    for cyrillic in string_in_russian:
        try:
            latin = u2a[cyrillic]
        except:
            latin = '' + cyrillic
        ascii_string = ascii_string + latin
    return ascii_string
