# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed import Parsed

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Output(ABC):
    """
    Standardized way of outputting correctly parsed objects into string objects.
    Used by the parser `output_...` methods to correctly form the wanted text version

    The base Output class is an abstract class, which means the classes that inherit from it,
    must implement all following methods.
    """
    # ------------------------------------------------------------------------------------------------------------------
    # - Formatting text snippets -
    # ------------------------------------------------------------------------------------------------------------------
    @classmethod
    @abstractmethod
    def format_documentation(cls,parsed_object:Parsed) -> str:
        """
        Formats the `parsed_object.doc` into a correct string.

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def format_type(cls, parsed_object:Parsed) -> str:
        """
        Formats the `parsed_object.type` into a correct string.

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def format_module_name(cls, parsed_object:Parsed) -> str:
        """
        Formats the `parsed_object.module_name` into a correct string.

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def format_object_name(cls, parsed_object:Parsed) -> str:
        """
        Formats the `parsed_object.name` into a correct string.

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def format_signature(cls, parsed_object:Parsed) -> str:
        """
        Formats the `parsed_object.signature` into a correct string.

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def format_header(cls, parsed_object: Parsed) -> str:
        """
        Formats multiple components of `parsed_object` together.
        This forms the piece of documentation that display the name, signature, type and other similar components.

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def format_footer(cls, parsed_object: Parsed) -> str:
        """
        Formats multiple components of `parsed_object` together.
        This forms the piece of documentation that display the end of the piece of documentation for that `parsed_object`

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    # - Full structures -
    # ------------------------------------------------------------------------------------------------------------------
    @classmethod
    @abstractmethod
    def structure_function(cls, parsed_object:Parsed) -> str:
        """
        Calls on other `Output` methods to export a sensible string for a function object

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def structure_class(cls,parsed_object: Parsed) -> str:
        """
        Calls on other `Output` methods to export a sensible string for a class object

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

    @classmethod
    @abstractmethod
    def structure_method(cls, parsed_object: Parsed) -> str:
        """
        Calls on other `Output` methods to export a sensible string for a method object

        Parameters:
        - parsed_object:Parsed

        Returns: str
        """
        pass

