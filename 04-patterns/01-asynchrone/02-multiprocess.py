import time
from multiprocessing import Process

processes = []


def do_stuff(i):
    print("pass %d" % i)
    time.sleep(3)


for i in range(1, 3):
    # do_stuff(i)
    process = Process(target=do_stuff, args=(i,))
    processes.append(process)

# start all processes
for process in processes:
    process.start()

# make sure that all processes have finished
for process in processes:
    process.join()

print("done.")
