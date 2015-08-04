# check http://matplotlib.org/users/customizing.html
sz=17
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('axes', labelsize=sz)
rc('xtick', labelsize=sz)
rc('ytick', labelsize=sz)
rc('legend', fontsize=13)
rc('axes', titlesize=sz)
rc('grid', alpha=0.5)
plt.rcParams['text.latex.preamble']=[r"\usepackage{utopia}"]

dataZZ = np.genfromtxt('data_268_ZZ.csv', delimiter=",", 
			skip_header=0, skip_footer=0, names=True , 
			usecols=("arc_length","TemperatureC","Concentration_carbon","Concentration_chromium")
			)

dataFreckle = np.genfromtxt('data_268_Freckle.csv', delimiter=",", 
			skip_header=0, skip_footer=0, names=True , 
			usecols=("arc_length","TemperatureC","Concentration_carbon","Concentration_chromium")
			)

NbMarker = 25
alphaT = 0.85
width1 = 1
ms = 6
lstyle1 ='-'
lstyle2 ='-'
c1 = "k"
c2 = (0.5,0.5,0.5)

fig, ax1 = plt.subplots()

xC1, xCr1 , y1 = dataZZ['Concentration_carbon'], dataZZ['Concentration_chromium'], dataZZ['arc_length'] 
xC2, xCr2 , y2 = dataFreckle['Concentration_carbon'], dataFreckle['Concentration_chromium'], dataFreckle['arc_length'] 

xC_rel1 = (xC1-2.0)*100/2.0 
xCr_rel1 = (xCr1-30.0)*100/30.0 
xC_rel2 = (xC2-2.0)*100/2.0 
xCr_rel2 = (xCr2-30.0)*100/30.0 

# ax1.set_title('Relative macrosegregation in a vertical cut plane')
#ax1.tick_params(axis='y', left='off', right='off', labelbottom='off')
ax1.set_ylabel('Distance from chill [m]')
#ax1.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax1.set_xlabel('Relative segregation'+r'$\frac{\langle  w_i \rangle - \langle  w_i \rangle_0 }{\langle  w_i \rangle_0 }$ [\%]' )
ax1.set_xlim(-8,8)
ax1.set_ylim(ymin=-0.005, ymax=0.08)
ax1.plot(xC_rel1,y1 , color= c1, linestyle= lstyle1, marker= 's', markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT,   label= "carbon - ZZ'"   )
ax1.plot(xCr_rel1,y1 , color= c1, linestyle= lstyle1, marker= 'o', markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT,  label= "chromium - ZZ'" )
ax1.plot(xC_rel2,y2 , color= c2, linestyle= lstyle2, marker= 's', markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT,   label= "carbon - FF'" )
ax1.plot(xCr_rel2,y2 , color= c2, linestyle= lstyle2, marker= 'o', markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT,  label= "chromium - FF'" )
legend = ax1.legend(loc='best', fancybox=True, shadow=True)

# ax1.axvline(x=0, lw=2, ls="--", color="k")

ax1.grid(True)

# plt.show()
# plt.savefig('final_segregation_ZZ_FF.png', dpi=300, bbox_inches='tight')
plt.savefig('final_segregation_ZZ_FF.pdf', bbox_inches='tight')