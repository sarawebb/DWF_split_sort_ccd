"""split_ccds.py -- Input a year, month, and field for data that has been unziped and shorted, this script will split the multi extension fits into each ccd.

Usage: split_ccds [-h] [-v] [--debug] <year> <month> <field> 

Arguments:
        year (string)
                The year of the observations.
        month (string)
                The month of the observations
        field (string)
                The DWF field name, ensureing it is spelt exactly how it appears in the NOAO header.
Options:
        -h, --help                              Show this screen
        -v, --verbose                                   Show extra information [default: False]
        --debug                                 Output more for debugging [default: False]
Example:
        python split_ccds.py -v 2015 01 4hr
"""

import docopt
import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from astropy import wcs
from astropy.wcs import WCS
from astropy.io import fits
import sys
import math
import os
import glob
import sys
from sortedcontainers import SortedDict
import datetime as dt
import imageio
import os
from PIL import Image
from matplotlib.colors import LogNorm
from astropy.nddata.utils import Cutout2D
from astropy import units as u
import datetime as dt 
import glob
import shutil


def split_ccds(year,month,field, verbose=False, debugmode=False):
	input_path = '/fred/oz100/NOAO_archive/archive_NOAO_data/data/'+ year+ '/'+month+'/'+field+'/g_band/single/'
	
	output_path = '/fred/oz100/NOAO_archive/archive_NOAO_data/data_outputs/'

	thresh = np.arange(1, 2.5, 0.5)
	ext = np.arange(1,60, 1)

	for filename in os.listdir(input_path): 
		if filename.endswith('.fits'): 
			for i in ext: 
				print(filename)
				hdulist = fits.open(input_path + '/'+ filename)
				head = hdulist[0].header
				field = head['OBJECT']
				date = dt.datetime.strptime(head['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
				year = date.strftime('%Y')
				month = date.strftime('%m')
				im_type = head['PRODTYPE']
                  
				if im_type == 'image1':
					image_type = 'stacked'
				if im_type == 'image':
					image_type = 'single'
                
				image_filenam = (str(os.path.splitext(filename)[0]))
				fit_files_path = output_path + year + '/'+ month+'/'+ field +'/'+ 'g_band/'+image_type+'/' + image_filenam + '/ccds'
            #fit_files_path='/mnt/dwf/archive_NOAO_data/testfolder/swap/singles/'
				if not os.path.exists(fit_files_path):
					os.makedirs(fit_files_path, 0o755)
				else: 
					pass 
        	
				data = hdulist[i].data 
				hdu = fits.PrimaryHDU(data, header=hdulist[i].header)
				try:
					hdu.writeto(fit_files_path + '/' + image_filenam + '._ext_' + str(i) + '.fits', clobber=False)
					print('Ext ' + str(i) + ' saved')
					hdulist.close()
				except: 
					print('file ext' +str(i) +' already exsists')
	return print('DONE')

if __name__ == "__main__":
	arguments = docopt.docopt(__doc__)
	print(arguments)
	year = arguments['<year>']
	month = arguments['<month>']
	field = arguments['<field>']
	debugmode = arguments['--debug']
	verbose = arguments['--verbose']
	if debugmode:
		print(arguments)
	split_ccds(year, month, field, verbose=True, debugmode=debugmode)
