from typing import Dict
import csv

def sanitise(x: str) -> str:
    """
    Sanitise a string for use in a file name.
    
    Parameters
    ----------
    x : str
        String to be sanitised.
    
    Returns
    -------
    str
        Sanitised string.

    Examples
    --------
    >>> sanitise("Hello World")
    "Hello_World"
    >>> sanitise("Hello/World")
    "Hello_World"
    >>> sanitise("Hello (World)")
    "Hello_World"
    """
    return x.replace(" ","_").replace("/","_").replace("(","").replace(")","")

def load_data(input_file: str, id_column: str) -> Dict[str,dict]:
    """
    Load data from a csv file.
    
    Parameters
    ----------
    input_file : str
        Input file name.
    id_column : str
        Column name matching the sequence IDs used in the tree.
    
    Returns
    -------
    dict
        Dictionary of dictionaries for each column in the csv file.
    """
    data = {}
    rows = []
    for row in csv.DictReader(open(input_file,encoding="utf-8-sig")):
        rows.append(row)
    columns = list(rows[0].keys())
    for column in columns:
        if column != id_column:
            data[column] = {row[id_column]:row[column] for row in rows if row[column] != ""}
    return data

def load_binary_matrix_data(input_file: str, id_column: str) -> Dict[str,dict]:
    """
    Load data from a csv file.
    
    Parameters
    ----------
    input_file : str
        Input file name.
    id_column : str
        Column name matching the sequence IDs used in the tree.
    
    Returns
    -------
    dict
        Dictionary of dictionaries for each column in the csv file.
    """
    data = {}
    for row in csv.DictReader(open(input_file,encoding="utf-8-sig")):
        index = row[id_column]
        del row[id_column]
        print(set(row.values()))
        assert set(row.values()).issubset(set(["0","1"])), "Binary matrix must contain only 0s and 1s"
        data[index] = row

    
    return data
