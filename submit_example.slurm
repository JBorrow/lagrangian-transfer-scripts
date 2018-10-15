#!/bin/bash -l

#SBATCH -J JobName
#SBATCH -N 1
#SBATCH -o LTCaesar_%j.out
#SBATCH -e LTCaesar_%j.err
#SBATCH -p PARTITION
#SBATCH -A ALLOCATION
#SBATCH --exclusive
#SBATCH -t 1:00:00

module load <python_module>

python3 setup_venv.py

source simba_env/bin/activate  # In case your home python doesn't have yaml

python3 halo_finder.py

python3 run_analysis.py

