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
import math
expected = open('ExpectedRunNetflix.txt').readlines()
usercount = 0
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
# print_rmse
# -------------

def print_rmse (myzipper,w) :
	v = sum([(x - y) ** 2 for x, y in myzipper], 0.0)
	w.write("RMSE : " + str(math.sqrt(v / usercount)))
	"""
	here is where i handle getting rmse with my zipper of expected and actual output
	s = len(a) == usercount
	z = zip(a, p) == myzipper
	v = sum([(x - y) ** 2 for x, y in myzipper], 0.0)
	#w.write("RMSE : " + str(math.sqrt(v / usercount)))
	"""

# -------------
# find_needed_lines : I used this function to build my cache and then i changed it to refine my cache to just the ratings
# -------------
def find_needed_lines (users_keeper,w) :
	#my_lookup_file = open('mv_0010034.txt').readlines()
	neededlist = []
	fixer = 0
	with open('ExpectedRunNetflix.txt', 'r') as inF:
		for line in inF:
			if ':' in line :
				w.write(line)
			else :
				for i in line:
					if fixer == 1 :
						w.write(i + "\n")
						fixer = 0
						break
					if i == ',' :
						fixer = 1

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w):
	global usercount
	global expected #remember rob that this list is backwards len()-iter
	iter = -1
	#print (str(type(expected)) + "	"+str(expected))
	users_keeper = []
	myzipper = [] #this is what we use for zipping my two ratings for rmse
	nums = 0 #this should be a string representation of what i read in for the line
	rateing = 3.9 #the best value to start with according to document on assignment
	for t in netflix_read(r) :
		iter +=1
		nums = t[(len(t)-2)]
		if not ':' in nums : #it must be a customer if no colon
			users_keeper.append(nums)
			usercount +=1
			currentuserrate = rateing + 0.09 #lets assume this guy is a movie buff by .05
			currentuser = int(nums)
			currentuserrate += currentmovierate
			currentuserrate /= 2
			myzipper.append((currentuserrate,float(expected[iter])))
			w.write(nums + " " + str(currentuserrate) + "\n")
			#w.write("<<<<<<<<<<<<<<<<<" + str(expected[iter]) + "\n")
		elif ':' in nums :
			currentmovie = int(nums.rstrip(':')) #just remember you still have a : appended to the end
			currentmovierate = rateing
			#w.write(nums + "\n") #+ "		"+ "movie:" + str(currentmovie) + "		rate:" + str(currentmovierate)  + "\n")
		else:
			w.write("we have a problem in netflix_solve and nums is: " + nums + "\n")
	#users_keeper = find_needed_lines(users_keeper,w)
	print_rmse(myzipper,w)