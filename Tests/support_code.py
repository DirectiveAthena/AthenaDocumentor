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

PERSON = {
    'doc': 'A person class for a game',
    'methods': [{'doc': 'Initialize self.  See help(type(self)) for accurate '
                     'signature.',
              'methods': [],
              'name': '__init__',
              'parent_module': 'Tests.support_code',
              'signature': "(self, name: 'str', age: 'int', health=100)",
              'type': '#func'},
             {'doc': 'The function affects the health of the Person object',
              'methods': [],
              'name': 'affect_health',
              'parent_module': 'Tests.support_code',
              'signature': "(self, amount: 'int')",
              'type': '#func'},
             {'doc': 'Sets the health of a Person to 0',
              'methods': [],
              'name': 'kill',
              'parent_module': 'Tests.support_code',
              'signature': '(self)',
              'type': '#func'},
             {'doc': 'Clones the current Person into a new object',
              'methods': [],
              'name': 'clone',
              'parent_module': 'Tests.support_code',
              'signature': "(self) -> 'Person'",
              'type': '#func'}],
     'name': 'Person',
     'parent_module': 'Tests.support_code',
     'signature': "(name: 'str', age: 'int', health=100)",
     'type': '#class'
}
# ----------------------------------------------------------------------------------------------------------------------
# - Function -
# ----------------------------------------------------------------------------------------------------------------------
def random_function(a:int, b:int) -> int:
    """this is quite the random function"""
    return a+b

RANDOM_FUNCTION = {
    'doc': 'this is quite the random function',
     'methods': [],
     'name': 'random_function',
     'parent_module': 'Tests.support_code',
     'signature': "(a: 'int', b: 'int') -> 'int'",
     'type': '#func'
}

# ----------------------------------------------------------------------------------------------------------------------
# - object -
# ----------------------------------------------------------------------------------------------------------------------
strange_object = {"help":["I am trapped in a list"]}