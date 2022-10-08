import math
import os
import random
import re
import sys
if __name__ == '__main__':
    a = []

    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))
    sum=int(0)
    max=int(-1000)
    for i in range(4):
        for j in range(4):
            sum=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
            if sum > max:
                max=sum
    print(max)