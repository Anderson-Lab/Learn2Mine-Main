#!/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

"""
Simple script to add a prefix to every line in a file.
"""

import sys

for line in sys.stdin: print sys.argv[1] + line,
