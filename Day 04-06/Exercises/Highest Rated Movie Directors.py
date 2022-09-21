"""In this challenge I have to get the 20 highest rated directors from a data set based on their
average movie IMDB ratings. """

import copy
import csv
import collections

YEAR = 2023
MINIMUM_YEAR = 1960
path = "movie_metadata.csv"
file = open(path, newline='', encoding='utf-8')
reader = csv.reader(file)
header = next(reader)
his_movie = collections.namedtuple('his_movie', ['Title', 'Year', 'Score'])


def get_important_data(the_file):
    """This function reads the file line by line and give us a dictionary which contains the directors with
    their works"""
    directors = collections.defaultdict(list)
    for line in the_file:
        try:
            director_name = line[1]  # Director name
            movie_title = line[11].replace('\xa0', '')  # Movie title
            title_year = int(line[23])  # Title year
            imdb_score = float(line[25])  # Imdb score
        except ValueError:
            continue
        director_movies = his_movie(movie_title, title_year, imdb_score)
        directors[director_name].append(director_movies)
    return directors


directors_dict = get_important_data(reader)


def minimum_year():
    """This function takes the dictionary as an input and give us all of the movies that have been made
    since the MINIMUM YEAR global variable"""
    lst_by_year = []
    for director, movie in directors_dict.items():
        if directors_dict[director][0].Year > MINIMUM_YEAR:
            lst_by_year.append(directors_dict[director][0])
    return lst_by_year

def most_famous_directors(top_i):
    """This function take the dictionary as an input and return the most common i directors
    with how many movies he/she did"""
    count = collections.Counter()
    for director, his_movies in directors_dict.items():
        count[director] += len(his_movies)
    return count.most_common(top_i)


def sort_movies_by_year(lst):  # Counting Sort Algorithm
    """Counting Sort Algorithm for the years, This Function takes the list that we made
    in the minimum_year() function and returns a sorted list by years, with the movie title and year
    and score"""
    # lst =elements: his_movie(Title='The Mongol King', Year=2005, Score=7.8) from  minimum_year()
    size = len(lst)
    output_lst = [0]*size  # movies lst size
    place = [0]*(YEAR - MINIMUM_YEAR)   # lst that has YEAR of elements
    for i in range(0, size):
        place[lst[i][1]-MINIMUM_YEAR] += 1
    count = copy.copy(place)

    for j in range(len(place)):
        place[j] += place[j-1]
    for h in range(len(place)):
        place[h] -= 1

    for b in range(len(place)-1, -1, -1):
        if b > 0:
            while place[b]-place[b-1] > 0:
                output_lst[place[b]] = (lst[place[b]][0], b + MINIMUM_YEAR, lst[place[b]][2])
                place[b] -= 1
        else:
            while place[b]-0 >= 0:
                output_lst[place[b]] = (lst[place[b]][0], b + MINIMUM_YEAR, lst[place[b]][2])
                place[b] -= 1
    return output_lst


def lst_all_movies_with_the_score(j):
    """This function takes a float between 0.0 and 10.0 and returns the movies with the same
    score in a list with the director name and the movie's title and year"""
    lst = []
    for director, s_movie in directors_dict.items():
        if s_movie[0].Score == j:
            lst.append((director, directors_dict[director][0].Title, directors_dict[director][0].Year))
    return lst


def top_movies(num):
    """this function takes integer as an N input and returns the top N movies from the dictionary"""
    sorted_lst = []
    for i in range(100, -1, -1):
        wanted_score = i/10
        the_movie_lst = lst_all_movies_with_the_score(wanted_score)
        if len(the_movie_lst) > 0:
            for j in range(len(the_movie_lst)):
                sorted_lst.append((the_movie_lst[j][1], the_movie_lst[j][2]))  # Give just the title and year
    return sorted_lst[0:num]


print(top_movies(10))