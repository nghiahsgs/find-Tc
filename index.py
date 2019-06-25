import numpy as np

data=np.genfromtxt("xacsuat48.dat")
temp = set(data[:, 0])
temp =list(temp)
temp.sort()


d=[]
for t in temp: d.append(np.mean(data[abs(data[:, 0] - t) < 1e-5, 1:], 0))
d=np.array(d)

import matplotlib.pyplot as plt

# plt.plot(data[:,0],data[:,1],'.')
# plt.plot(data[:,0],data[:,2],'.')
# plt.plot(data[:,0],data[:,3],'.')

plt.plot(temp,d[:,0],'-')
plt.plot(temp,d[:,1],'-')
plt.plot(temp,d[:,2],'-')

#plt.legend(['z','a','q'])
plt.show()