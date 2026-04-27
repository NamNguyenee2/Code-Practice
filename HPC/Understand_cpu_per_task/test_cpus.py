import os 
import numpy as np
import multiprocessing
from multiprocessing import Pool
import time


def simulate(initial):
    time.sleep(0.1)
    return f"Data for angle {initial} generated."


if __name__ == '__main__':
    start_time = time.time()

    slurm_cpus = int(os.environ.get("SLURM_CPUS_PER_TASK"))
    
    # slurm_cpus = multiprocessing.cpu_count()-5 # use from my local computer
    print(f"Starting dataset generation using {slurm_cpus} CPUs ...")

    angles = np.linspace(-np.pi, np.pi, 500)

    with Pool(processes=slurm_cpus) as pool:
        results = pool.map(simulate, angles)

    print(f"Successfully generated {len(results)} pendulum trajectories.")
    print(f"Running time: {time.time() - start_time}s")