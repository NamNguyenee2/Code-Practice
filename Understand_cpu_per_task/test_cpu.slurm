#!/bin/bash

# For more information regarding SLURM sbatch options
# and how to set the properties for your job, please
# refer to the SLURM documentation:
#   https://slurm.schedmd.com/pdfs/summary.pdf
#   https://slurm.schedmd.com/documentation.html

#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=0:02:00
#SBATCH --output=test_cpu.out

# The anaconda module provides Python
module load anaconda/anaconda-2024.10

# Activate one of the pre-made ARCC environments (or
# your own environment) on top of the base environment.
conda activate base
source ~/testenv/bin/activate


# Run a Python script
python3 test_cpus.py

deactivate
