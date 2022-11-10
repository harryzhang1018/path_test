from cProfile import label
from numpy import genfromtxt
import numpy as np
import sys
sys.path.append('/home/harry/Documents/path_test')
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg') 


cone_pos = genfromtxt('/home/harry/Documents/path_test/cone_path_iros_wider.csv', delimiter='')
state_06 = genfromtxt('/home/harry/Documents/path_test/state_w1_l04.csv', delimiter=',')
state_08 = genfromtxt('/home/harry/Documents/path_test/state_w1_l05.csv', delimiter=',')
state_10 = genfromtxt('/home/harry/Documents/path_test/state_w1_l06.csv', delimiter=',')
state_12 = genfromtxt('/home/harry/Documents/path_test/state_w1_l07.csv', delimiter=',')
state_14 = genfromtxt('/home/harry/Documents/path_test/state_w1_l08.csv', delimiter=',')
state_16 = genfromtxt('/home/harry/Documents/path_test/state_w1_v08.csv', delimiter=',')
# cone_r_x = data[:,0]
# cone_r_y = data[:,1]
cone_l_x = cone_pos[:,2]
cone_l_y = cone_pos[:,3]
state_x_06 = state_06[:,0]
state_y_06 =state_06[:,1]
state_x_08 = state_08[:,0]
state_y_08 =state_08[:,1]
state_x_10 = state_10[:,0]
state_y_10 =state_10[:,1]
state_x_12 = state_12[:,0]
state_y_12 =state_12[:,1]
state_x_14 = state_14[:,0]
state_y_14 =state_14[:,1]
state_x_16 = state_16[:,0]
state_y_16 =state_16[:,1]
# ref_x = state[400:-1,2]+state_x -0.6
# ref_y = state[400:-1,3]+state_y + 0.2
plt.plot(cone_l_x,cone_l_y,'*',label="cone position")
plt.plot(state_x_06,state_y_06,label="la = 0.4 ")
plt.plot(state_x_08,state_y_08,label="la = 0.5 ")
plt.plot(state_x_10,state_y_10,label="la = 0.6 ")
plt.plot(state_x_12,state_y_12,label="la = 0.7 ")
plt.plot(state_x_14,state_y_14,label="la = 0,8 ")
plt.plot(state_x_16,state_y_16,label="la = 1.0 ")
plt.legend(loc="upper left")
#plt.xlim([-2.5,1.5])
#plt.plot(ref_x,ref_y)
plt.show()