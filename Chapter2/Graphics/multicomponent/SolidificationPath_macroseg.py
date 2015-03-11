# check http://matplotlib.org/users/customizing.html
sz=20
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
# rc('axes', labelsize=sz)
# rc('xtick', labelsize=sz)
# rc('ytick', labelsize=sz)
# rc('legend', fontsize=14)

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
import numpy as np
import matplotlib.pyplot as plt

CEM = np.genfromtxt('tabs/PhaseFractions-CEM.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
M7C3 = np.genfromtxt('tabs/PhaseFractions-M7C3.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction","PhaseComposition_carbon", "PhaseComposition_chromium") )
FCC = np.genfromtxt('tabs/PhaseFractions-FCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
BCC = np.genfromtxt('tabs/PhaseFractions-BCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
LIQ = np.genfromtxt('tabs/PhaseFractions-LIQ.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("avg_carbon","avg_chromium","Temperature","PhaseFraction", "PhaseComposition_carbon", "PhaseComposition_chromium") )
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CHOOSE THE NAMES OF YOUR TERNARY SOLUTES AND AVERAGE COMPOSITION INTERVAL <<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
solute1 = "carbon"
solute2 = "chromium"
min_solute1 = 1.8
max_solute1 = 2.2
min_solute2 = 27
max_solute2= 33
DRAW_SOLIDF_PATHS_ONLY = False  # True # False
DRAW_ENTHALPY_ALSO = not(DRAW_SOLIDF_PATHS_ONLY)

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

if DRAW_SOLIDF_PATHS_ONLY :
	fig, ( (ax9, ax1, ax2), 
		   (ax10, ax3, ax4),
		   (ax11, ax5, ax6), 
		   (ax12, ax7, ax8)) = plt.subplots(nrows=4, ncols=3)
		   
if DRAW_ENTHALPY_ALSO :
	fig, ( (ax9, ax1, ax2,  ax13),  
		   (ax12, ax7, ax8, ax14)) = plt.subplots(nrows=2, ncols=4)


#-----------------------------------------
#|  ax9    |  ax1     |  ax2    |  
#--------------------------------   ax13
#|  ax10   |  ax3     |  ax4    |  
#-----------------------------------------
#|  ax11   |  ax5     |  ax6    |  
#--------------------------------   ax14
#|  ax12   |  ax7     |  ax8    |  
#-----------------------------------------
# left  = 0.125  # the left side of the subplots of the figure
# right = 0.9    # the right side of the subplots of the figure
# bottom = 0.1   # the bottom of the subplots of the figure
# top = 0.9      # the top of the subplots of the figure
# wspace = 0.2   # the amount of width reserved for blank space between subplots
# hspace = 0.2   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.925, top=0.875, wspace=0.22, hspace=0.22)
# fig.tight_layout()	   
#fig.suptitle('Thermodynamic Tabulations for the Fe-C-Cr system', fontsize=18, fontweight='bold', va='top', ha='center')
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PLOT THE PHASE FRACTIONS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# >>>>>>>> ax9
ax9.set_title('Phase Fractions \n\n'+r'$\langle w_0 \rangle$='+repr(min_solute1)+' wt%C  '+repr(min_solute2)+'wt%Cr')
ax9.set_ylabel(r'$g^{\phi}$'+'[-]')
ax9.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# ax9.set_xlabel('Temperature ($^\circ$C)')
# ax9.set_xlim(150,250)
ax9.set_ylim(-0.05,1.05)
ax9.plot( liq_w1['Temperature'], liq_w1['PhaseFraction'] , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax9.plot( bcc_w1['Temperature'], bcc_w1['PhaseFraction'] , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax9.plot( fcc_w1['Temperature'], fcc_w1['PhaseFraction'] , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax9.plot( m7c3_w1['Temperature'], m7c3_w1['PhaseFraction'] , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax9.plot( cem_w1['Temperature'], cem_w1['PhaseFraction'] , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax9.grid(True)

# >>>>>>>> ax10
# ax10.set_title(r'$\langle w_0 \rangle$='+repr(min_solute1)+'wt%C  '+repr(max_solute2)+'wt%Cr')
# ax10.set_ylabel(r'$g^{\phi}$'+'[-]')
# ax10.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# ax10.set_xlabel('Temperature ($^\circ$C)')
# ax10.set_xlim(150,250)
# ax10.set_ylim(-0.05,1.05)
# ax10.plot( liq_w2['Temperature'], liq_w2['PhaseFraction'] , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax10.plot( bcc_w2['Temperature'], bcc_w2['PhaseFraction'] , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax10.plot( fcc_w2['Temperature'], fcc_w2['PhaseFraction'] , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax10.plot( m7c3_w2['Temperature'], m7c3_w2['PhaseFraction'] , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax10.plot( cem_w2['Temperature'], cem_w2['PhaseFraction'] , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax10.grid(True)

# >>>>>>>> ax11
# ax11.set_title(r'$\langle w_0 \rangle$='+repr(max_solute1)+'wt%C  '+repr(min_solute2)+'wt%Cr')
# ax11.set_ylabel(r'$g^{\phi}$'+'[-]')
# ax11.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# # ax11.set_xlabel('Temperature ($^\circ$C)')
# # ax11.set_xlim(150,250)
# ax11.set_ylim(-0.05,1.05)
# ax11.plot( liq_w3['Temperature'], liq_w3['PhaseFraction'] , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax11.plot( bcc_w3['Temperature'], bcc_w3['PhaseFraction'] , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax11.plot( fcc_w3['Temperature'], fcc_w3['PhaseFraction'] , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax11.plot( m7c3_w3['Temperature'], m7c3_w3['PhaseFraction'] , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax11.plot( cem_w3['Temperature'], cem_w3['PhaseFraction'] , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax11.grid(True)

# >>>>>>>> ax12
ax12.set_title('$\langle w_0 \rangle$='+repr(max_solute1)+'wt%C  '+repr(max_solute2)+'wt%Cr')
ax12.set_ylabel('$g^{\phi}$'+'[-]')
ax12.set_xlabel('Temperature ($^\circ$C)')
# ax12.set_xlim(150,250)
ax12.set_ylim(-0.05,1.05)
ax12.plot( liq_w4['Temperature'], liq_w4['PhaseFraction'] , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax12.plot( bcc_w4['Temperature'], bcc_w4['PhaseFraction'] , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax12.plot( fcc_w4['Temperature'], fcc_w4['PhaseFraction'] , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax12.plot( m7c3_w4['Temperature'], m7c3_w4['PhaseFraction'] , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax12.plot( cem_w4['Temperature'], cem_w4['PhaseFraction'] , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax12.grid(True)
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PLOT THE PHASE COMPOSITIONS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# >>>>>>>> ax1
ax1.set_title('Phase Compositions (wt% '+ solute1 +') \n\n'+'$\langle w_0 \rangle$='+repr(min_solute1)+' wt%C  '+repr(min_solute2)+'wt%Cr')
ax1.set_ylabel('$\langle w_{C}^{\phi} \rangle^{\phi}$'+' [wt% C]')
ax1.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# ax1.set_xlabel('Temperature ($^\circ$C)')
# ax1.set_xlim(150,250)
# ax1.set_ylim(-0.05,1.05)
ax1.plot( liq_w1['Temperature'], liq_w1['PhaseComposition_carbon']*(liq_w1['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax1.plot( bcc_w1['Temperature'], bcc_w1['PhaseComposition_carbon']*(bcc_w1['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax1.plot( fcc_w1['Temperature'], fcc_w1['PhaseComposition_carbon']*(fcc_w1['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax1.plot( m7c3_w1['Temperature'], m7c3_w1['PhaseComposition_carbon']*(m7c3_w1['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax1.plot( cem_w1['Temperature'], cem_w1['PhaseComposition_carbon']*(cem_w1['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax1.grid(True)

# >>>>>>>> ax2
ax2.set_title('Phase Compositions (wt% '+ solute2 +') \n\n'+'$\langle w_0 \rangle$='+repr(min_solute1)+' wt%C  '+repr(min_solute2)+'wt%Cr')
ax2.set_ylabel('$\langle w_{Cr}^{\phi} \rangle^{\phi}$'+' [wt% Cr]')
ax2.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# ax2.set_xlabel('Temperature ($^\circ$C)')
# ax2.set_xlim(150,250)
# ax2.set_ylim(-0.05,1.05)
ax2.plot( liq_w1['Temperature'], liq_w1['PhaseComposition_chromium']*(liq_w1['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax2.plot( bcc_w1['Temperature'], bcc_w1['PhaseComposition_chromium']*(bcc_w1['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax2.plot( fcc_w1['Temperature'], fcc_w1['PhaseComposition_chromium']*(fcc_w1['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax2.plot( m7c3_w1['Temperature'], m7c3_w1['PhaseComposition_chromium']*(m7c3_w1['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax2.plot( cem_w1['Temperature'], cem_w1['PhaseComposition_chromium']*(cem_w1['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax2.grid(True)

# >>>>>>>> ax3
# ax3.set_title(r'$\langle w_0 \rangle$='+repr(min_solute1)+'wt%C  '+repr(max_solute2)+'wt%Cr')
# ax3.set_ylabel(r'$\langle w_{C}^{\phi} \rangle^{\phi}$'+' [wt% C]')
# ax3.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# # ax3.set_xlabel('Temperature ($^\circ$C)')
# # ax3.set_xlim(150,250)
# # ax3.set_ylim(-0.05,1.05)
# ax3.plot( liq_w2['Temperature'], liq_w2['PhaseComposition_carbon']*(liq_w2['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax3.plot( bcc_w2['Temperature'], bcc_w2['PhaseComposition_carbon']*(bcc_w2['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax3.plot( fcc_w2['Temperature'], fcc_w2['PhaseComposition_carbon']*(fcc_w2['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax3.plot( m7c3_w2['Temperature'], m7c3_w2['PhaseComposition_carbon']*(m7c3_w2['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax3.plot( cem_w2['Temperature'], cem_w2['PhaseComposition_carbon']*(cem_w2['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax3.grid(True)

# # >>>>>>>> ax4
# ax4.set_title(r'$\langle w_0 \rangle$='+repr(min_solute1)+'wt%C  '+repr(max_solute2)+'wt%Cr')
# ax4.set_ylabel(r'$\langle w_{Cr}^{\phi} \rangle^{\phi}$'+' [wt% Cr]')
# ax4.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# # ax4.set_xlabel('Temperature ($^\circ$C)')
# # ax4.set_xlim(150,250)
# # ax4.set_ylim(-0.05,1.05)
# ax4.plot( liq_w2['Temperature'], liq_w2['PhaseComposition_chromium']*(liq_w2['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax4.plot( bcc_w2['Temperature'], bcc_w2['PhaseComposition_chromium']*(bcc_w2['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax4.plot( fcc_w2['Temperature'], fcc_w2['PhaseComposition_chromium']*(fcc_w2['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax4.plot( m7c3_w2['Temperature'], m7c3_w2['PhaseComposition_chromium']*(m7c3_w2['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax4.plot( cem_w2['Temperature'], cem_w2['PhaseComposition_chromium']*(cem_w2['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax4.grid(True)

# # >>>>>>>> ax5
# ax5.set_title(r'$\langle w_0 \rangle$='+repr(max_solute1)+'wt%C  '+repr(min_solute2)+'wt%Cr')
# ax5.set_ylabel(r'$\langle w_{C}^{\phi} \rangle^{\phi}$'+' [wt% C]')
# ax5.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# # ax5.set_xlabel('Temperature ($^\circ$C)')
# # ax5.set_xlim(150,250)
# # ax5.set_ylim(-0.05,1.05)
# ax5.plot( liq_w3['Temperature'], liq_w3['PhaseComposition_carbon']*(liq_w3['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax5.plot( bcc_w3['Temperature'], bcc_w3['PhaseComposition_carbon']*(bcc_w3['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax5.plot( fcc_w3['Temperature'], fcc_w3['PhaseComposition_carbon']*(fcc_w3['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax5.plot( m7c3_w3['Temperature'], m7c3_w3['PhaseComposition_carbon']*(m7c3_w3['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax5.plot( cem_w3['Temperature'], cem_w3['PhaseComposition_carbon']*(cem_w3['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
# ax5.grid(True)

# # >>>>>>>> ax6
# ax6.set_title(r'$\langle w_0 \rangle$='+repr(max_solute1)+'wt%C  '+repr(min_solute2)+'wt%Cr')
# ax6.set_ylabel(r'$\langle w_{Cr}^{\phi} \rangle^{\phi}$'+' [wt% Cr]')
# ax6.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# # ax6.set_xlabel('Temperature ($^\circ$C)')
# # ax6.set_xlim(150,250)
# # ax6.set_ylim(-0.05,1.05)
# ax6.plot( liq_w3['Temperature'], liq_w3['PhaseComposition_chromium']*(liq_w3['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax6.plot( bcc_w3['Temperature'], bcc_w3['PhaseComposition_chromium']*(bcc_w3['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax6.plot( fcc_w3['Temperature'], fcc_w3['PhaseComposition_chromium']*(fcc_w3['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax6.plot( m7c3_w3['Temperature'], m7c3_w3['PhaseComposition_chromium']*(m7c3_w3['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax6.plot( cem_w3['Temperature'], cem_w3['PhaseComposition_chromium']*(cem_w3['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
# ax6.grid(True)

# >>>>>>>> ax7
ax7.set_title('$\langle w_0 \rangle$='+repr(max_solute1)+'wt%C  '+repr(max_solute2)+'wt%Cr')
ax7.set_ylabel('$\langle w_{C}^{\phi} \rangle^{\phi}$'+' [wt% C]')
ax7.set_xlabel('Temperature ($^\circ$C)')
# ax7.set_xlim(150,250)
# ax7.set_ylim(-0.05,1.05)
ax7.plot( liq_w4['Temperature'], liq_w4['PhaseComposition_carbon']*(liq_w4['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( bcc_w4['Temperature'], bcc_w4['PhaseComposition_carbon']*(bcc_w4['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( fcc_w4['Temperature'], fcc_w4['PhaseComposition_carbon']*(fcc_w4['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( m7c3_w4['Temperature'], m7c3_w4['PhaseComposition_carbon']*(m7c3_w4['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.plot( cem_w4['Temperature'], cem_w4['PhaseComposition_carbon']*(cem_w4['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax7.grid(True)

# >>>>>>>> ax8
ax8.set_title('$\langle w_0 \rangle$='+repr(max_solute1)+'wt%C  '+repr(max_solute2)+'wt%Cr')
ax8.set_ylabel('$\langle w_{Cr}^{\phi} \rangle^{\phi}$'+' [wt% Cr]')
ax8.set_xlabel('Temperature ($^\circ$C)')
# ax8.set_xlim(150,250)
# ax8.set_ylim(-0.05,1.05)
ax8.plot( liq_w4['Temperature'], liq_w4['PhaseComposition_chromium']*(liq_w4['PhaseFraction']>0) , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax8.plot( bcc_w4['Temperature'], bcc_w4['PhaseComposition_chromium']*(bcc_w4['PhaseFraction']>0) , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax8.plot( fcc_w4['Temperature'], fcc_w4['PhaseComposition_chromium']*(fcc_w4['PhaseFraction']>0) , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax8.plot( m7c3_w4['Temperature'], m7c3_w4['PhaseComposition_chromium']*(m7c3_w4['PhaseFraction']>0) , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax8.plot( cem_w4['Temperature'], cem_w4['PhaseComposition_chromium']*(cem_w4['PhaseFraction']>0) , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width2,   markevery=NbMarker, alpha=alphaT)
ax8.grid(True)


#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PLOT THE PHASE ENTHALPIES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

CEM_enthalpy = np.genfromtxt('tabs/PhaseEnthalpy-CEM.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("intrinsic_carbon","intrinsic_chromium","Temperature","PhaseEnthalpy") )
M7C3_enthalpy = np.genfromtxt('tabs/PhaseEnthalpy-M7C3.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("intrinsic_carbon","intrinsic_chromium","Temperature","PhaseEnthalpy") )
FCC_enthalpy = np.genfromtxt('tabs/PhaseEnthalpy-FCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True ,  usecols=("intrinsic_carbon","intrinsic_chromium","Temperature","PhaseEnthalpy") )
BCC_enthalpy = np.genfromtxt('tabs/PhaseEnthalpy-BCC.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("intrinsic_carbon","intrinsic_chromium","Temperature","PhaseEnthalpy") )
LIQ_enthalpy = np.genfromtxt('tabs/PhaseEnthalpy-LIQ.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("intrinsic_carbon","intrinsic_chromium","Temperature","PhaseEnthalpy") )


# Interpolate the enthalpy in the phase composition grid using the previously obtained phase compositions
liq_h_min = get_interpolated_enthalpy(liq_w1,LIQ_enthalpy)
liq_h_max = get_interpolated_enthalpy(liq_w4,LIQ_enthalpy)
bcc_h_min = get_interpolated_enthalpy(bcc_w1,BCC_enthalpy)
bcc_h_max = get_interpolated_enthalpy(bcc_w4,BCC_enthalpy)
fcc_h_min = get_interpolated_enthalpy(fcc_w1,FCC_enthalpy)
fcc_h_max = get_interpolated_enthalpy(fcc_w4,FCC_enthalpy)
m7c3_h_min = get_interpolated_enthalpy(m7c3_w1,M7C3_enthalpy)
m7c3_h_max = get_interpolated_enthalpy(m7c3_w4,M7C3_enthalpy)
cem_h_min = get_interpolated_enthalpy(cem_w1,CEM_enthalpy)
cem_h_max = get_interpolated_enthalpy(cem_w4,CEM_enthalpy)

# ax13 = plt.subplot2grid((4,4), (0,3), rowspan=2)
# >>>>>>>> ax13
ax13.set_title('Phase Enthalpies \n\n'+'$\langle w_0 \rangle$='+repr(min_solute1)+' wt%C  '+repr(min_solute2)+'wt%Cr')
ax13.set_ylabel('$\langle h^{\phi} \rangle^{\phi}$'+' [J/Kg]')
ax13.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# ax13.set_xlabel('Temperature ($^\circ$C)')
ax13.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax13.plot( liq_w1['Temperature'], liq_h_min , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax13.plot( bcc_w1['Temperature'], bcc_h_min , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax13.plot( fcc_w1['Temperature'], fcc_h_min , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax13.plot( m7c3_w1['Temperature'], m7c3_h_min  , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax13.plot( cem_w1['Temperature'], cem_h_min , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax13.grid(True)

# ax14 = plt.subplot2grid((4,4), (2,3), rowspan=2)
# >>>>>>>> ax14
ax14.set_title('$\langle w_0 \rangle$='+repr(max_solute1)+' wt%C  '+repr(max_solute2)+'wt%Cr')
ax14.set_ylabel('$\langle h^{\phi} \rangle^{\phi}$'+' [J/Kg]')
ax14.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax14.set_xlabel('Temperature ($^\circ$C)')
# ax14.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax14.plot( liq_w1['Temperature'], liq_h_max , color= colorLIQ, linestyle= lstyle1, marker= markerLIQ, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax14.plot( bcc_w1['Temperature'], bcc_h_max , color= colorBCC, linestyle= lstyle1, marker= markerBCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax14.plot( fcc_w1['Temperature'], fcc_h_max , color= colorFCC, linestyle= lstyle1, marker= markerFCC, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax14.plot( m7c3_w1['Temperature'], m7c3_h_max  , color= colorM7C3, linestyle= lstyle1, marker= markerM7C3, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax14.plot( cem_w1['Temperature'], cem_h_max , color= colorCEM, linestyle= lstyle1, marker= markerCEM, markersize=8, linewidth=width1,   markevery=NbMarker, alpha=alphaT)
ax14.grid(True)

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CREATE CUSTOM LEGEND <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# Get artists and labels for legend and chose which ones to display
handles, labels = ax1.get_legend_handles_labels()
display = (0,1,2)

# Create custom artists
CEM_art = plt.Line2D((0,1),(0,0), color=colorCEM, marker=markerCEM, linestyle='-', linewidth=2)
M7C3_art = plt.Line2D((0,1),(0,0), color=colorM7C3, marker=markerM7C3, linestyle='-', linewidth=2)
FCC_art = plt.Line2D((0,1),(0,0), color=colorFCC, marker=markerFCC, linestyle='-', linewidth=2)
BCC_art = plt.Line2D((0,1),(0,0), color=colorBCC, marker=markerBCC, linestyle='-', linewidth=2)
LIQ_art = plt.Line2D((0,1),(0,0), color=colorLIQ, marker=markerLIQ, linestyle='-', linewidth=2)

#Create legend from custom artist/label lists
fig.legend([handle for i,handle in enumerate(handles) if i in display]+[LIQ_art, BCC_art, FCC_art, M7C3_art, CEM_art],
         [label for i,label in enumerate(labels) if i in display]+['LIQ', 'BCC','FCC',  'M7C3', 'CEM'],loc='upper right', fancybox=True, shadow=True) #center left

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SHOW OR SAVE THE PLOT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
# plt.show()
plt.savefig('SP_macroseg.png', dpi=300, bbox_inches='tight')
plt.savefig('SP_macroseg.pdf', bbox_inches='tight')