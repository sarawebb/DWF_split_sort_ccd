#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH --output output.out
#SBATCH --partition=skylake
#SBATCH --time=04:00:00
#SBATCH --account=oz100

python split_2015_01_CDF-S_gband_singles.py 

