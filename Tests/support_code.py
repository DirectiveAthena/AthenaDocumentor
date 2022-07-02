# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Class -
# ----------------------------------------------------------------------------------------------------------------------
class Person:
    """A person class for a game"""

    name:str
    age:int
    health:int

    def __init__(self, name:str, age:int, health=100):
        self.name=name
        self.age=age
        self.health=health

    def affect_health(self, amount:int):
        """The function affects the health of the Person object"""
        self.age += amount

    def kill(self):
        """Sets the health of a Person to 0"""
        self.age = 0

    def clone(self) -> Person:
        """Clones the current Person into a new object"""
        return Person(self.name, self.age, self.health)

PERSON ={'doc': 'A person class for a game',
 'methods': [{'doc': 'Initialize self.  See help(type(self)) for accurate '
                     'signature.',
              'name': '__init__',
              'parent_module': 'Tests.support_code',
              'signature': "(self, name: 'str', age: 'int', health=100)",
              'type': '#method'},
             {'doc': 'The function affects the health of the Person object',
              'name': 'affect_health',
              'parent_module': 'Tests.support_code',
              'signature': "(self, amount: 'int')",
              'type': '#method'},
             {'doc': 'Sets the health of a Person to 0',
              'name': 'kill',
              'parent_module': 'Tests.support_code',
              'signature': '(self)',
              'type': '#method'},
             {'doc': 'Clones the current Person into a new object',
              'name': 'clone',
              'parent_module': 'Tests.support_code',
              'signature': "(self) -> 'Person'",
              'type': '#method'}],
 'name': 'Person',
 'parent_module': 'Tests.support_code',
 'signature': "(name: 'str', age: 'int', health=100)",
 'type': '#class'}
# ----------------------------------------------------------------------------------------------------------------------
# - Function -
# ----------------------------------------------------------------------------------------------------------------------
def random_function(a:int, b:int) -> int:
    """this is quite the random function"""
    return a+b

RANDOM_FUNCTION = {'doc': 'this is quite the random function',
 'name': 'random_function',
 'parent_module': 'Tests.support_code',
 'signature': "(a: 'int', b: 'int') -> 'int'",
 'type': '#func'}

# ----------------------------------------------------------------------------------------------------------------------
# - object -
# ----------------------------------------------------------------------------------------------------------------------
strange_object = {"help":["I am trapped in a list"]}

# ----------------------------------------------------------------------------------------------------------------------
# - Full MD output -
# ----------------------------------------------------------------------------------------------------------------------
ATHENADOCUMENTOR_MD = f"""#class <small>AthenaDocumentor.</small>**OutputMarkdown**()

The OutputMarkdown supports the `Parser` in formatting `ParsedObject` objects to the defined format.



---


#class <small>AthenaDocumentor.</small>**ParsedObject**(obj)

ParsedObject(obj)

$\qquad$**__init__**(self, obj)

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**to_dict**(self) -> dict

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</span>

$\qquad$**__eq__**(self, other)

<span class="parent_indent">Return self==value.</s

---


#class <small>AthenaDocumentor.</small>**Parser**(*, root_module: Any, markdown_structure: type[OutputMarkdown] = <class AthenaDocumentor.models.markdown_structure.OutputMarkdown>) -> None

Object to control the correct handling of parsing through a Python package

$\qquad$**parse**(self) -> Parser

<span class="parent_indent">Main method of the Parser object.
Running this will start the pared and populate the 'parsed_items' slot of the Parser object</span>

$\qquad$**_parse_recursive**(self, module_to_parse: Any)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**output_to_dict**(self, *, flat: bool = False) -> dict[str:list[dict]]

<span class="parent_indent">Output the 'parsed_items' dictionary as is, or with custom parameters.</span>

$\qquad$**output_to_json_file**(self, filepath: str)

<span class="parent_indent">Output the 'parsed_items' dictionary to a json file.
This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`</span>

$\qquad$**_output_to_markdown**(self)

<span class="parent_indent">*<span style=color:red>-!- Missing documentation -!-</span>*</span>

$\qquad$**output_to_markdown_file**(self, filepath: str)

<span class="parent_indent">Output the 'parsed_items' to a structured MarkDown file.</span>

$\qquad$**output_to_markdown_string**(self) -> str

<span class="parent_indent">Output the 'parsed_items' to string, formatted in MarkDown</span>

$\qquad$**__init__**(self, *, root_module: Any, markdown_structure: type[OutputMarkdown] = <class AthenaDocumentor.models.markdown_structure.OutputMarkdown>) -> None

<span class="parent_indent">Initialize self.See help(type(self)) for accurate signature.</span>

$\qquad$**__repr__**(self)

<span class="parent_indent">Return repr(self).</s

---


#class <small>AthenaDocumentor.data.types.</small>**Types**(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

$\qquad$**_generate_next_value_**(name, start, count, last_values)

<span class="parent_indent">Generate the next value when not given.
name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None</span>

$\qquad$**__new__**(cls, value)

<span class="parent_indent">Create and return a new object.See help(type) for accurate signature.</s

---


#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**indent_all_lines**(text: str, indent: int) -> str

Indents all lines in a string with a defined amount of indentation

---


#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**quote_all_lines**(text: str) -> str

Places a quote prefix in front of all lines in a string

---


#func <small>AthenaDocumentor.functions.markdown_string_manipulations.</small>**remove_empty_prefix**(text: str) -> str

*<span style=color:red>-!- Missing documentation -!-</span>*

---


#func <small>AthenaDocumentor.functions.type_finder.</small>**find_type**(obj) -> Types

*<span style=color:red>-!- Missing documentation -!-</span>*

---

"""