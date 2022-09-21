"""In this challenge I have to get the 20 highest rated directors from a data set based on their
average movie IMDB ratings. """
import copy
import csv
import collections

YEAR = 2023
MINIMUM_YEAR = 2015
path = "movie_metadata.csv"
file = open(path, newline='', encoding='utf-8')
reader = csv.reader(file)
header = next(reader)
his_movie = collections.namedtuple('his_movie', ['Title', 'Year', 'Score'])


def get_important_data(the_file):
    data = []

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
    lst_by_year = []
    for director, movie in directors_dict.items():
        if directors_dict[director][0].Year > MINIMUM_YEAR:
            lst_by_year.append(directors_dict[director][0])
    return lst_by_year

def most_famous_directors(top_i):
    """Directors with how many movies he/she did"""
    count = collections.Counter()
    for director, his_movies in directors_dict.items():
        count[director] += len(his_movies)
    return count.most_common(top_i)

print(most_famous_directors(2))
def sort_movies_by_year(lst):  # Counting Sort Algorithm
    """Counting Sort Algorithm for the years"""
    # lst =elements: his_movie(Title='The Mongol King', Year=2005, Score=7.8) from  minimum_year()
    size = len(lst)
    output_lst = [0]*size  # movies lst size
    place = [0]*(YEAR - MINIMUM_YEAR)   # lst that has YEAR of elements
    for i in range(0, size):
        place[lst[i]-MINIMUM_YEAR] += 1
    count = copy.copy(place)

    for j in range(len(place)):
        place[j] += place[j-1]
    for h in range(len(place)):
        place[h] -= 1

    for b in range(len(place)-1, -1, -1):
        if b > 0:
            while place[b]-place[b-1] > 0:
                output_lst[place[b]] = b + MINIMUM_YEAR
                place[b] -= 1
        else:
            while place[b]-0 >= 0:
                output_lst[place[b]] = b + MINIMUM_YEAR
                place[b] -= 1


sort_movies_by_year([2015, 2016, 2016, 2015, 2016, 2018, 2017, 2020, 2019, 2017])


def lst_all_movies_with_the_score(j):
    lst = []
    for director, s_movie in directors_dict.items():
        if s_movie[0].Score == j:
            lst.append((director, directors_dict[director][0].Title, directors_dict[director][0].Year))
    return lst


def top_movies(num):
    sorted_lst = []
    for i in range(100, -1, -1):
        wanted_score = i/10
        the_movie_lst = lst_all_movies_with_the_score(wanted_score)
        if len(the_movie_lst) > 0:
            for j in range(len(the_movie_lst)):
                sorted_lst.append((the_movie_lst[j][1], the_movie_lst[j][2]))  # Give just the title and year
    return sorted_lst[0:num]


print(len(minimum_year()))