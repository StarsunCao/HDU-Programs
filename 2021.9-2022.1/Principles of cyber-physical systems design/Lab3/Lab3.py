import numpy as Np
from numpy import linalg as La
import matplotlib.pyplot as Plt

data_read = Np.genfromtxt('testLab1Var73.csv', delimiter=',')

time = data_read[:,0]
time = time[:, Np.newaxis]
current = data_read[:,1]
current = current[:, Np.newaxis]
voltage = data_read[:,2]
voltage = voltage[:, Np.newaxis]
print(voltage[10])
print(time[10])

fig, (ay1,ay2) = Plt.subplots(2, 1, sharex=True)
T_per = 0.1
ay1.plot(time[time<2*T_per],voltage[time<2*T_per])
ay1.grid()
ay1.set_xlabel('time, s')
ay1.set_ylabel('voltage, V')
ay2.plot(time[time<2*T_per],current[time<2*T_per])
ay2.grid()
ay2.set_xlabel('time, s')
ay2.set_ylabel('current, A')
Plt.show()
fig.savefig('Recieved data(part)')

X = Np.concatenate([voltage[0:len(voltage)-2],current[0:len(current)-2]], axis = 1)
Y = current[1:len(current)-1]
K = Np.dot(Np.dot(La.inv(Np.dot(X.T,X)),X.T),Y)
Td = 0.001
R = 1 / K[0] * (1 - K[1])
T = -Td / Np.log(K[1])
L = T*R
current_est = X.dot(K)
fig, ax = Plt.subplots(1, 1)
Plt.plot(time[time<T_per],current[time<T_per])
Plt.plot(time[time<T_per],current_est[time[0:len(current)-2]<T_per])
ax.grid()
ax.set_xlabel('time, s')
ax.set_ylabel('current, A')
Plt.show()
fig.savefig('Compared data(part)')
print(R)
print(L)

R_est = []
L_est = []

n = 1000
for i in range(0, n-1, 1):

     ind = (time>=T_per*i) & (time <= T_per*(i+1))
     if all(voltage[ind]) > 0:
         new_current = current[ind]
         new_current = new_current[:, Np.newaxis]
         new_voltage = voltage[ind]
         new_voltage = new_voltage[:, Np.newaxis]

         X = Np.concatenate([new_voltage[1:len(new_voltage) - 1],new_current[0:len(new_current) - 2]], axis=1)
         Y = current[1:len(new_current) - 1]
         K = Np.dot(Np.dot(La.inv(Np.dot(X.T, X)), X.T), Y)
         if K[1] > 0:
            R = 1/K[0]*(1-K[1])
            T = -Td / Np.log(K[1])
            R_est.append(R)
            L_est.append(T*R)

R_est = Np.array(R_est)
L_est = Np.array(L_est)

print('Mean value of R: ',Np.mean(R_est),' Ohm')
print('Standart deviation of R: ',Np.std(R_est))
print('Mean value of L = ',Np.mean(L_est),' Hn')
print('Standart deviation of R: ',Np.std(L_est))