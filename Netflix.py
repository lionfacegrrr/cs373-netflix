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
    """
    line = (map(str, s.split()) for s in r)
    if len(line) == 3 :
        return line
    elif len(line) == 2 :
        return line
    else:
        print ("we have a problem in read \n")
#this isnt working right now so fix it 
    return line



# ------------
# netflix_eval_movie
# ------------

def netflix_eval_movie ((idnumber, punctuation),w) :
    print ("--we could read the line and it is now in movie-- \n")
    return 0


# ------------
# netflix_eval_user
# ------------

def netflix_eval_user ((idnumber, punctuation, date),w) :

    print ("~~we could read the line and can listen to the customer~~")
    return 1

# -------------
# netflix_print_user
# -------------

def netflix_print_user (w, (idnumber, punctuation, date), prediction) :
    """

    """
    	w.write(str(idnumber) + " " + str(punctuation) + " " + str(date) + " " + str(prediction) + "\n")

# -------------
# netflix_print_movie
# -------------

def netflix_print_movie (w, (idnumber, punctuation), prediction) :
    """
        
        """
            w.write(str(idnumber) + " " + str(punctuation) + " " + str(prediction) + "\n")

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
        if len(prediction) == 3 :
            netflix_eval_user(prediction,w)
            netflix_print_user(w, t, prediction)
        elif len(prediction) == 2 :
            netflix_eval_movie(prediction,w)
            netflix_print_movie(w, t, prediction)
        else:
            print ("we have a problem in solve \n")
