#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH --output=run_2015_2016_.out
#SBATCH --error=run_2015_2016_.err
#SBATCH --partition=skylake
#SBATCH --time=04:00:00

python split_2015_01_4hr_gband_singles.py  

