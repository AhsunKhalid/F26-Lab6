# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 04/11/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

# TO DO 1: Create function add_movie(). 
# TO DO 2: Call the function 4 times.
# TO DO 3: Print the database as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.

def add_movie(database,name,director,year,runtime):
    movie={"Name":name, "Director":director, "Year":year, "Runtime":runtime}
    database.append(movie)
def main():
    movie_database=[]
    add_movie(movie_database,"Titanic","James Cameron",1997,195)
    add_movie(movie_database, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(movie_database,"Alien", "Ridley Scott", 1979, 117)
    add_movie(movie_database,"The Lord of the Rings", "Peter Jackson", 2001, 178)
    for movie in movie_database:
        print(movie)
main()        