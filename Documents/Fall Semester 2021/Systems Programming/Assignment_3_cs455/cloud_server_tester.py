import multiprocessing as mp
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('--n', type = int, required = True)
parser.add_argument('-source', '--param2', required = True)

args = parser.parse_args()
fp = open(args.param2, 'r')

def iclient(u, f, d):
	os.system('python cloud_client.py -uid %s -file %s -data ./%s' %(u, f, d))

if __name__ == '__main__':
	cpus = args.n

	p1 = mp.Pool(cpus)

	for i in range(cpus):
		randuid = np.random.random(size = 5) * 100000
		p1.apply_async(iclient(randuid, args.param2, fp))
	fp.close()
	p1.close()
	p1.join()
	 

