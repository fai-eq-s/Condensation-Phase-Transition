import random
import matplotlib.pyplot as plt
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

tf=10000
L=100
R=10000
rgn = 0
curr = 10
c = [0]*tf
m = [0]*L
Time = []
FM = [0]*tf
SM = [0]*tf
σ2 = [0]*tf

def plotf(Time, σ2, R):
	plt.title("Variation of sigma squared σ² = ⟨m²⟩ - ⟨m⟩² with respect to time for R = {}".format(R), fontsize = 15)
	plt.xlabel("time (t)", fontname = "Avenir Next", fontsize = 15)
	plt.ylabel("σ²(t)", fontname = "Avenir Next", fontsize = 15)
	
	plt.plot(Time, σ2, label ='σ² for R = {}'.format(R),	 linewidth=1)
	plt.rcParams['font.family'] = "Avenir Next"
	plt.legend()


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
		a = random.randint(0, L)
		m[a] = m[a] + rgn

# MONTE CARLO
	for t in range(0, tf):
			
		if m[0]>0:
			c[t] = c[t]+m[0]
# START THE MICRO LOOP	
		for tm in range(0,L):
			i=(int)(L*random.random())
			if m[i]>0:
				prob = random.random()
				if prob < 0.5:
					# CHIPS
					chipping(m, i)	
				else:
					# DIFFUSES
					diffuse(m, i)
#print(c)
FM[0] = c[0]/R
SM[0] = (c[0]**2)/(R**2)
σ2[0] = SM[0] - (FM[0]*FM[0])
for t in range(0, tf):
	Time.append(t)
	if t>0:
		FM[t] = ((t-1)*FM[t-1]+(c[t]/R))/t
		SM[t] = ((t-1)*SM[t-1]+((c[t]**2)/(R**2)))/t
		σ2[t] = SM[t] - (FM[t]*FM[t])
print(FM)
print(SM)
print(σ2)

plotf(Time, σ2, R)
plt.show()
