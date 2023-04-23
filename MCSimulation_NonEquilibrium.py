import random
import matplotlib.pyplot as plt

t=0
tm=0
tf=300
ts=30
L=3
N=1
R=8000
count = [0]*L
c1 = [0]*tf
c2 = [0]*tf
c3 = [0]*tf
m = [None]*L
p1 = [0]*L
N1 = 0
p=0.5
P1 = []
P2 = []
P3 = []
Trials = [] 
j=0
for r in range(0,R):
	m[0] = 1
	for i in range(1,L):
		m[i] = 0
	for t in range(0, tf):
		if(m[0]>0):
			c1[t]=c1[t]+1
		if(m[1]>0):
			c2[t]=c2[t]+1
		if(m[2]>0):
			c3[t]=c3[t]+1
		for tm in range(0,L):
			i=(int)(L*random.random())
			if m[i]>0:
				x=random.random()
				if x<p:
					j=(i+1)%L
				m[j]=m[j]+1;
				m[i]=m[i]-1;
		if t>ts:
			for k in range(0,L):
				if m[k]>0:
					count[k]=count[k]+1;
				else:
					continue;



for i in range(0,L):
	N1=N1+m[i];
	p1[i]=(count[i]*1.0)/(R*(tf-ts)*1.0);
	print(p1[i], " " );

for t in range(0,tf):
	c_1=(c1[t]*1.0)/(R*1.0)
	P1.append(c_1)
	c_2=(c2[t]*1.0)/(R*1.0)
	P2.append(c_2)
	c_3=(c3[t]*1.0)/(R*1.0)
	P3.append(c_3)
	Trials.append(t)

print("Final particle=%d\n",N1)
plt.title("Time evolution of probability of a configuration in case of Non-Equilibrium System", fontsize = 20)
plt.xlabel("time (t)", fontsize = 20)
plt.ylabel("Probability", fontsize = 20)
plt.scatter(Trials[0:42], P1[0:42], color = "red", s=20)
plt.plot(Trials[0:42], P1[0:42], label ='P(0, t)', color = "red", linewidth=1)
plt.scatter(Trials[:42], P2[:42], color = "green", s=20)
plt.plot(Trials[:42], P2[:42], label ='P(1, t)', color = "green", linewidth=1)
plt.scatter(Trials[:42], P3[:42], color = "blue", s=20)
plt.plot(Trials[:42], P3[:42], label ='P(2, t)', color = "blue", linewidth=1)
font = {'family' : 'normal', 'size'   : 20}
plt.rc('font', **font)
plt.axhline(y=0.33, label='0.333', color="black")
plt.margins(x=0)
plt.margins(y=0)
plt.legend()
plt.show()

