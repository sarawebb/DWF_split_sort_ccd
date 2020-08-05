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

input_path = '/mnt/dwf/archive_NOAO_data/data/2016/01/FRB151230/g_band/single'

output_path = '/mnt/dwf/archive_NOAO_data/data_outputs/'

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
            try: 
                    mag_zpt = head['MAGZPT']
            except:
                    mag_zpt = 25
                    
            
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
            
            #for j in thresh: 
             #   os.system('sex ' + input_path + '/' + image_filenam +'_pos_'+ str(i)+'_.fits'+' -c default_params.sex -CATALOG_NAME ' + output_path + '/' + filename  + '_'+ str(i) + '_' +  str(j) +'_pos_SE.cat -DETECT_THRESH ' + str(j) +' -MAG_ZEROPOINT ' + str(mag_zpt))
       
    
