#!/usr/bin/env python

# -------------------------------
# ~/Desktop/cs373-netflix/TestNetflix.py
# Copyright (C) 2013
# Robert A. Hammond
# RAH584
# ---------------------------

"""
    To test the program:
    % python TestNetflix.py > TestNetflix.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py > TestNetflix.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
    # ----
    # read
    # ----
    #making sure i can read in one movieline
    def test_read_1 (self) :
        r = StringIO.StringIO("1 :\n")
        p = netflix_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == ':')
    
    
    # ----
    # eval
    # ----
    #looking to see if it can read a movie
    def test_eval_1 (self) :
        v = netflix_eval((1 , ':'))
        self.assert_(v == 1)
    

    # -----
    # print
    # -----
    #looking to see if i can print a movie
    def test_print_1 (self) :
        w = StringIO.StringIO()
        netflix_print(w, (1, ':', None), 1)
        self.assert_(w.getvalue() == "1 : 1\n")

    
    # -----
    # solve
    # -----
    
    def test_solve_1 (self) :
        r = StringIO.StringIO(" 1 :\n 2 :\n 3 :\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == " 1 : 1\n 2 : 1\n 3 : 1\n")



# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."