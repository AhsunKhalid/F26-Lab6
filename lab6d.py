# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 04/11/2026
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# TO DO 1: Create function times_ten as instructed in readme.md file. 

# TO DO 2: Run the script.
def times_ten(start_index:int, end_index:int):
    this_dictionary={}
    for i in range(start_index,end_index+1):
        this_dictionary[i]=i*10
    return this_dictionary
def main():
    my_dictionary=times_ten(2,6)
    print(my_dictionary)

if __name__=="__main__":
    main()