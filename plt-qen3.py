# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math as mt
import glob
from matplotlib.ticker import FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.cm as cmx
import matplotlib

matplotlib.rcParams.update({'font.size': 15})

files = glob.glob("/mnt/point/shape/qen3/tabla.txt")

for i in files:
    #open and save data
    AG, QN, RS, MD, ME, SE = np.loadtxt(i, unpack=True, usecols=(0,1,2,3,4,5))

    W = QN

    fig, ax = plt.subplots()
    datamin=min(W)
    datamax=max(W)
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(10,-9)
    col = ax.scatter(RS, AG, MD,c=W, s=SE*1500, vmin=datamin, vmax=datamax, marker='x', cmap=cm.winter_r)

    ax.set_xlabel( 'Resolution')
    ax.set_ylabel( 'Inclination' )
    ax.set_zlabel( 'Mean Distance, AD: '"{0:.4f}".format(np.mean(MD))+' kpc' )
    ax.set_zlim(0.8, 1.1)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 90)
    cbar = plt.colorbar(col)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel('# of vectors', rotation=270)
    plt.title('QEN3 - Resolution & Inclination & Mean Distance & # of vectors & Standard Error')



    v1 = plt.scatter([],[],s=min(SE)*1500, marker='x',color='#555555')
    v2 = plt.scatter([],[],s=np.mean(SE)*1500, marker='x',color='#555555')
    v3 = plt.scatter([],[],s=0.1945*1500, marker='x',color='#555555') #qen3

    plt.legend((v1,v2,v3),
       ("{0:.2f}".format(min(SE)*100)+'%', "{0:.2f}".format(np.mean(SE)*100)+'%', "{0:.2f}".format(0.1945*100)+'%'),
       scatterpoints=1,
       loc='lower left',
       ncol=1,
           title = 'Standard Error',
               shadow = True)

# ax.get_legend().get_title().set_fontsize('10')

plt.show()
