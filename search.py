def search(term, list_of_strings):
    results_strings = []
    for string in list_of_strings:
        if term in string:
            results_strings.append(string)
    return results_strings
