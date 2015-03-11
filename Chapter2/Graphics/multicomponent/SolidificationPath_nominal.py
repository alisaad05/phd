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
rc('legend', fontsize=16)

def get_test_AvgCompositions(phase_array):

	phase_avg_carbon, phase_avg_chromium = phase_array['avg_carbon'], phase_array['avg_chromium']
	w1 = (phase_avg_carbon==2) & (phase_avg_chromium==30)
	phase_Wavg1 = phase_array[w1]
	return phase_Wavg1
		
import numpy as np
import matplotlib.pyplot as plt

CEM = np.genfromtxt('tabs/PhaseFractions-CEM.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction"))
M7C3 = np.genfromtxt('tabs/PhaseFractions-M7C3.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction"))
FCC = np.genfromtxt('tabs/PhaseFractions-FCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction"))
BCC = np.genfromtxt('tabs/PhaseFractions-BCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction"))
LIQ = np.genfromtxt('tabs/PhaseFractions-LIQ.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction"))

liq_w1= get_test_AvgCompositions(LIQ)
bcc_w1= get_test_AvgCompositions(BCC)
fcc_w1= get_test_AvgCompositions(FCC)
m7c3_w1= get_test_AvgCompositions(M7C3)
cem_w1= get_test_AvgCompositions(CEM)

colorFCC, colorBCC, colorLIQ , colorM7C3, colorCEM= 'red', 'green', 'blue', 'orange', 'black'
markerFCC , markerBCC , markerLIQ , markerM7C3, markerCEM= '^', 'd', 'o', 's', '*'
NbMarker = 10
alphaT = 0.85
width1 = 1
ms = 7
lstyle1 = lstyle2 = lstyle3 ='-'

fig, ax1 = plt.subplots()

##### AVG COMPOSITION 1 : 2 wt%C 30 wt%Cr
#ax1.set_title('Transformation Path')
ax1.set_ylabel('Volume Phase Fraction (-)')
#ax1.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax1.set_xlabel('Temperature ($^\circ$C)')
#ax1.set_xlim(150,250)
ax1.set_ylim(-0.05,1.05)
ax1.plot( liq_w1['Temperature'], liq_w1['PhaseFraction'] , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT,label= "Liquid" )
ax1.plot( bcc_w1['Temperature'], bcc_w1['PhaseFraction'] , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label= "BCC")
ax1.plot( fcc_w1['Temperature'], fcc_w1['PhaseFraction'] , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label= "FCC")
ax1.plot( m7c3_w1['Temperature'], m7c3_w1['PhaseFraction'] , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label= "$M_7C_3$")
ax1.plot( cem_w1['Temperature'], cem_w1['PhaseFraction'] , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label= "CEM")
legend = ax1.legend(loc='best', fancybox=True, shadow=True)
ax1.grid(True)

#figManager = plt.get_current_fig_manager()
#figManager.window.showMaximized()
#plt.show()
plt.savefig('SP_nominal.png', dpi=300, bbox_inches='tight')
plt.savefig('SP_nominal.pdf', bbox_inches='tight')