import re
import numpy as np
from ast import literal_eval

def format_query(query):
    """
    Formats a list of numbers as a string with each number rounded to 6 decimal places and separated by a hyphen.
    Parameters:
        query (list): A list of numbers to be formatted.
    Returns:
        str: A string with each number in the input list rounded to 6 decimal places and separated by a hyphen.
    Example:
        >>> format_query([1.23456789, 0.3456789, 3.456789])
        '1.234568-0.345679-3.456789'
    """
    x = ''
    for i in range(len(query)):
        x += str(format(query[i], '0.6f'))
        if i != len(query) - 1:
            x += '-'
    return x

def get_function_data_from_file(filename, function_number):
    with open(filename, 'r') as f:
        txt = f.read()
    
    return get_function_data(txt, function_number)

def get_function_data(txt, function_number):
    
    # normalise the text
    txt = normalise_text(txt)

    # create array to store results
    results = []

    # split txt into lines
    lines = txt.splitlines()

    # for each line in lines
    for line in lines:
        result = get_function_data_from_line(line, function_number)
        results.append(result)
    
    return results

def get_function_data_from_line(line, function_number):
    # Replacing "array" with "" and removing whitespace
    line = line.replace("array", "").replace(" ", "")

    # Converting the string to list of lists using literal_eval
    lst = literal_eval(line)

    # Converting list of lists to list of numpy arrays
    np_arrays = [np.array(l) for l in lst]

    array = np_arrays[function_number - 1]
    
    return array

def normalise_text(txt):
    """
    Normalizes the given text by removing line wraps and multiple spaces.
    
    Parameters:
        txt (str): The text to be normalized.
    
    Returns:
        str: The normalized text.
    """
    # removing line wrap (only if there is a space after the newline character)
    txt = re.sub(r"\n[\s]+", " ", txt)

    # removing multiple spaces
    txt = re.sub(r" +", " ", txt)

    return txt