SUMMARY
================================================================================

This dataset was constructed to support participants in the Netflix Prize.  See
http://www.netflixprize.com for details about the prize.

The movie rating files contain over 100 million ratings from 480 thousand
randomly-chosen, anonymous Netflix customers over 17 thousand movie titles.  The
data were collected between October, 1998 and December, 2005 and reflect the
distribution of all ratings received during this period.  The ratings are on a
scale from 1 to 5 (integral) stars. To protect customer privacy, each customer
id has been replaced with a randomly-assigned id.  The date of each rating and
the title and year of release for each movie id are also provided.


USAGE LICENSE
================================================================================

Netflix can not guarantee the correctness of the data, its suitability for any
particular purpose, or the validity of results based on the use of the data set.
The data set may be used for any research purposes under the following
conditions:

     * The user may not state or imply any endorsement from Netflix.

     * The user must acknowledge the use of the data set in
       publications resulting from the use of the data set, and must
       send us an electronic or paper copy of those publications.

     * The user may not redistribute the data without separate
       permission.

     * The user may not use this information for any commercial or
       revenue-bearing purposes without first obtaining permission
       from Netflix.

If you have any further questions or comments, please contact the Prize
administrator <prizemaster@netflix.com>


TRAINING DATASET FILE DESCRIPTION
================================================================================

The file "training_set.tar" is a tar of a directory containing 17770 files, one
per movie.  The first line of each file contains the movie id followed by a
colon.  Each subsequent line in the file corresponds to a rating from a customer
and its date in the following format:

CustomerID,Rating,Date

- MovieIDs range from 1 to 17770 sequentially.
- CustomerIDs range from 1 to 2649429, with gaps. There are 480189 users.
- Ratings are on a five star (integral) scale from 1 to 5.
- Dates have the format YYYY-MM-DD.

MOVIES FILE DESCRIPTION
================================================================================

Movie information in "movie_titles.txt" is in the following format:

MovieID,YearOfRelease,Title

- MovieID do not correspond to actual Netflix movie ids or IMDB movie ids.
- YearOfRelease can range from 1890 to 2005 and may correspond to the release of
  corresponding DVD, not necessarily its theaterical release.
- Title is the Netflix movie title and may not correspond to 
  titles used on other sites.  Titles are in English.


QUALIFYING AND PREDICTION DATASET FILE DESCRIPTION
================================================================================

The qualifying dataset for the Netflix Prize is contained in the text file
"qualifying.txt".  It consists of lines indicating a movie id, followed by a
colon, and then customer ids and rating dates, one per line for that movie id.
The movie and customer ids are contained in the training set.  Of course the
ratings are withheld. There are no empty lines in the file.

MovieID1:
CustomerID11,Date11
CustomerID12,Date12
...
MovieID2:
CustomerID21,Date21
CustomerID22,Date22

For the Netflix Prize, your program must predict the all ratings the customers
gave the movies in the qualifying dataset based on the information in the
training dataset.

The format of your submitted prediction file follows the movie and customer id,
date order of the qualifying dataset.  However, your predicted rating takes the
place of the corresponding customer id (and date), one per line.

For example, if the qualifying dataset looked like:

111:
3245,2005-12-19
5666,2005-12-23
6789,2005-03-14
225:
1234,2005-05-26
3456,2005-11-07

then a prediction file should look something like:
111:
3.0
3.4
4.0
225:
1.0
2.0

which predicts that customer 3245 would have rated movie 111 3.0 stars on the
19th of Decemeber, 2005, that customer 5666 would have rated it slightly higher
at 3.4 stars on the 23rd of Decemeber, 2005, etc.

You must make predictions for all customers for all movies in the qualifying
dataset.

THE PROBE DATASET FILE DESCRIPTION
================================================================================

To allow you to test your system before you submit a prediction set based on the
qualifying dataset, we have provided a probe dataset in the file "probe.txt".
This text file contains lines indicating a movie id, followed by a colon, and
then customer ids, one per line for that movie id.

MovieID1:
CustomerID11
CustomerID12
...
MovieID2:
CustomerID21
CustomerID22

Like the qualifying dataset, the movie and customer id pairs are contained in
the training set.  However, unlike the qualifying dataset, the ratings (and
dates) for each pair are contained in the training dataset.

If you wish, you may calculate the RMSE of your predictions against those
ratings and compare your RMSE against the Cinematch RMSE on the same data.  See
http://www.netflixprize.com/faq#probe for that value.


Good luck!


MD5 SIGNATURES AND FILE SIZES
================================================================================

d2b86d3d9ba8b491d62a85c9cf6aea39        577547 movie_titles.txt #same in my code
ed843ae92adbc70db64edbf825024514      10782692 probe.txt #in my program this is RunNetflix.in
88be8340ad7b3c31dfd7b6f87e7b9022      52452386 qualifying.txt #same in my code
0e13d39f97b93e2534104afc3408c68c           567 rmse.pl #dont think i need this since i can implement and/or use library according to piazza
0098ee8997ffda361a59bc0dd1bdad8b    2081556480 training_set.tar #not sure how i can deal with this




----------------------------------------------------------------------------------------------------
Netflix Prize Data Set  

Abstract: This is the official data set used in the Netflix Prize 
competition. The data consists of about 100 million movie ratings, and 
the goal is to predict missing entries in the movie-user rating matrix.

------------------------------------------------------------------------

Data Set Characteristics:  Multivariate, Time-Series
Attribute Characteristics: Integer
Associated Tasks: Clustering, Recommender-Systems
Number of Instances: 100480507
Number of Attributes: 17770
Area: N/A
Missing Values? Yes
Date Donated: 2009-09-21

------------------------------------------------------------------------

Source:

Netflix Prize

http://www.netflixprize.com

------------------------------------------------------------------------

Data Set Information:

This dataset was constructed to support participants in the Netflix Prize. See
http://www.netflixprize.com/ for details about the prize.

There are over 480,000 customers in the dataset, each identified by a
unique integer id.

The title and release year for each movie is also provided. There are over
17,000 movies in the dataset, each identified by a unique integer id.

The dataset contains over 100 million ratings. The ratings were collected
between October 1998 and December 2005 and reflect the distribution of all
ratings received during this period. Each rating has a customer id, a movie id,
the date of the rating, and the value of the rating.

As part of the original Netflix Prize a set of ratings was identified whose
rating values were not provided in the original dataset. The object of the
Prize was to accurately predict the ratings from this 'qualifying' set. These
missing ratings are now available in the grand_prize.tar.gz dataset file. 

-------------------------------------------------------------------------------

Attribute Information:

The format of the data is described fully in the README files contained in the
dataset tar files.

MovieID:
Arbitrarily assigned unique integer in the range [1 .. 17770].

CustomerID:
Arbitrarily assigned unique integer in the range [1..2649429] (with gaps).

Rating:
Number of 'stars' assigned to a movie by a customer; an integer from 1 to 5.

Title:
English language title of the movie on the Netflix website.

YearOfRelease:
Year a movie was released in the range [1890..2005]. May correspond to the
release of corresponding DVD, not necessarily its theaterical release.

Date:
Timestamp of a rating in the form YYYY-MM-DD, in the range 1998-11-01 to
2005-12-31.

NetflixID:
Integer ID of a movie as currently used in the Netflix developer API 
http://developer.netflix.com/

--------------------------------------------------------------------------------

Relevant Papers:

James Bennett and Stan Lanning. "The Netflix Prize", 2007. 
http://rexa.info/paper/4755326FDAE3929649348DC380A46D3882A98198

---------------------------------------------------------------------------------

Citation Request:


USAGE LICENSE:

Netflix cannot guarantee the correctness of the data, its suitability for any
particular purpose, or the validity of results based on the use of the data set.
The data set may be used for any research purposes under the following
conditions:

* The user may not state or imply any endorsement from Netflix.

* The user must acknowledge the use of the data set in
publications resulting from the use of the data set, and must
send us an electronic or paper copy of those publications.

* The user may not redistribute the data without separate
permission from Netflix.

* The user may not use this information for any commercial or
revenue-bearing purposes without first obtaining permission
from Netflix, and may not attempt to de-anonymize the data or
otherwise associate it with personally identifying information.

If you have any further questions or comments, please contact the Prize
administrator: prizemaster '@' netflix.com.
