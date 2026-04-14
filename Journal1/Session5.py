import numpy as np
from astropy.table import Table

x = np.linspace(0, 2*np.pi, 1000)
sinx = np.sin(x)

def main():
    t1 = Table()
    t1['sin(x)'] = sinx
    t1['x'] = x
    t1.pprint_all()

if __name__ == "__main__": main()

