import os

def load_files(path_to_folder):
    path_separator = '/'
    list_of_strings = []
    list_of_fields = []
    field_separator = '\t'
    field_number = -1
    for dirpath, dirnames, filenames in os.walk(path_to_folder):
        for filename in filenames:
            # print(filename)
            path_to_file = dirpath + path_separator + filename
            # print(path_to_file)
            with open(path_to_file, 'r') as f:
                for string in f:
                    # print(string)
                    list_of_fields = string.split(field_separator)
                    list_of_strings.append(list_of_fields[field_number])
    return list_of_strings
