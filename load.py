# -*- coding: utf-8 -*-

import os
import codecs

def load_files(path_to_folder):
    list_of_strings = []
    for dirpath, dirnames, filenames in os.walk(path_to_folder):
        for filename in filenames:
            # print filename
            path_to_file = path_to_folder + '/' + filename
            with codecs.open(path_to_file, 'r', encoding = 'utf-8') as f:
                for string in f:
                    # print string
                    list_of_strings.append(string)
    return list_of_strings
