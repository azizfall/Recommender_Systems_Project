import numpy as np
import csv 
import pandas as pd 

Book_added_info = pd.read_csv("Book_Information.csv").values
Ratings_data = pd.read_csv("Ratings.csv").values
Users_data = pd.read_csv("Users.csv").values 




ISBN_hash = {} 
User_hash = {} 


#list of ISBN values
ISBN_arr = Book_added_info.T[0]
for i in range(len(ISBN_arr)):
	ISBN_hash[ISBN_arr[i]] = 1 

New_Ratings_arr = [] 

for i in range(len(Ratings_data)):
	rating_example = Ratings_data[i].tolist()
	#CHECK ISBN
	ISBN_rating = rating_example[1]
	#CHECK USER 
	UserID = rating_example[0]
	#ISBN_rating is in hash table
	if ISBN_hash.get(ISBN_rating, 0) != 0:
		New_Ratings_arr.append(rating_example)
		User_hash[UserID] = 1
		

#make new rating csv 
csv_filename = "New_Ratings.csv"
fields = ["User-ID", "ISBN", "Book-Rating"]

with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(New_Ratings_arr) 



New_Users_arr = [] 

for i in range(len(Users_data)):
	user_example = Users_data[i].tolist()
	UserID = user_example[0] 
	#check if user is in hash table 
	if User_hash.get(UserID, 0) != 0:
		New_Users_arr.append(user_example)

csv_filename = "New_Users.csv"
fields = ["User-ID", "Location", "Age"]

with open(csv_filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(New_Users_arr) 






