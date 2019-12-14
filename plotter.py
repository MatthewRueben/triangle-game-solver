from pylab import *
from copy import deepcopy

def makeplot():
    pegs_in_each_row = (5,4,3,2,1)
    pos_current = [0,0]
    pos_start_of_row = deepcopy(pos_current)
    pos_pegs = []
    for pegs_in_this_row in pegs_in_each_row:
        pos_current = deepcopy(pos_start_of_row)
        for peg_in_row_current in range(pegs_in_this_row):
            pos_pegs.append(deepcopy(pos_current))
            pos_current[0] += 1.0   # move one space to the right
        
        # Moving up a row
        pos_start_of_row[1] += 1.0
        pos_start_of_row[0] += 0.5
        
    x = [x_i for x_i, y_i in pos_pegs]
    y = [y_i for x_i, y_i in pos_pegs]
    plot(x, y, '.')
    show()

