import random
import matplotlib.pyplot as plt
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

tf=300
L=10
fms = 0

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

def plotf(Time, M, fms, R):
	plt.title("Variation of mass respect to time for R = {}".format(R), fontsize = 10)
	plt.xlabel("time (t)", fontname = "Avenir Next", fontsize = 10)
	plt.ylabel("Mass at site one", fontname = "Avenir Next", fontsize = 10)
	plt.scatter(Time, M, s=10)

	plt.plot(Time, M, label ='P(0, t) for R = {}'.format(R),	 linewidth=1)
	plt.rcParams['font.family'] = "Avenir Next"
	plt.legend()

def mainfunc(curr, rgn, R):	
	for r in range(0,R):
		while curr!=0:
			curr = curr - rgn
			rgn = random.randint(0, curr)
			a = random.randint(0, L-1)
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

	print(c)

	sum = 0
	for time in range(0, tf):
		M.append(c[time]/R)
		Time.append(time)
		sum = sum + M[time]
	fms = sum/tf

	sum2 = 0
	for time in range(0, tf):
		sum2 = sum2 + (M[time])*(M[time])

	sms = sum2/tf
	variance = sms-(fms**2)
	print(M)
	print()
	print("The first moment is {}".format(fms))
	print("The second moment is {}".format(sms))
	print("The variance σ² = ⟨m²⟩ - ⟨m⟩² is {}".format(variance))
	plotf(Time, M, fms, R)

flag = True
R = 1


for k in range(0, 3):

	c = [0]*tf
	m = [0]*L
	Time = []

	M = []
	R = R*10

	
	mainfunc(30, 0, R)
plt.margins(x=0)
plt.margins(y=0)
plt.axhline(y=fms, label='Average Value', color="black")
plt.show()