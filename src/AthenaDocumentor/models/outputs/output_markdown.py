# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect

# Custom Library

# Custom Packages
from AthenaDocumentor.models.outputs.output import Output
from AthenaDocumentor.models.parsed import Parsed, ParsedMethod,ParsedClass,ParsedFunction

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class OutputMarkdown(Output):
    """
    The OutputMarkdown supports the `Parser` in formatting `Parsed` objects to a Markdown format.
    """
    indent:int = 4

    missing_documentation:str = "*`-!- Missing documentation -!-`*"
    default_footer:str = "\n\n---\n\n"

    # ----------------------------------------------------------------------------------------------------------------------
    # - Formatting text snippets -
    # ----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def format_documentation(cls,parsed_object:Parsed) -> str:
        if isinstance(parsed_object.obj, classmethod|staticmethod):
            doc = inspect.getdoc(parsed_object.obj.__func__)
        else:
            doc = inspect.getdoc(parsed_object.obj)
        if doc is None or not doc:
            return cls.missing_documentation
        return doc

    @classmethod
    def format_type(cls, parsed_object:Parsed) -> str:
        return parsed_object.type.value
    @classmethod
    def format_module_name(cls, parsed_object:Parsed) -> str:
        return f"{parsed_object.parent_module.__name__}."
    @classmethod
    def format_object_name(cls, parsed_object:Parsed) -> str:
        return f"**{parsed_object.obj_name}**"
    @classmethod
    def format_signature(cls, parsed_object:ParsedFunction|ParsedMethod|ParsedClass) -> str:
        return str(parsed_object.signature).replace("'", "")

    @classmethod
    def format_header(cls, parsed_object: ParsedFunction|ParsedMethod|ParsedClass) -> str:
        type_:str = cls.format_type(parsed_object)
        module_name:str = cls.format_module_name(parsed_object)
        object_name:str = cls.format_object_name(parsed_object)
        signature:str = cls.format_signature(parsed_object)
        return f"{type_} {module_name}{object_name}{signature}"

    @classmethod
    def format_footer(cls, parsed_object: Parsed) -> str:
        return cls.default_footer

    # ----------------------------------------------------------------------------------------------------------------------
    # - Full structures -
    # ----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def structure_function(cls, parsed_object:ParsedFunction|ParsedMethod) -> str:
        header = cls.format_header(parsed_object)
        footer = cls.format_footer(parsed_object)
        return f"{header}\n\n{cls.format_documentation(parsed_object)}{footer}"

    @classmethod
    def structure_class(cls,parsed_object: ParsedClass) -> str:
        header = cls.format_header(parsed_object)
        methods:str = "\n\n".join(
            cls.structure_method(method)
            for method in parsed_object.methods
        )
        footer = cls.format_footer(parsed_object)
        return f"{header}\n\n{cls.format_documentation(parsed_object)}\n\n{methods}{footer}"

    @classmethod
    def structure_method(cls, parsed_object: ParsedFunction|ParsedMethod) -> str:
        object_name:str = cls.format_object_name(parsed_object)
        signature:str = cls.format_signature(parsed_object)
        documentation = cls.format_documentation(parsed_object)
        return f'{object_name}{signature}\n\n{documentation}'