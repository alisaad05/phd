# -*- coding: utf-8 -*-

"""
Created on Tue Aug 12 17:11:52 2014

@author: ali.saad
"""

# check http://matplotlib.org/users/customizing.html
sz=20
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('axes', labelsize=sz)
rc('xtick', labelsize=sz)
rc('ytick', labelsize=sz)
rc('legend', fontsize=sz)


# IMPORT
data1 = np.genfromtxt('data_liq.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("w_ga","temperatureC") )
data2 = np.genfromtxt('data_tetra.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("w_ga","temperatureC") )
data5 = np.genfromtxt('data_tetra_solvus.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("w_ga","temperatureC") )
data3 = np.genfromtxt('data_ortho.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("w_ga","temperatureC") )
data4 = np.genfromtxt('data_eut.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("w_ga","temperatureC") )

data1.sort()
#data2.sort()
#data3.sort()
#data4.sort()
data5.sort()

x1, y1 = data1['w_ga'], data1['temperatureC']
x2, y2 = data2['w_ga'], data2['temperatureC']
x3, y3 = data3['w_ga'], data3['temperatureC']
x4, y4 = data4['w_ga'], data4['temperatureC']
x5, y5 = data5['w_ga'], data5['temperatureC']


# SETTINGS
markfreq = 10
alphaT = 0.85
width1 = 3
ms = 6
ls1 ='-'
#ls2 ='--'
c1, c2 , c3, c4= "r" , "b", "m", "g"
#m1, m2 , m3, m4= "s" , "o", "v", "d"
m1, m2 , m3, m4= "" , "", "", ""


fig, ax1 = plt.subplots()
# ax1.set_title('Indium-Gallium Phase Diagram')
ax1.set_ylabel(u'Temperature ($^\circ$C)')
ax1.set_xlabel('Composition (wt$\%$ Ga)')
ax1.set_xlim(xmax=100, xmin=0)
ax1.set_ylim(ymax=250, ymin=-100)

ax1.plot(x1,y1 , color= c1, linestyle= ls1, marker= m1, markersize=ms, linewidth=width1, alpha=alphaT, label="Liquid",
         markevery= markfreq
         )
ax1.plot(x2,y2 , color= c2, linestyle= ls1, marker= m2,  markersize=ms, linewidth=width1,    alpha=alphaT, label="Tetragonal",
         markevery= markfreq
         )
ax1.plot(x3,y3 , color= c3, linestyle= ls1, marker= m3,  markersize=ms, linewidth=width1,    alpha=alphaT, label="Orthorhombic" ,
#         markevery= markfreq
         )
ax1.plot(x4,y4 , color= c4, linestyle= ls1, marker= m4,  markersize=ms, linewidth=width1,    alpha=alphaT, label="Eutectic",
#         markevery= markfreq
         )
ax1.plot(x5,y5 , color= c2, linestyle= ls1, marker= m2,  markersize=ms, linewidth=width1,    alpha=alphaT ,
         markevery= markfreq
         )
# legend = ax1.legend(loc='best', shadow=True)
# ax1.axvline(x=0, lw=2, ls="--", color="k")


x = np.arange(0,100,1)
yl = -2.73*x+230
ax1.plot(x,yl, ls="dashed", lw=3, c="k")
# x = np.arange(0,20,1)
ys = (-2.73/0.0165)*x+230
ax1.plot(x,ys, ls="dotted",lw=3, c="k")
plt.xticks([0,25,50,75,100])

fs = 12
plt.text(55, 170,"Liquid", fontsize=20)
plt.text(10, 35,"Liquid+Tetragonal", fontsize=20)
plt.text(30, -40,"Orthorhombic+Tetragonal", fontsize=20)
# ax.annotate("Liquid", xytext=(50,200))
# ax.annotate( 'T_{liquidus}^{BCC}', fontsize=fs, xy=(4000, T1), xytext=(4000,T1-200),
			# arrowprops=dict(arrowstyle="-|>", #linestyle="dashed",
                            # color="r",
                            # patchB=None,
                            # shrinkB=0,
                            # connectionstyle="arc3",
                            # ),
			# horizontalalignment='center', 
			# verticalalignment='center',
			# )
			
			
			
			
ax1.grid(True)
plt.savefig('PhaseDiagram.png', dpi=300, bbox_inches='tight')
plt.savefig('PhaseDiagram.pdf', bbox_inches='tight')