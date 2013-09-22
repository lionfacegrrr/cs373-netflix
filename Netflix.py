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
    return (map(int, s.split()) for s in r)




# ------------
# netflix_the_math
# ------------

def netflix_the_math (n,v,w) :
    """here is where i calculate for netflix"""
    if v == 0 :
        if n == 1 :
            return 1
        else :
            if (n % 2) == 0 :
                n = (n >> 1)
                v = netflix_the_math(n,v,w)
                v = v + 1
            else :
                n = (((3 * n) + 1) >> 1)
                v = netflix_the_math(n,v,w)
                v = v + 2
    return v


# ------------
# netflix_the_iteration
# ------------

def netflix_the_iteration (first,last,w) :
    """
    this should be where i sort out each number in the 
    string of numbers and send it to netflix_the_math 
    i should be handling greatest v here too
    assert first < last
    quiz3trick = 0
    quiz3trick = last / 2
    if (first < quiz3trick):
        first = quiz3trick
    biggest_v = 1
    test_v = 1
    v = 0
    for x in range(first, (last+1)):
        test_v = netflix_the_math(x,v,w)
        if ( biggest_v < test_v) :
            biggest_v = test_v
    assert biggest_v > 0
    return biggest_v
	^ABOVE IS ALL MY OLD CODE FOR COLLATZ INCASE I NEED IT^
    """


# ------------
# netflix_eval
# ------------

def netflix_eval ((idnumber, punctuation, date),w) :

    assert idnumber != None
    assert punctuation != None
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
	assert idnumber != None
    assert punctuation != None
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
