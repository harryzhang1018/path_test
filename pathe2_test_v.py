from cProfile import label
from numpy import genfromtxt
import numpy as np
import sys
sys.path.append('/home/harry/Documents/path_test')
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg') 


cone_pos = genfromtxt('/home/harry/Documents/path_test/easy_two.csv', delimiter='')
state_v06 = genfromtxt('/home/harry/Documents/path_test/state_e2_v06.csv', delimiter=',')
state_v08 = genfromtxt('/home/harry/Documents/path_test/state_e2_v08.csv', delimiter=',')
state = genfromtxt('/home/harry/Documents/path_test/state_e2_v10.csv', delimiter=',')
state_v12 = genfromtxt('/home/harry/Documents/path_test/state_e2_v12.csv', delimiter=',')
state_v14 = genfromtxt('/home/harry/Documents/path_test/state_e2_v14.csv', delimiter=',')
state_v16 = genfromtxt('/home/harry/Documents/path_test/state_e2_v16.csv', delimiter=',')
# cone_r_x = data[:,0]
# cone_r_y = data[:,1]
cone_l_x = cone_pos[:,2]
cone_l_y = cone_pos[:,3]
state_x_v06 = state_v06[:,0]
state_y_v06 =state_v06[:,1]
state_x_v08 = state_v08[:,0]
state_y_v08 =state_v08[:,1]
state_x = state[:,0]
state_y =state[:,1]
state_x_v12 = state_v12[:,0]
state_y_v12 =state_v12[:,1]
state_x_v14 = state_v14[:,0]
state_y_v14 =state_v14[:,1]
state_x_v16 = state_v16[:,0]
state_y_v16 =state_v16[:,1]
# ref_x = state[400:-1,2]+state_x -0.6
# ref_y = state[400:-1,3]+state_y + 0.2
plt.plot(cone_l_x,cone_l_y,'*',label="cone position")
plt.plot(state_x_v06,state_y_v06,label="v = 0.6 m/s")
plt.plot(state_x_v08,state_y_v08,label="v = 0.8 m/s")
plt.plot(state_x,state_y,label="v = 1.0 m/s")
plt.plot(state_x_v12,state_y_v12,label="v = 1.2 m/s")
plt.plot(state_x_v14,state_y_v14,label="v = 1.4 m/s")
plt.plot(state_x_v16,state_y_v16,label="v = 1.6 m/s")
plt.legend(loc="upper left")
#plt.xlim([-2.5,1.5])
#plt.plot(ref_x,ref_y)
plt.show()