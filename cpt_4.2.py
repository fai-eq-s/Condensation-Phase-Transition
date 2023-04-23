# SIGMA SQUARE VS RHO FOR L=1

# IMPORTING LIBRARIES
import random
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
np.set_printoptions(threshold=sys.maxsize)

# INITIATING TIME
start = time.time()

# DEFINING PLOT FUNCTION
def plotf(σModel, ρs, R, σAnalytic):
	plt.title("'σ²' VS ρ for R = {}".format(R), fontsize = 15)
	plt.xlabel("Rho (ρ = M/L)", fontname = "Avenir Next", fontsize = 15)
	plt.ylabel("σ²(ρ)", fontname = "Avenir Next", fontsize = 15)
	plt.scatter(ρs, σModel, s=10)
	plt.plot(ρs, σModel, label ='σ² for R = {}'.format(R), linewidth=1)
	plt.scatter(ρs, σAnalytic, s=10)
	plt.plot(ρs, σAnalytic, label ='σ²')
	plt.rcParams['font.family'] = "Avenir Next"
	plt.legend()

# DEFINING CHIPPING FUNCTION
def chipping(m, i):
	x = random.random()
	if x<0.5:
		j=(i+1)%L
		m[j] = m[j]+1
	else:
		j=(i+L-1)%L
		m[j] = m[j]+1
	m[i] = m[i]-1

# DEFNINING DIFFUSING FUNCTION
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

# DEFINING MAIN FUNCTION
def mainfunc(σModel, ρs, M, σAnalytic):
	rgn = 0
	curr = M
	FM = 0
	SM = 0

	# REALISATION TIME LOOP
	for r in range(0,R):
		while curr!=0:
			curr = curr - rgn
			rgn = random.randint(0, curr)
			a = random.randint(0, L-1)
			m[a] = m[a] + rgn

	# MONTE CARLO LOOP
		for t in range(0, tf):

	# MICRO LOOP	
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

	# CALULATING FIRST MOMENT, SECOND MOMENT, SIGMA SQUARED, RHO
	FM = FM/(R*(tf-ts))
	SM = SM/(R*(tf-ts))
	σ2 = SM-(FM**2)
	r = M/L
	σModel.append(σ2)
	ρs.append(r)
	σAnalytic.append((r*(1+r)*(1+(r**2)))/(1-(2*r)-(r**2)))
	print("ρ = {}, Model σ² = {}, Analytical σ² = {} ".format(r, σ2, (r*(1+r)*(1+(r**2)))/(1-(2*r)-(r**2)) ))

# DEFINING VARIABLES
tf=8000
ts=2000
L=1000
R=1
m = [0]*L
Time = []
σModel = []
σAnalytic = []
ρs = []
M = 0

#CALLING MAIN FUNCTION FOR DIFFERENT VALUES OF RHOs
for k in range(1, 28):
	if k<8:
		M = M + 0.05*L
	elif k<17:
		M = M + 0.005*L
	else:
		M = M + 0.001*L
	mainfunc(σModel, ρs, M, σAnalytic)

# TERMINATING TIME
end = time.time()
tt = end - start
print("Total time taken to run the code is {} s".format(tt))
plotf(σModel, ρs, R, σAnalytic)
plt.show()

