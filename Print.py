import sys
if __name__ == '__main__':
    try:
        n = int(input())
        numbers = []
        for x in range(n):
            if x !=0:
                numbers.append(x)
            if x == n-1:
                numbers.append(x+1)
            #sys.stdout.write(x)
        print(*numbers,sep="",end="",file=sys.stdout)
    except ValueError:
        print("Given input is not a number")