import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib import rc
# for Palatino and other sans serif fonts (Helvetica, Avant Garde, Computer Modern Sans serif) use:
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# for Palatino and other serif fonts (Times, Palatino, New Century Schoolbook, Bookman, Computer Modern Roman) use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


data1 = np.genfromtxt('DarcyBlocking_disabled.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , 
						usecols=("Temps", 
						# "CodeConvergence", 
								 # "vA", "vM", 
								 "mM", "mMpct", 
								 "ml" , "ms", 
								 # "mA",
#								 "Vmin", "Vmax" , 
								 # "msolute", "msoluteM", "msoluteM_pct",
								 # "eM", "eA","e_system"  
								 ) 
					)
					
					
data2 = np.genfromtxt('DarcyBlocking25pct.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , 
						usecols=("Temps", 
						# "CodeConvergence", 
								 # "vA", "vM", 
								 "mM", "mMpct", 
								 "ml" , "ms", 
								 # "mA",
#								 "Vmin", "Vmax" , 
								 # "msolute", "msoluteM", "msoluteM_pct",
								 # "eM", "eA","e_system"  
								 ) 
					)
					
data3 = np.genfromtxt('DarcyBlocking50pct.txt', delimiter='\t', skip_header=0, skip_footer=0, names=True , 
						usecols=("Temps", 
						# "CodeConvergence", 
								 # "vA", "vM", 
								 "mM", "mMpct", 
								 "ml" , "ms", 
								 # "mA",
#								 "Vmin", "Vmax" , 
								 # "msolute", "msoluteM", "msoluteM_pct",
								 # "eM", "eA","e_system"  
								 ) 
					)

time1 = data1['Temps']
time2 = data2['Temps']
time3 = data3['Temps']

######################################################################################3
marker = itertools.cycle(('^', 's', 'o', 'p', 'v'))  #randomize marker style
color = itertools.cycle(('g', 'b', 'r', 'c', 'y', 'k', 'm'))  #randomize color
ms = 7
mf = 200
lw = 2
al = 0.9
cA = "k"
cM = "r"
cl = "r"
cs = "b"
######################################################################################3
# fig, ax = plt.subplots()
fig, (	(ax1, ax2, ax3), 
		(ax4, ax5, ax6),
		(ax7, ax8, ax9)	) = plt.subplots(nrows=3, ncols=3)
# fig.suptitle('Dashboard P0C', va='top', ha='center',
						# fontsize=18, fontweight='bold',
						# )		
		

######################################################################################
ax1.plot(time, data['msolute'], marker = marker.next(), color = color.next(), lw=lw,  label='msolute',  markevery=mf, alpha=al, ms=ms)
# ax1.set_xlim(0,4500)
# ax1.set_ylim(0,4500)
ax1.grid(True)
# ax1.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax1.set_title('System solute mass')
# ax1.set_ylabel(r'$g^{\phi}$'+'[-]')
######################################################################################
ax2.plot(time, data['msoluteM'], marker = marker.next(), color = color.next(), lw=lw,  label='msoluteM',  markevery=mf, alpha=al, ms=ms) # m_solute Vmax
# ax2.set_xlim(0,4500)
# ax2.set_ylim(0,4500)
ax2.grid(True)
# ax2.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax2.set_title('Metal solute mass')
# ax2.set_ylabel(r'$g^{\phi}$'+'[-]')
######################################################################################
# msoluteM = data['msoluteM']
msoluteM_pct = data['msoluteM_pct']
# msoluteM_init = msoluteM[0]
# msoluteM_pct = 100*(msoluteM-msoluteM_init)/msoluteM_init
ax3.plot(time, msoluteM_pct, marker = marker.next(), color = color.next(), lw=lw,  label='mM(pct)',  markevery=mf, alpha=al, ms=ms)
# ax3.set_xlim(0,4500)
# ax3.set_ylim(0,4500)
ax3.grid(True)
# ax3.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
# ax3.set_title('Relative change of Metal mass ($\%$)')
ax3.set_title('Metal solute mass variation (pct)')
# ax3.set_ylabel(r'$g^{\phi}$'+'[-]')	
######################################################################################
######################################################################################
######################################################################################
ax4.plot(time, data['vM'], marker = marker.next(), color = cM, lw=lw,  label='vM',  markevery=mf, alpha=al, ms=ms)
ax4.plot(time, data['vA'], marker = marker.next(), color = cA, lw=lw,  label='vA',  markevery=mf*3, alpha=al, ms=ms)
# ax4.set_xlim(0,4500)
# ax4.set_ylim(ymin=0.003, ymax=0.005)
ax4.grid(True)
# ax4.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax4.set_title('Volume Air/Metal')
# ax4.set_ylabel(r'$g^{\phi}$'+'[-]')
######################################################################################
ax5.plot(time, data['mM'], marker = marker.next(), color = cM, lw=lw,  label='mM',  markevery=mf, alpha=al, ms=ms)
ax5.plot(time, data['mA'], marker = marker.next(), color = cA, lw=lw,  label='mA',  markevery=mf*3, alpha=al, ms=ms)
# ax5.set_xlim(0,4500)
# ax5.set_ylim(ymin=20, ymax=40)
ax5.grid(True)
# ax5.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax5.set_title('Mass Air/Metal')
# ax5.set_ylabel(r'$g^{\phi}$'+'[-]')
######################################################################################
ax6.plot(time, data['ml'], marker = marker.next(), color = cl, lw=lw,  label='ml',  markevery=mf, alpha=al, ms=ms)
ax6.plot(time, data['ms'], marker = marker.next(), color = cs, lw=lw,  label='ms',  markevery=mf*3, alpha=al, ms=ms)
# ax6.set_xlim(0,4500)
# ax6.set_ylim(0,4500)
ax6.grid(True)
# ax6.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax6.set_title('Mass Liquid/Solid')
# ax6.set_ylabel(r'$g^{\phi}$'+'[-]')
######################################################################################
######################################################################################
######################################################################################
y1, y2 = data['eM'], data['eA']
ax7.plot(time, y1, marker = marker.next(), color = cM, lw=lw,  label='eM',  markevery=mf, alpha=al, ms=ms)
ax7.plot(time, y2, marker = marker.next(), color = cA, lw=lw,  label='eA',  markevery=mf*3, alpha=al, ms=ms)
# ax7.set_xlim(0,4500)
# ax7.set_ylim(ymin=3e6, ymax=3.5e6)
ax7.grid(True)
# ax7.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax7.set_title('Energy Air/Metal')
# ax7.set_ylabel(r'$g^{\phi}$'+'[-]')
######################################################################################
ax8.plot(time, data['e_system'], marker = marker.next(), color = color.next(), lw=lw,  label='Base',  markevery=mf, alpha=al, ms=ms)
# ax8.set_xlim(0,4500)
# ax8.set_ylim(0,4500)
ax8.grid(True)
# ax8.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax8.set_title('Energy system')
# ax8.set_ylabel(r'$g^{\phi}$'+'[-]')
######################################################################################
ax9.plot(time, data['mMpct'], marker = marker.next(), color = color.next(), lw=lw,  label='mMpct',  markevery=mf, alpha=al, ms=ms)
# ax9.set_xlim(0,4500)
# ax9.set_ylim(0,4500)
ax9.grid(True)
# ax9.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
ax9.set_title('Metal mass variation (pct)')
# ax9.set_ylabel(r'$g^{\phi}$'+'[-]')

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
# plt.show()
plt.savefig('Dashboard_P0C.png', dpi=300, bbox_inches='tight')
plt.savefig('Dashboard_P0C.pdf', bbox_inches='tight')

