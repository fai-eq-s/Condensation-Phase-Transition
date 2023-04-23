import random
import matplotlib.pyplot as plt

t=0
tm=0
tf=300
ts=30
L=10
N=1
R=1
count = [0]*L
c1 = [0]*tf
c2 = [0]*tf
c3 = [0]*tf
c4 = [0]*tf
c5 = [0]*tf
c6 = [0]*tf
c7 = [0]*tf
c8 = [0]*tf
c9 = [0]*tf
c10 = [0]*tf
m = [None]*L
p1 = [0]*L
N1 = 0
p=0.5
P1 = []
P2 = []
P3 = []
Trials = [] 
j=0

M = 0

print(m)

def chip(*args):
	x=random.random()
	if x<p:
		j=(i+1)%L
	else:
		j=(L+i-1)%L
	m[j]=m[j]+1;
	m[i]=m[i]-1;

def diff(*args):
	x=random.random()
	if x<p:
		j=(i+1)%L
	else:
		j=(L+i-1)%L
	m[j]=m[j]+m[i];
	m[i]=0;
for M in range(0,1000):
	for i in range(0,L):
		no = (int)(M*random.random())
		m[i] = no
		M = M-no
	for t in range(0, tf):
		for tm in range(0,L):
			i=(int)(L*random.random())
			trans = random.random()
			if trans<0.5:
				if m[i]>1:
					chip(m, i, j, p)
			else:
				if m[i]>0:
					diff(m, i, j, p)
		for k in range(0,L):
			count[k]=count[k]+m[k];



for i in range(0,L):
	N1=N1+m[i];
	p1[i]=(count[i]*1.0)/(M*(tf)*1.0);
	print(p1[i], " " );

for t in range(0,tf):
	c_1=(c1[t]*1.0)/(M*1.0)
	P1.append(c_1)
	c_2=(c2[t]*1.0)/(M*1.0)
	P2.append(c_2)
	c_3=(c3[t]*1.0)/(M*1.0)
	P3.append(c_3)
	Trials.append(t)

print("Final particle=%d\n",N1)

plt.title("Time evolution of probability of a configuration in case Non-Equilibrium System", fontsize = 20)

plt.xlabel("time (t)", fontsize = 20)
plt.ylabel("Probability", fontsize = 20)


plt.scatter(Trials, P1, color = "red", s=20)
plt.plot(Trials, P1, label ='P(0, t)', color = "red", linewidth=1)

plt.scatter(Trials, P2, color = "green", s=20)
plt.plot(Trials, P2, label ='P(1, t)', color = "green", linewidth=1)

plt.scatter(Trials, P3, color = "blue", s=20)
plt.plot(Trials, P3, label ='P(2, t)', color = "blue", linewidth=1)

#font = {'family' : 'normal', 'size'   : 20}


 


#plt.rc('font', **font)
plt.axhline(y=0.33, label='0.333', color="black")
plt.margins(x=0)
plt.margins(y=0)
plt.legend()
plt.show()