"""In this challenge I have to get the 20 highest rated directors from a data set based on their
average movie IMDB ratings. """

import csv
import datetime

path = "movie_metadata.csv"
file = open(path, newline='', encoding='utf-8')
reader = csv.reader(file)
header = next(reader)

data = []

for line in reader:
    try:
        director_name = line[1]  # Director name
        movie_title = line[11]  # Movie title
        title_year = datetime.datetime.strptime(line[23], '%Y')  # Title year
        imdb_score = float(line[25])  # Imdb score
    except ValueError:
        continue

    data.append([director_name, movie_title, title_year, imdb_score])

print(data)