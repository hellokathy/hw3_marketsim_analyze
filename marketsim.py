import argparse as ap
import csv
import datetime as dt
import pandas as pd

import qstkutil.qsdateutil as du
import qstkutil.DataAccess as da

#creating ArgumentParse object to receive the arguments of the input 
argparser = ap.ArgumentParser(description = "Takes an order file and outputs a values file.")
argparser.add_argument("cash", type=float)
argparser.add_argument("infile")
argparser.add_argument("outfile")
args = argparser.parse_args()

print "Starting with " + str(args.cash) + " dollars."
print "Input file: " + args.infile
print "Values file: " + args.outfile

#setting up an empty list to store our order information
orders = []

#oppening our files with the "with" command ensures that they close automatically
with open (args.infile, "rU") as infile:
    with open (args.outfile, "w") as outfile:
        #set up our reading and writing objects
        reader = csv.reader(infile, excel)
        writer = csv.writer(oufile)
        #read each row, sore the value in the orders list and write it to the values file
        for row in reader:
            orders.append([dt.date(int(row[0]), int(row[1]), int(row[2])), row[3], row[4], int(row[5])])
            #parrto what we readback to the output file
            writer.writerow(row)
#print our orders to the screen so we can make sure they read correctly
for order in orders:
    print order
#wait for user inut
foo = raw_input("\nPress Enter\n")

# get our timestamps for our trading days, prin hem to the screen
startday = min(orders)[0]
endday = max(orders)[0]
timeofday = dt.timedelta(hours=16)
timestamps = du.getNYSEdays(startday, endday, timeofday)
                          
print "\n\n", timestamps

#wait for user input
bar = raw_input("\nPress enter\n")

#get list of unique symbols
symbols = list(set([order[1] for order in orders]))
#load in data
dataobj = da.DataAccess('Yahoo')
close = dataobj.get_data(timestamps, symbols, "close")

print symbols
print "variable 'close' is ", type(close), " object class"        
        

