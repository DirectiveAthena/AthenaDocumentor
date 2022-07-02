# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def indent_all_lines(text:str, indent:int) -> str:
    """
    Indents all lines in a string with a defined amount of indentation

    Parameters:
    - text : str -> input text
    - indent : int -> amount of whitespaces that has to be added before everything else
    """
    indentation:str = " "*indent
    text_indented = text.replace("\n", f"\n{indentation}")
    return f"{indentation}{text_indented}"

def quote_all_lines(text:str) -> str:
    """
    Places a quote prefix in front of all lines in a string

    Parameters:
    - text : str -> input text
    """
    text_indented = text.replace("\n", f"\n> ")
    return f"> {text_indented}"

def remove_empty_prefix(text:str) -> str:
    """
    Removes any double spaces ("  ")

    Parameters:
    - text : str -> input text
    """
    return text.replace("  ", "")

