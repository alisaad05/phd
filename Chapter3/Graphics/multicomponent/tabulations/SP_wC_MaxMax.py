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

"""
The script PhaseALL does all the work: phase fractions, phase compositions, phase enthalpies
"""
"""
Takes as params the phase array and Min-Max combinations for each solute (2 of them)
returns the lines corresponding to the Min Max cross
"""
def Extract_AvgComp_lines(phase_array, MIN1, MAX1, MIN2, MAX2):

	phase_avg_carbon, phase_avg_chromium = phase_array['avg_carbon'], phase_array['avg_chromium']
	w1 = (phase_avg_carbon==MIN1) & (phase_avg_chromium==MIN2)
	w2 = (phase_avg_carbon==MIN1) & (phase_avg_chromium==MAX2)
	w3 = (phase_avg_carbon==MAX1) & (phase_avg_chromium==MIN2)
	w4 = (phase_avg_carbon==MAX1) & (phase_avg_chromium==MAX2)
	phase_Wavg1 , phase_Wavg2 , phase_Wavg3 , phase_Wavg4 = phase_array[w1] , phase_array[w2], phase_array[w3], phase_array[w4]
	return phase_Wavg1 , phase_Wavg2 , phase_Wavg3 , phase_Wavg4
#==================================================================================
"""
deprecated : takes a phase array as parameter and returns the lines corresponding to the Min-Max cross in the gridded input phase compositions
It was used to draw enthalpy in the min and max phase compositions so as to show the largest possible variation
"""
def Extract_IntrinsicComp_lines(phase_array):

	phase_intrsc_carbon, phase_intrsc_chromium = phase_array['intrinsic_carbon'], phase_array['intrinsic_chromium']
	MinCarbon, MaxCarbon = phase_intrsc_carbon.min() , phase_intrsc_carbon.max()
	MinChromium, MaxChromium = phase_intrsc_chromium.min() , phase_intrsc_chromium.max()
	wmin = (phase_intrsc_carbon==MinCarbon) & (phase_intrsc_chromium==MinChromium)
	wmax = (phase_intrsc_carbon==MaxCarbon) & (phase_intrsc_chromium==MaxChromium)
	Min = (MinCarbon,MinChromium)
	Max = (MaxCarbon,MaxChromium)
	return phase_array[wmin] , phase_array[wmax], Min, Max
#==================================================================================
"""
takes the phase compositions computed during solidification paths then computes the enthalpy by interpolating in the gridded input phase compositions
"""
def get_interpolated_enthalpy(phase_real_W, phase_H):
	from scipy.interpolate import griddata
	
	grid_w1, grid_w2, grid_T, grid_H =  phase_H["intrinsic_carbon"], phase_H["intrinsic_chromium"], phase_H["Temperature"], phase_H["PhaseEnthalpy"]
	real_w1, real_w2, real_T = phase_real_W["PhaseComposition_carbon"] , phase_real_W["PhaseComposition_chromium"], phase_real_W["Temperature"] 
	
	interpolated_enthalpy = griddata((grid_w1, grid_w2, grid_T), grid_H, (real_w1, real_w2, real_T), method='linear')  # method='nearest' cubic linear
	return interpolated_enthalpy

########################################################################################################################################	
########################################################################################################################################	

CEM = np.genfromtxt('PhaseFractions-CEM.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
M7C3 = np.genfromtxt('PhaseFractions-M7C3.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction","PhaseComposition_carbon", "PhaseComposition_chromium") )
FCC = np.genfromtxt('PhaseFractions-FCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
BCC = np.genfromtxt('PhaseFractions-BCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
LIQ = np.genfromtxt('PhaseFractions-LIQ.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHOOSE THE NAMES OF YOUR TERNARY SOLUTES AND AVERAGE COMPOSITION INTERVAL <<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
solute1 = "carbon"
solute2 = "chromium"
min_solute1 = 1.8
max_solute1 = 2.2
min_solute2 = 27
max_solute2= 33

liq_w1, liq_w2, liq_w3, liq_w4 = Extract_AvgComp_lines(LIQ, min_solute1, max_solute1, min_solute2, max_solute2)
bcc_w1, bcc_w2, bcc_w3, bcc_w4 = Extract_AvgComp_lines(BCC, min_solute1, max_solute1, min_solute2, max_solute2)
fcc_w1, fcc_w2, fcc_w3, fcc_w4 = Extract_AvgComp_lines(FCC, min_solute1, max_solute1, min_solute2, max_solute2)
m7c3_w1, m7c3_w2, m7c3_w3, m7c3_w4 = Extract_AvgComp_lines(M7C3, min_solute1, max_solute1, min_solute2, max_solute2)
cem_w1, cem_w2, cem_w3, cem_w4 = Extract_AvgComp_lines(CEM, min_solute1, max_solute1, min_solute2, max_solute2)
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHOOSE HERE THE SPECS (COLORS, ...) FOR YOUR PLOT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
colorFCC, colorBCC, colorLIQ , colorM7C3, colorCEM= 'red', 'green', 'blue', 'orange', 'black'
markerFCC , markerBCC , markerLIQ , markerM7C3, markerCEM= '^', 'd', 'o', 'v', 'x'
NbMarker = 20
alphaT = 1
width1 = 1
width2 = 1
lstyle1 = lstyle2 = lstyle3 ='-'
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHOOSE HERE YOUR LAYOUT  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-	
fig,ax7 =plt.subplots()

ax7.set_ylabel(r'$\langle w_{C}^{\phi} \rangle^{\phi}$'+'[wt.$\%$ $C$]')
ax7.set_xlabel(r'Temperature ($^\circ$C)')
# ax7.set_xlim(150,250)
# ax7.set_ylim(-0.05,1.05)
ax7.plot( liq_w4['Temperature'], liq_w4['PhaseComposition_carbon']*(liq_w4['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( bcc_w4['Temperature'], bcc_w4['PhaseComposition_carbon']*(bcc_w4['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( fcc_w4['Temperature'], fcc_w4['PhaseComposition_carbon']*(fcc_w4['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( m7c3_w4['Temperature'], m7c3_w4['PhaseComposition_carbon']*(m7c3_w4['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( cem_w4['Temperature'], cem_w4['PhaseComposition_carbon']*(cem_w4['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.grid(True)

# plt.show()
plt.savefig('Tabulation_wC_MaxMax.png', dpi=300, bbox_inches='tight')
plt.savefig('Tabulation_wC_MaxMax.pdf', bbox_inches='tight')