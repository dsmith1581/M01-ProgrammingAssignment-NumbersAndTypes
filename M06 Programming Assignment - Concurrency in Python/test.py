import multiprocessing
import time
import random


# Waits a random number of seconds between 0-1 before printing the current time
def wait_worker():
    time.sleep(random.random())
    
    print(time.ctime())

def main():
    processes = []

    # Run the processes
    for i in range(3):
        process = multiprocessing.Process(target=wait_worker)
        processes.append(process)
        process.start()

    # Wait for them to all finish
    for p in processes:
        process.join()

if __name__ == "__main__":
    main()
