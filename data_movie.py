#
import json
from pprint import pprint

with open('movies.json', 'r', encoding='utf8') as f:
    data_movies = json.load(f)


print("################## How many movies are in the json files? ######################")
print(len(data_movies))# panjang data
print("\n")
#Genre
genre_list = {}
for i in data_movies:
    if len(i['genres']) == 0:
        if 'blank' in genre_list.keys():
            genre_list['blank'] = genre_list['blank'] + 1
        else:
            genre_list['blank'] = 1
    else:
        for z in i['genres']:
            if z in genre_list.keys():
                genre_list[z] = genre_list[z] + 1
            else:
                genre_list[z] = 1
genre = set(genre_list)
print("######### How many distinct genres are there? What are they? ###################")
print(len(genre))
print(genre)

list_of_years = []
for movie in data_movies:
    list_of_years.append(movie["year"])
years = set(list_of_years)
print("\n")
print("########################## Movie’s year? Earliest & Latest? ####################")
earliest = min(years)
latest = max(years)
print(" Earliest movie =  %s, \n Latest movie = %s " % (earliest, latest))
print("\n")
print("#################### How many movies in each genre? ############################")
list_of_genres1 = []
for movie in data_movies:
    list_of_genres1.extend(movie["genres"])
for q in genre:
    sum_genre = list_of_genres1.count(q)
    print("Genre =  %s, Jumlah = %d movie" % (q, sum_genre))
print("\n")
print("######################### How many movies each year? ###########################")
for list_year in years:
    sum_year = list_of_years.count(list_year)
    print("Tahun = %s, Jumlah = %d movie" % (list_year, sum_year))
print("\n")
print("################### What is the genre with most movies? #########################")
most_movie = 0
key_genre = ''
for y in genre_list.keys():
    if most_movie < genre_list[y]:
        most_movie = genre_list[y]
        key_genre = y
print("%s = %s"%(key_genre, most_movie))
print("\n")
print("################# How many cast are there? ######################################")
cast_list = {}
for j in data_movies:
    if len(j['cast']) == 0:
        if 'blank' in cast_list.keys():
            cast_list['blank'] = cast_list['blank'] + 1
        else:
            cast_list['blank'] = 1
    else:
        for v in j['cast']:
            if v in cast_list.keys():
                cast_list[v] = cast_list[v] + 1
            else:
                cast_list[v] = 1
cast = set(cast_list)
print(len(cast))
print("\n")
print("############ Who are the actor/actress played most movies over years? ############")
most_cast = 0
key_cast = ''
for u in cast_list.keys():
    if u != 'blank':
        if most_cast < cast_list[u]:
            most_cast = cast_list[u]
            key_cast = u
print("%s = %s" % (key_cast, most_cast))
