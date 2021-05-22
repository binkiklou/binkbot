# This script takes in all the CSV and turns them into one big txt

import pandas
import os

directory = '../Data/'
text = '' # <-- Output

# For each file in data folder

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        print(directory + filename)
        f = open(directory + filename)
        lines = f.read()

        #AuthorID,Author,Date,Content,Attachments,Reactions
        column_names = ["AuthorID","Author","Date","Content","Attachments","Reactions"]
        df = pandas.read_csv(directory + filename, names=column_names)
        w = df.Content.to_list() # I love good names
        for msg in w:
            if type(msg) == str:
                text += msg + "\n"
        continue
    else:
        continue

f = open("../data.txt","w")
f.write(text)
f.close()