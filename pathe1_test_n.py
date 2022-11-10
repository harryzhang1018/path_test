from cProfile import label
from numpy import genfromtxt
import numpy as np
import sys
sys.path.append('/home/harry/Documents/path_test')
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg') 


cone_pos = genfromtxt('/home/harry/Documents/path_test/easy_one.csv', delimiter='')
state_v06 = genfromtxt('/home/harry/Documents/path_test/state_e1_n06.csv', delimiter=',')
state_v08 = genfromtxt('/home/harry/Documents/path_test/state_e1_n08.csv', delimiter=',')
state = genfromtxt('/home/harry/Documents/path_test/state_e1_n10.csv', delimiter=',')
state_v12 = genfromtxt('/home/harry/Documents/path_test/state_e1_n12.csv', delimiter=',')
state_v14 = genfromtxt('/home/harry/Documents/path_test/state_e1_n16.csv', delimiter=',')
state_v16 = genfromtxt('/home/harry/Documents/path_test/state_e1_n20.csv', delimiter=',')
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
plt.plot(state_x_v06,state_y_v06,label="N = 6")
#plt.plot(state_x_v08,state_y_v08,label="N = 8")
plt.plot(state_x,state_y,label="N = 10")
plt.plot(state_x_v12,state_y_v12,label="N = 12")
plt.plot(state_x_v14,state_y_v14,label="N = 16")
plt.plot(state_x_v16,state_y_v16,label="N = 20")
plt.legend(loc="upper left")
#plt.xlim([-2.5,1.5])
#plt.plot(ref_x,ref_y)
plt.show()