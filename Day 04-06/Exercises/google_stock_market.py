"""In this file we will deal with data in a form of csv of google stock market if
   the first 10 years from 2004 and 2014"""
import csv

path = "Google Stock Market Data.csv"
file = open(path, newline='')  # Depending on the system strings will end with \n or \r
reader = csv.reader(file)
header = next(reader)  # Extract the header


