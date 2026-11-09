# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 04/11/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py
# TO DO 1: Copy the code from lab6a.py and paste here.
# TO DO 2: Create the function s3ors5().
# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.

def buildtheSet(divisor):
    # Complete this function
    numbers = set()
    for num in range (101):
        if num % divisor == 0:
            numbers.add(num)
    return numbers

def s3_or_s5(s3,s5):
    union_set=s3.union(s5)
    common_set=s3.intersection(s5)
    result_set=union_set.difference(common_set)
    return result_set

def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")
    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")
    Difference = s3_or_s5(s3,s5)
    print ("Numbers in s3 and s5 but not both:", Difference)

main ()