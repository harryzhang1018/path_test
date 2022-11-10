from cProfile import label
from numpy import genfromtxt
import numpy as np
import sys
sys.path.append('/home/harry/Documents/path_test')
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg') 


cone_pos = genfromtxt('/home/harry/Documents/path_test/easy_one.csv', delimiter='')
state_l04 = genfromtxt('/home/harry/Documents/path_test/state_e1_l04.csv', delimiter=',')
state_l06 = genfromtxt('/home/harry/Documents/path_test/state_e1_l06.csv', delimiter=',')
state_l08 = genfromtxt('/home/harry/Documents/path_test/state_e1_l08.csv', delimiter=',')
state_l10 = genfromtxt('/home/harry/Documents/path_test/state_e1_l10.csv', delimiter=',')
state_l12 = genfromtxt('/home/harry/Documents/path_test/state_e1_l12.csv', delimiter=',')
state_l14 = genfromtxt('/home/harry/Documents/path_test/state_e1_l14.csv', delimiter=',')
# cone_r_x = data[:,0]
# cone_r_y = data[:,1]
cone_l_x = cone_pos[:,2]
cone_l_y = cone_pos[:,3]
state_x_l04 = state_l04[:,0]
state_y_l04 =state_l04[:,1]
state_x_l06 = state_l06[:,0]
state_y_l06 =state_l06[:,1]
state_x_l08 = state_l08[:,0]
state_y_l08 =state_l08[:,1]
state_x_l10 = state_l10[:,0]
state_y_l10 =state_l10[:,1]
state_x_l12 = state_l12[:,0]
state_y_l12 =state_l12[:,1]
state_x_l14 = state_l14[:,0]
state_y_l14 =state_l14[:,1]
# ref_x = state[400:-1,2]+state_x -0.6
# ref_y = state[400:-1,3]+state_y + 0.2
plt.plot(cone_l_x,cone_l_y,'*',label="cone position")
plt.plot(state_x_l04,state_y_l04,label="la=0.4 m")
plt.plot(state_x_l06,state_y_l06,label="la=0.6 m")
plt.plot(state_x_l08,state_y_l08,label="la=0.8 m")
plt.plot(state_x_l10,state_y_l10,label="la=1.0 m")
plt.plot(state_x_l12,state_y_l12,label="la=1.2 m")
plt.plot(state_x_l14,state_y_l14,label="la=1.4 m")
plt.legend(loc="upper left")
#plt.xlim([-2.5,1.5])
#plt.plot(ref_x,ref_y)
plt.show()