# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 04/11/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.
# TO DO 2: Create function find_movie().
# TO DO 3: Call the function as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.

def add_movie(database,name,director,year,runtime):
    movie={"name":name, "director":director, "year":year, "runtime":runtime}
    database.append(movie)

def find_movie(database,search_word):
    results=[]
    for movie in database:
        if search_word.lower() in movie ["name"].lower():
                results.append(movie)
    return(results)
    
def main():
    movie_database=[]
    add_movie(movie_database,"Titanic","James Cameron",1997,195)
    add_movie(movie_database, "Avatar", "James Cameron", 2009, 162)
    add_movie(movie_database,"Avatar", "James Cameron", 2009, 162)
    add_movie(movie_database,"Avatar", "James Cameron", 2009, 162)
    print(find_movie(movie_database,"titanic"))
main()        