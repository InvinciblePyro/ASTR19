import numpy as np
import sys

def cartesian_dist(x1, y1, x2, y2):
    '''
    holy shit i didnt know i could do this
    '''

    dx  = x1-x2
    dy = y1-y2
    ds = np.sqrt(dx**2 + dy**2)

    return ds

def main():
    np.random.rand()
    x1 = 5*np.random.rand(10)
    y1 = 5*np.random.rand(10)
    
    x2 = 5*np.random.rand(10)
    y2 = 5*np.random.rand(10)

    ds = cartesian_dist(x1, y1, x2, y2)

    for i in range(len(x1)):
        print(f"The points ({x1[i]}, {y1[i]}) and ({x2[i]}, {y2[i]}) have a distance of: {ds[i]}")

main()