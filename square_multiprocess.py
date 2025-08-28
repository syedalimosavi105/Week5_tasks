import time
from multiprocessing import Pool, cpu_count

# adjust size for your machine; large sizes show benefit of multiprocessing
LIST_SIZE = 500_000   # try 500_000 or 1_000_000 depending on your PC

def square(x):
    return x * x

def single_process_square(data):
    return [square(x) for x in data]

def multi_process_square(data, processes=None):
    # processes=None -> use cpu_count()
    with Pool(processes=processes) as p:
        result = p.map(square, data)
    return result

if __name__ == "__main__":
    print(f"Preparing list of {LIST_SIZE} integers...")
    data = list(range(LIST_SIZE))

    # Single-process
    t0 = time.perf_counter()
    single_res = single_process_square(data)
    t1 = time.perf_counter()
    single_time = t1 - t0
    print(f"Single-process time: {single_time:.2f} seconds")

    # Multiprocess using number of CPU cores
    procs = cpu_count()
    print(f"Using multiprocessing with {procs} processes...")
    t0 = time.perf_counter()
    multi_res = multi_process_square(data, processes=procs)
    t1 = time.perf_counter()
    multi_time = t1 - t0
    print(f"Multiprocess time: {multi_time:.2f} seconds")

    # Quick sanity check (first 5 values)
    print("\nSanity check — first 5 squares (single / multi):")
    for i in range(5):
        print(single_res[i], "/", multi_res[i])

    print(f"\nSpeedup: {single_time / multi_time:.2f}x (single / multi)")
