'''
Input Specification:
Each line will contain the name of the movie and rating, separated by ‘#’
The input will be terminated by “THE END”.

Output Specification:
Print the name and rating sum of the movie which have the highest rating sum.
If two movies have same highest rating sum, print the movie which comes first in
dictionary order .
'''

dic = {}

while True:
    line = input().strip()
    if line == "THE END":
        break

    line = line.rsplit(" # ", 1)
    movie, rating = line[0], int(line[1])
    if movie not in list(dic.keys()):
        dic[movie] = rating
    else:
        dic[movie] += rating

val = max(list(dic.values()))
probableMovies = [key for key, value in dic.items() if value == val]
print(min(probableMovies))