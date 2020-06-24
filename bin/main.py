import regression.random_forest as rf
import record.register as rs

from time import time

def iterate():
    start = time()
    rf.run()
    end = time()

    time_elapsed = end - start

    rs.register(time_elapsed)

    print('Time elapsed: %s' % str(time_elapsed))

for i in range(10):
    iterate()