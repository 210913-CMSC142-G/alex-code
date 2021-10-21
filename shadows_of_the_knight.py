import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
a, b, c, d = 0, h-1, 0, w-1 

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print

    if bomb_dir[0] == 'U':
        b = y0 - 1
    if bomb_dir[0] == 'D':
        a = y0 + 1
    if bomb_dir[-1] == 'R':
        c = x0 + 1
    if bomb_dir[-1] == 'L':
        d = x0 - 1

    x0 = int((c+d)/2)
    y0 = int((a+b)/2)
    print (str(x0)+' '+str(y0))
    

    
