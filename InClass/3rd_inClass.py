from astropy.table import Table 
import numpy as np

def load_dataset(path_to_data, format_data):
    Gaia_table = Table.read(path_to_data, format=format_data)    
    parallax = Gaia_table["parallax"]
    parallax_arc = parallax / 1000
    g_app_mag = Gaia_table['phot_g_mean_mag']
    return parallax_arc, g_app_mag

def get_dist(p_angle): return (1/p_angle)

def get_absolute_mag(D, app_mag): return (app_mag - 5  * np.log10(D/10))

def main():
    parallax_arc, g_app_mag = load_dataset("Gaia_1kpc.fits", "fits")
    dist = get_dist(parallax_arc)
    abs_mag = get_absolute_mag(dist, g_app_mag)
    print(np.array(abs_mag))

if __name__ == '__main__':
    main()