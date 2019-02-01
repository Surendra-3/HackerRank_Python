#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
N = abs(N)
if N <= 100 and N >= 1:
    if  N%2 != 0:
        print("Weird")
    else:
        if N >=2 and N<=5:
            print("Not Weird")
        else:
            if N>=6 and N<=20:
                print("Weird")
            else:
                if N > 20:
                    print("Not Weird")
            

