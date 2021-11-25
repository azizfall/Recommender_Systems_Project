import numpy as np
import csv 
import pandas as pd 

Books_data = pd.read_csv("Books.csv").values
Ratings_data = pd.read_csv("Ratings.csv").values
Users_data = pd.read_csv("Users.csv").values 

outF = open("Book_addedinfo.txt", "r")


num_row, num_col = np.shape(Books_data)  
Book_info = []

book_limit = 49992

for i in range(book_limit):

	book_data_row = Books_data[i].tolist() 
	ISBN = book_data_row[0]
	Title = book_data_row[1]
	Author = book_data_row[2]
	Year_of_Publication = book_data_row[3]
	Publisher = book_data_row[4]

	myline = outF.readline()
	parse_str = myline.split() 
	assert int(parse_str[2]) == (i + 1), "At wrong book number"

	myline = outF.readline()
	parse_str = myline.split(" ", 1)
	description = parse_str[1]

	#missing description
	if description == "\n":
		description = "unknown"

	

	myline = outF.readline() 
	parse_str = myline.split() 
	page_count = int(parse_str[2]) 

	#missing page_count
	if page_count == -1:
		page_count = np.nan
	

	myline = outF.readline() 
	parse_str = myline.split(" ", 1)
	genre = str(parse_str[1]) 

	#missing genre
	if genre == "\n":
		genre = "unknown"
	

	myline = outF.readline() 
	parse_str = myline.split() 
	avg_rating = float(parse_str[2])

	#missing avg_rating
	if avg_rating == -1:
		avg_rating =  np.nan


	myline = outF.readline() 
	parse_str = myline.split() 
	rating_count = int(parse_str[2])

	#missing rating_count
	if rating_count == -1:
		rating_count =  np.nan

	#ignore country accessed since they 
	#are all from the US
	myline = outF.readline() 

	#ignore empty line
	myline = outF.readline() 

	book_data_row.append(description)
	book_data_row.append(str(page_count) )
	book_data_row.append(genre)
	book_data_row.append(str(avg_rating))
	book_data_row.append(str(rating_count))
	Book_info.append(book_data_row) 



csv_filename = "Book_Information.csv"
fields = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Image-URL-S",\
         "Image-URL-M", "Image-URL-L", "Description", "Page Count", "Genre", "Average Rating", "Rating Count"]

print("IN THIS PART OF THE CODE")

with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(Book_info) 

















