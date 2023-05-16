"""In this file we will deal with data in a form of csv of google stock market if
   the first 10 years from 2004 and 2014"""
import csv
import datetime

path = "Google Stock Market Data.csv"
file = open(path, newline='')  # Depending on the system strings will end with \n or \r
reader = csv.reader(file)
header = next(reader)  # Extract the header

# header = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
# data types :['8/18/2014', '576.11258', '584.512631', '576.002598', '582.162619', '1284100', '582.162619']
data = []
for line in reader:
    date = datetime.datetime.strptime(line[0], '%m/%d/%Y')
    opn = float(line[1])
    high = float(line[2])
    low = float(line[3])
    close = float(line[4])
    value = int(line[5])
    adj_close = float(line[6])
    data.append([date, opn, high, low, close, value, adj_close])
