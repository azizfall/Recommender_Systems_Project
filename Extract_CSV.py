import numpy as np
import requests
import json
import pandas as pd
import csv 
from requests.auth import HTTPBasicAuth
import time


Books_data = pd.read_csv("Books.csv").values
Ratings_data = pd.read_csv("Ratings.csv").values
Users_data = pd.read_csv("Users.csv").values

outF = open("Book_addedinfo.txt", "w")

#return types
#description ---> string  ["" if key does not exist] 
#page_count ---> integer  [-1 if key does not exist]
#genre ---> string        ["" if key does not exist]
#avg_rating --> float     [-1 if key does not exist]
#rating_count --> integer [ -1 if key does not exist]
#country_access ---> string ["" if key does not exist]
number_access = 0

def compute_bookinfo(query_string):
    #print(query_string)
    #print("access number is: ", number_access)
    auth = HTTPBasicAuth('apikey', "AIzaSyDJzdhQmTmITLh9FI_wvjaDxuVP70kvP7s")
    url = "https://www.googleapis.com/books/v1/volumes?q=" + query_string
    r = requests.get(url, auth=auth)
    pretty_json = json.loads(r.text)

    if not ("items" in pretty_json):
    	time.sleep(1)
    	r = requests.get(url, auth=auth)
    	pretty_json = json.loads(r.text)
    	
    	if not ("items" in pretty_json):
    		return "", -1, "", -1, -1, ""

    #process first item in the google search 
    #print(pretty_json)
    #print("\n\n\n\n\n")
    items0 = pretty_json['items'][0]
    volumeInfo = items0["volumeInfo"]
    
    description = ""
    if "description" in volumeInfo:
        description = volumeInfo["description"]
        
    page_count = -1 
    if "pageCount" in volumeInfo:
        page_count = volumeInfo["pageCount"]
    
    genre = ""
    if "categories" in volumeInfo:
        genre = volumeInfo["categories"][0]
        
    avg_rating = -1
    if "averageRating" in volumeInfo:
        avg_rating = volumeInfo["averageRating"]
        
    rating_count = -1
    if "ratingsCount" in volumeInfo:
        rating_count = volumeInfo["ratingsCount"]
        
    country_access = ""
    if "accessInfo" in items0:
        accessInfo = items0["accessInfo"]
        if "country" in accessInfo:
            country_access = accessInfo["country"]

    return (description,page_count,genre,avg_rating,rating_count,country_access)
    
    

       
num_row, num_col = np.shape(Books_data)  
Book_info = []
for i in range(num_row):
    book_data_row = Books_data[i].tolist()
    ISBN = book_data_row[0]
    Title = book_data_row[1]
    Author = book_data_row[2]
    Year_of_Publication = book_data_row[3]
    Publisher = book_data_row[4]
    query_string = Title  
    description,page_count,genre,avg_rating,rating_count,country_access = compute_bookinfo(query_string) 
    book_data_row.append(description)
    book_data_row.append(str(page_count) )
    book_data_row.append(genre)
    book_data_row.append(str(avg_rating))
    book_data_row.append(str(rating_count))
    book_data_row.append(country_access)
    number_access = number_access + 1
    
    outF.write("Book Number: " + str(number_access) + "\n")
    outF.write("Description: " + description + "\n")
    outF.write("Page Count: " + str(page_count) + "\n")
    outF.write("Genre: " + genre + "\n")
    outF.write("Avg Rating: " + str(avg_rating) + "\n")
    outF.write("Rating Count: " + str(rating_count) + "\n")
    outF.write("Country Accessed: " + country_access + "\n")
    outF.write("\n")

    
    Book_info.append(book_data_row) 
    
csv_filename = "Book_Information.csv"
fields = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Image-URL-S",\
         "Image-URL-M", "Image-URL-L", "Description", "Page Count", "Genre", "Average Rating", "Rating Count",\
         "Country Accessed"]

print("IN THIS PART OF THE CODE")

with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(Book_info) 

