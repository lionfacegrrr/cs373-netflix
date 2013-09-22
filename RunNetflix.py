#!/usr/bin/env python

# ------------------------------
# ~/Desktop/cs373-netflix/RunNetflix.py
# Copyright (C) 2013
# Robert A. Hammond
# RAH584
# ---------------------------

"""
To run the program
    % python RunNetflix.py < RunNetflix.in > RunNetflix.out
    % chmod ugo+x RunNetflix.py
    % RunNetflix.py < RunNetflix.in > RunNetflix.out

To document the program
    % pydoc -w Netflix
"""

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

netflix_solve(sys.stdin, sys.stdout)
