from .PEDataObject import PEDataObject
from .DataObject import DataObject
from .command_line import getListOfFilesForDirectory

import sys

if len(sys.argv) < 1:
    print("Usage: python3 scanner.py <dirname>")
    exit(0)

files = getListOfFilesForDirectory(sys.argv[1])

