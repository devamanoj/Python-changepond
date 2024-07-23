movies = {'vel','kanguva','24','unnai ninathu','ayan','shree'}
add_movies = {'mattran','24','ayan','friends'}
#union() -does not repeat element
union = movies.union(add_movies)
print('union:',union)

union = movies |add_movies
print('union using operators:',union)

#intersection and & operator
intersection = movies.intersection(add_movies)
print('intersection:',intersection)

#difference and - operator
difference = movies.difference(add_movies)
print('difference:',difference)

difference = add_movies.difference(movies)
print('difference:',difference)

#symmetric differencer
symmetric = movies.symmetric_difference(add_movies)
print('symmetric',symmetric)
