#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH -n 3
#SBATCH -c 1 # 1 core per task
#SBATCH --output=run_2015_2016_.out
#SBATCH --error=run_2015_2016_.err
#SBATCH --partition=skylake
#SBATCH --time=04:00:00

srun -N 1 -n 1 python split_2015_01_4hr_gband_singles.py 0 &    
srun -N 1 -n 1 python split_2015_01_CDF-S_gband_singles.py 1 &    
srun -N 1 -n 1 python split_2015_01_FRB090625_gband_singles.py 2 &    
srun -N 1 -n 1 python split_2015_01_FRB131104_gband_singles.py 3 &    

