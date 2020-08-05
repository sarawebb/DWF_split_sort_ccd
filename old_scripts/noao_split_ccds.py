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

input_path = '/fred/oz100/pipes/DWF_PIPE/CTIO_PUSH/'

#output_path = '/mnt/dwf/archive_NOAO_data/data_outputs/'

thresh = np.arange(1, 2.5, 0.5)
ext = np.arange(1,62, 1)

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
            ccd_num = head['CCDNUM']
            print('ccd_num: '+ str(ccd_num))
            print('ext: '+ str(i))
            '''    
            image_filenam = (str(os.path.splitext(filename)[0]))
            fit_files_path = output_path + year + '/'+ month+'/'+ field +'/'+ 'g_band/'+image_type+'/' + image_filenam + '/ccds'
            #fit_files_path='/mnt/dwf/archive_NOAO_data/testfolder/swap/singles/'
            if not os.path.exists(fit_files_path):
                os.makedirs(fit_files_path, 0o755)
            else: 
                pass 
        	
            data = hdulist[i].data 
            hdu = fits.PrimaryHDU(data, header=hdulist[i].header)
            hdu.writeto(fit_files_path + '/' + image_filenam + '._ext_' + str(i) + '.fits', clobber=True)
            print('Ext ' + str(i) + ' saved')
            hdulist.close()
            
            
    '''
