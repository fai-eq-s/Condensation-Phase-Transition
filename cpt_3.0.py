# SIGMA SQUARE VS RHO

import random
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import pandas as pd

np.set_printoptions(threshold=sys.maxsize)

start = time.time()
tf=8000
ts=2000
L=100
R=1
rgn = 0
curr = 10
#c = [0]*tf
m = [0]*L
Time = []
FM = 0
SM = 0
df = pd.DataFrame({'Rho': [], 'Sigma Squared': []})
pd.append(
def chipping(m, i):
	x = random.random()
	if x<0.5:
		j=(i+1)%L
		m[j] = m[j]+1
	else:
		j=(i+L-1)%L
		m[j] = m[j]+1
	m[i] = m[i]-1

def diffuse(m, i):
	x = random.random()
	if x<0.5:
		j=(i+1)%L
		m[j] = m[j]+m[i]
		m[i]=0
	else:
		j=(i+L-1)%L
		m[j] = m[j]+m[i]
		m[i]=0



for r in range(0,R):
	while curr!=0:
		curr = curr - rgn
		rgn = random.randint(0, curr)
		a = random.randint(0, L-1)
		m[a] = m[a] + rgn

# MONTE CARLO
	for t in range(0, tf):
#		c[t] = c[t]+m[0]
# START THE MICRO LOOP	
		for tm in range(0,L):
			i=random.randint(0, L-1)
			if m[i]>0:
				prob = random.random()
				if prob < 0.5:
					# CHIPS
					chipping(m, i)	
				else:
					# DIFFUSES
					diffuse(m, i)
		if(t>ts):
			FM = FM + m[0]
			SM = SM + m[0]**2


FM = FM/(R*(tf-ts))
SM = SM/(R*(tf-ts))
print("⟨m⟩ = {}".format(FM))
print("⟨m²⟩ = {}".format(SM))
σ2 = SM-(FM**2)
print("σ² = {}".format(σ2))
end = time.time()
timetaken = end-start
print("The total time taken to run the code is {}".format(timetaken))
