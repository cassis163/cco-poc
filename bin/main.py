import regression.random_forest as rf
from time import time

start = time()
rf.run()
end = time()

print('Time elapsed: %s' % str(end - start))