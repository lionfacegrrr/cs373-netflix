#!/usr/bin/env python

# ---------------------------
# ~/Desktop/cs373-netflix/Netflix.py
# Copyright (C) 2013
# Robert A. Hammond
# RAH584
# ---------------------------

# ------------
# imports
# ------------

import io
movies = open('movie_cache.txt').readlines()
users  = open('users_cache.txt').readlines()
currentmovie = 0
currentmovierate = 1
currentuser  = 0
currentuserrate = 5

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
    global currentmovie
    global currentmovierate
    print ("--we could read the movie--")
    currentmovie = idnumber
    w.write("======>" + str(movies.index(idnumber + ":")) + "\n")
    #w.write(str(idnumber) + " " + str(punctuation) + "\n")
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
    #w.write(str(idnumber) + " " + str(prediction) + "\n")

# -------------
# netflix_print_movie
# -------------

def netflix_print_movie (w, (idnumber, punctuation)) :
    """
    
    """
    #w.write(str(idnumber) + " " + str(punctuation) + "\n")

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
    #training = io.open("/u/downing/cs/netflix/training_set/*", "r")
    qualifying = io.open("/u/downing/cs/netflix/qualifying.txt", "r")
        
    titles = open('movie_titles.txt').readlines()
    titles.reverse()
    """
    global movies
    global users
    movies.sort()
    users.sort()
    nums = 0 #this should be a string representation of what i read in for the line
    rateing = 3.7 #the best value to start with according to document on assignment
    for t in netflix_read(r) : #parse through my RunNetflix and look at each line
    	nums = t[(len(t)-2)]  #take the string from the tuple t (['OUR_STRING'])
    	#print (nums + "is of type" + str(type(nums)) + "\n")
        if not ':' in nums : #it must be a customer if no colon
	    	currentuserrate = rateing + 0.05 #lets assume this guy is a movie buff by .05
	    	currentuser = int(nums)
	    	currentuserrate += currentmovierate
	    	currentuserrate /= 2
	    	w.write(nums + " " + str(currentuserrate) + "\n")
	    	#w.write(nums +  "	user:" + str(currentuser) + "	rate:" + str(currentuserrate)  + "\n")
        	#rateing = netflix_eval_user(t,w)
        	#netflix_print_user(w, t[0], rateing)
        elif ':' in nums :
        	currentmovie = int(nums.rstrip(':')) #just remember you still have a : appended to the end
        	currentmovierate = rateing
	    	w.write(nums + "\n") #+ "		"+ "movie:" + str(currentmovie) + "		rate:" + str(currentmovierate)  + "\n")
	    	#netflix_print_movie(w, (nums[:(len(nums)-1)], nums[(len(nums)-2):]))
        else:
            w.write("we have a problem in netflix_solve and nums is: " + nums + "\n")
