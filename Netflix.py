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
    return (map(str, s.split()) for s in r)
    """
        r is a  reader
        
        old code:
        if len(line) == 3 :
        return line
        elif len(line) == 2 :
        return line
        else:
        print ("we have a problem in read \n")
        #this isnt working right now so fix it
        return line
    """



# ------------
# netflix_eval_movie
# ------------

def netflix_eval_movie ((idnumber, punctuation),w) :
    print ("--we could read the line and it is now in movie-- \n")
    return 0


# ------------
# netflix_eval_user
# ------------

def netflix_eval_user ((idnumber),w) :

    print ("~~we could read the line and can listen to the customer~~")
    return 1

# -------------
# netflix_print_user
# -------------

def netflix_print_user (w, idnumber, prediction) :
    """

    """
    w.write(str(idnumber) + " " + str(prediction) + "\n")

# -------------
# netflix_print_movie
# -------------

def netflix_print_movie (w, (idnumber, punctuation)) :
    """
    
    """
    w.write(str(idnumber) + " " + str(punctuation) + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    t is a line from reader
    \/at some point i should impliment a function to gain access to their caches here
    """
    for t in netflix_read(r) :
    	rateing = -1
        if len(t) == 1 :
        	rateing = netflix_eval_user(t,w)
        	netflix_print_user(w, t[0], rateing)
        elif len(t) == 2 :
        	rateing = netflix_eval_movie(t,w)
        	netflix_print_movie(w, t)
        else:
            w.write("we have a problem in solve \n")
