import sys
import os

import pathlib

src = pathlib.Path(__file__).parent / 'my_amazing_package'

# Adjust the path to include your package directory.
sys.path.insert(0, os.path.abspath(src))
