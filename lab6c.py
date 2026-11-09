# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 04/11/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

# TO DO 1: Copy the code from lab5b.py and paste here.
# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.

def buildtheSet(divisor):
    # Complete this function
    numbers = set()
    for num in range (101):
        if num % divisor == 0:
            numbers.add(num)
    return numbers

def s3_and_s5_not_s7(s3,s5,s7):
    s3ands5=s3.intersection(s5)
    result_set=s3ands5-s7
    return result_set

def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")
    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")
    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")
    three_afive_nseven = s3_and_s5_not_s7(s3,s5,s7)
    print ("Numbers in s3 and s5 but not in s7:", three_afive_nseven)

main ()