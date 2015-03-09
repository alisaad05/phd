# check http://matplotlib.org/users/customizing.html
sz=20
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('axes', labelsize=sz)
rc('xtick', labelsize=18)
rc('ytick', labelsize=sz)
rc('legend', fontsize=sz)

dataT1 = np.genfromtxt('capteurs\Capteur1.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
dataT2 = np.genfromtxt('capteurs\Capteur2.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
dataT3 = np.genfromtxt('capteurs\Capteur3.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
dataT4 = np.genfromtxt('capteurs\Capteur4.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
dataT5 = np.genfromtxt('capteurs\Capteur5.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
dataT6 = np.genfromtxt('capteurs\Capteur6.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
dataExp = np.genfromtxt('experiment.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , usecols=("Time_adjusted","FL3exp","FR3exp","L21exp","L24exp","L27exp","L30exp",) ) #L21exp	L24exp	L27exp	L30exp

timeT = dataT1['Temps']
y1,y2,y3,y4,y5,y6 = dataT1['TemperatureC'], dataT2['TemperatureC'], dataT3['TemperatureC'], dataT4['TemperatureC'], dataT5['TemperatureC'], dataT6['TemperatureC']
timeExp = dataExp['Time_adjusted']
z1,z2,z3,z4,z5,z6 = dataExp['FL3exp'],dataExp['L21exp'],dataExp['L24exp'],dataExp['L27exp'],dataExp['L30exp'],dataExp['FR3exp']

fig, ax = plt.subplots()
NbMarkerT = 100
alphaT = 0.75
orderT = 2
ax.plot(timeT, y1, 'k-^', linewidth=1,  label='Tsolver',  markevery=NbMarkerT, alpha=alphaT)
ax.plot(timeT, y2, 'k-^', linewidth=1,  markevery=NbMarkerT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y3, 'k-^', linewidth=1,	markevery=NbMarkerT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y4, 'k-^', linewidth=1,	markevery=NbMarkerT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y5, 'k-^', linewidth=1,	markevery=NbMarkerT, alpha=alphaT, zorder= orderT)
ax.plot(timeT, y6, 'k-^', linewidth=1,  markevery=NbMarkerT, alpha=alphaT)

NbMarkerExp = 300
alphaExp = 1
orderExp = 1
ax.plot(timeExp, z2, linewidth=5, color='#FF8000', label='Experimental',  markevery=NbMarkerExp, alpha=alphaExp, zorder=orderExp)
ax.plot(timeExp, z3, linewidth=5, color='#FF8000', 	markevery=NbMarkerExp, alpha=alphaExp, zorder=orderExp)
ax.plot(timeExp, z4, linewidth=5, color='#FF8000',	markevery=NbMarkerExp, alpha=alphaExp, zorder=orderExp)
ax.plot(timeExp, z5, linewidth=5, color='#FF8000',  markevery=NbMarkerExp, alpha=alphaExp, zorder=orderExp)
ax.plot(timeExp, z1, '-o', linewidth=4, color='#C3BCBC', label='LHE',  markevery=NbMarkerExp, alpha=alphaExp, zorder=orderExp)
ax.plot(timeExp, z6, '-d',linewidth=4, color='#7C7B7B', label='RHE',  markevery=NbMarkerExp, alpha=alphaExp, zorder=orderExp)

plt.xlim(0,4500)
plt.ylim(150,300)
plt.grid(True)

legend = ax.legend(loc='best', fancybox=True, shadow=True)
plt.xlabel('Time (sec)')
plt.ylabel('Temperature ($^\circ$C)') # if "Times" font is NOT used then the unit is $^\circ$C
# plt.title('SMACS $T(t)$')

#plt.show()
plt.savefig('smacs_CC.pdf', bbox_inches='tight')
plt.savefig('smacs_CC.png', dpi=300, bbox_inches='tight')
