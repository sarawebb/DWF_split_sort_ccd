#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH -n 26
#SBATCH -c 1 # 1 core per task
#SBATCH --output=run_2015_2016_.out
#SBATCH --error=run_2015_2016_.err

#SBATCH --partition=skylake
#SBATCH --time=48:00:00

srun -N 1 -n 1 python split_2015_01_4hr_gband_singles.py 0 &    
srun -N 1 -n 1 python split_2015_01_CDF-S_gband_singles.py 1 &    
srun -N 1 -n 1 python split_2015_01_FRB090625_gband_singles.py 2 &    
srun -N 1 -n 1 python split_2015_01_FRB131104_gband_singles.py 3 &    
srun -N 1 -n 1 python split_2015_01_Prime_gband_singles.py 4 &    
srun -N 1 -n 1 python split_2015_02_Prime_gband_singles.py 5 &    
srun -N 1 -n 1 python split_2015_12_3hr_gband_singles.py 6 &    
srun -N 1 -n 1 python split_2015_12_4hr_gband_singles.py 7 &    
srun -N 1 -n 1 python split_2015_12_CDF-S_gband_singles.py 8 &    
srun -N 1 -n 1 python split_2015_12_CDFS_gband_singles.py 9 &    
srun -N 1 -n 1 python split_2015_12_DWF_3hr_slew_gband_singles.py 10 &    
srun -N 1 -n 1 python split_2015_12_DWF_4hr_slew_gband_singles.py 11 &	 
srun -N 1 -n 1 python split_2015_12_DWF_FRB010714_slew_gband_singles.py 12 &    
srun -N 1 -n 1 python split_2015_12_FRB010724_gband_singles.py 13 & 
srun -N 1 -n 1 python split_2015_12_FRB151230_gband_singles.py 14 & 
srun -N 1 -n 1 python split_2016_01_FRB151230_gband_singles.py 15 & 
srun -N 1 -n 1 python split_2016_07_14hr_gband_singles.py 16 & 
srun -N 1 -n 1 python split_2016_07_dusty12_gband_singles.py 17 & 
srun -N 1 -n 1 python split_2016_07_DWF_14hr_slew_gband_singles.py 18 & 
srun -N 1 -n 1 python split_2016_07_DWF_dusty12_slew_gband_singles.py 19 & 
srun -N 1 -n 1 python split_2016_07_DWF_ngc6101_slew_gband_singles.py 20 & 
srun -N 1 -n 1 python split_2016_07_DWF_ngc6744_slew_gband_singles.py 21 & 
srun -N 1 -n 1 python split_2016_07_DWF_NSF2_slew_gband_singles.py 22 & 
srun -N 1 -n 1 python split_2016_07_ngc6101_gband_singles.py 23 & 
srun -N 1 -n 1 python split_2016_07_ngc6744_gband_singles.py 24 & 
srun -N 1 -n 1 python split_2016_07_NSF2_gband_singles.py 25 & 
wait 
