# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaDocumentor

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    parser = AthenaDocumentor.Parser(root_module=AthenaDocumentor).parse()
    # output the entire package to Obsidian
    parser.output_to_markdown_file(
        r"D:\Directive Athena\Programs\Veritas\Storage\Documentation\Content\Programming\AthenaDocumentor\reference.md"
    )

if __name__ == '__main__':
    main()