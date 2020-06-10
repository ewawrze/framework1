import csv

def get_csv_data(file_name):
    #create an empty list to store the rows
    rows_list=[]

    #open the csv file in a reader mode
    open_csv=open(file_name,"r")

    #create a csv reader
    csv_reader = csv.reader(open_csv)

    #skip the header
    next(csv_reader)

    #add rows from reader to a list
    for row in csv_reader:
        rows_list.append(row)
    return rows_list