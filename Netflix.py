#!/usr/bin/env python

# ---------------------------
# ~/Desktop/cs373-netflix/Netflix.py
# Copyright (C) 2013
# Robert A. Hammond
# RAH584
# ---------------------------

# ------------
# netflix_read
# ------------

def netflix_read (r) :
    """
    r is a  reader
    returns an generator that iterates over a sequence of lists of ints of length 2
    for s in r :
        l = s.split()
        b = int(l[0])
        e = int(l[1])
        yield [b, e]
    """
    line = (map(str, s.split(' ')) for s in r)
	if line[2]
#this isnt working right now so fix it 
    return line




# ------------
# netflix_eval
# ------------

def netflix_eval ((idnumber, punctuation, date),w) :

#assert (idnumber <> None)
#assert (punctuation <> None)
    if date == None :
    	w.write("movie :   >")
    	return 1
    else:
    	w.write("vote      >")
    	return 2
    return 0

# -------------
# netflix_print
# -------------

def netflix_print (w, (idnumber, punctuation, date), prediction) :
    """

    """
#assert (idnumber <> None)
#assert (punctuation <> None)
    if date == None :
    	w.write(str(idnumber) + " " + str(punctuation) + "\n")
    else:
    	w.write(str(idnumber) + " " + str(punctuation) + " " + str(date) + " " + str(prediction) + "\n")
    

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    t is a line from reader
    """
    for t in netflix_read(r) :
        prediction = netflix_eval(t,w)
        netflix_print(w, t, prediction)
