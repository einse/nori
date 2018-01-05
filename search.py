def search(term, list_of_strings):
    list_of_results = []
    for string in list_of_strings:
        if term in string:
            list_of_results.append(string)
    return list_of_results
