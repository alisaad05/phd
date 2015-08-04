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

#####################
########## NO  MACRO
#####################

# IMPORT
data1 = np.genfromtxt('capteursTP_nomacro/Capteur1.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )
data4 = np.genfromtxt('capteursTP_nomacro/Capteur4.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )

# SETTINGS
NbMarker = 2000
alphaT = 0.85
width1 = 1.5
ms = 6
ls_solid ='-'
ls_dashed ='--'
c1, c2 , c3, c4, c5 = "y" , "b", "r", "g", "m"
m1, m2 , m3, m4, m5 = "s" , "o", "v", "d" , "x"
# m1, m2 , m3, m4, m5= "" , "", "", "", ""

# PLOT 1
fig, (ax1,ax2) = plt.subplots(nrows=2, sharex=True,
									   figsize=(12,10),
													)

x, y1, y2, y3, y4, y5 = data1['Temps'], data1['FractionLiq'], data1['FractionBCC'], data1['FractionFCC'], data1['FractionM7C3'], data1['FractionCementite']
ax1.plot(x,y1, color= c1, linestyle= ls_solid, marker= m1, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="Liquid"  )
ax1.plot(x, y2, color= c2, linestyle= ls_solid, marker= m2, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="BCC"  )
ax1.plot(x, y3, color= c3, linestyle= ls_solid, marker= m3, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="FCC"  )
ax1.plot(x, y4, color= c4, linestyle= ls_solid, marker= m4, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="M7C3"  )
ax1.plot(x, y5, color= c5, linestyle= ls_solid, marker= m5, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="CEM"  )

x, y1, y2, y3, y4, y5 = data4['Temps'], data4['FractionLiq'], data4['FractionBCC'], data4['FractionFCC'], data4['FractionM7C3'], data4['FractionCementite']
ax1.plot(x,y1, color= c1, linestyle= ls_dashed, marker= m1, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="Liquid"  )
ax1.plot(x, y2, color= c2, linestyle= ls_dashed, marker= m2, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="BCC"  )
ax1.plot(x, y3, color= c3, linestyle= ls_dashed, marker= m3, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="FCC"  )
ax1.plot(x, y4, color= c4, linestyle= ls_dashed, marker= m4, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="M7C3"  )
ax1.plot(x, y5, color= c5, linestyle= ls_dashed, marker= m5, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="CEM"  )

ax1.set_title('(a) Without macrosegregation')
ax1.set_ylabel("Phase fraction [-]")
# ax1.set_xlabel('Time (sec)')
ax1.set_xlim(xmax=12000)
ax1.set_ylim(ymin=-0.05, ymax=1.05)
ax1.grid(True)

#####################
########## WITH MACRO
#####################
data1 = np.genfromtxt('capteursTP_macro/Capteur1.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )
data4 = np.genfromtxt('capteursTP_macro/Capteur4.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )

x, y1, y2, y3, y4, y5 = data1['Temps'], data1['FractionLiq'], data1['FractionBCC'], data1['FractionFCC'], data1['FractionM7C3'], data1['FractionCementite']
ax2.plot(x,y1, color= c1, linestyle= ls_solid, marker= m1, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="Liquid"  )
ax2.plot(x, y2, color= c2, linestyle= ls_solid, marker= m2, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="BCC"  )
ax2.plot(x, y3, color= c3, linestyle= ls_solid, marker= m3, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="FCC"  )
ax2.plot(x, y4, color= c4, linestyle= ls_solid, marker= m4, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="M7C3"  )
ax2.plot(x, y5, color= c5, linestyle= ls_solid, marker= m5, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="CEM"  )

x, y1, y2, y3, y4, y5 = data4['Temps'], data4['FractionLiq'], data4['FractionBCC'], data4['FractionFCC'], data4['FractionM7C3'], data4['FractionCementite']
ax2.plot(x,y1, color= c1, linestyle= ls_dashed, marker= m1, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="Liquid"  )
ax2.plot(x, y2, color= c2, linestyle= ls_dashed, marker= m2, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="BCC"  )
ax2.plot(x, y3, color= c3, linestyle= ls_dashed, marker= m3, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="FCC"  )
ax2.plot(x, y4, color= c4, linestyle= ls_dashed, marker= m4, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="M7C3"  )
ax2.plot(x, y5, color= c5, linestyle= ls_dashed, marker= m5, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="CEM"  )

ax2.set_title('(b) With macrosegregation')
ax2.set_ylabel("Phase fraction [-]")
ax2.set_xlabel('Time (sec)')
ax2.set_xlim(xmax=12000)
ax2.set_ylim(ymin=-0.05, ymax=1.05)
ax2.grid(True)

#####################
########## LEGEND
#####################

# handles, labels = ax1.get_legend_handles_labels()
# display = (0,1,2)

delta = 0.14

# Create custom artists
Liquid = plt.Line2D((0,1),(0,0), color=c1,  linestyle='-', marker= m1,  linewidth=2)
BCC = plt.Line2D((0,1),(0,0), color=c2,  linestyle='-',  marker= m2,  linewidth=2)
FCC = plt.Line2D((0,1),(0,0), color=c3,  linestyle='-',  marker=m3, linewidth=2)
CARB = plt.Line2D((0,1),(0,0), color=c4,  linestyle='-', marker=m4,  linewidth=2)
CEM = plt.Line2D((0,1),(0,0), color=c5,  linestyle='-',  marker=m5, linewidth=2)

pos1 = plt.Line2D((0,1),(0,0), color="k",  linestyle='-',  linewidth=2)
pos4 = plt.Line2D((0,1),(0,0), color="k",  linestyle='--', linewidth=2)
ax1.legend([Liquid, BCC, FCC, CARB, CEM],['LIQ', 'BCC', 'FCC', 'M$_7$C$_3$', 'CEM'], 
	fancybox=True, shadow=False, 
	bbox_to_anchor=[0.68, -0.2+delta], 
	loc='center', 
	ncol=5,
	# borderaxespad=0.25,
		)

ax2.legend([pos1,pos4],['Bottom', 'Top'], 
	fancybox=True, shadow=False, 
	bbox_to_anchor=[0.13, 1+delta],   # [0.75, 1.1]
	loc='center', 
	ncol=2,
	# borderaxespad=0.25,
						)

# plt.show()
# # plt.savefig('TP_both.png', dpi=300, bbox_inches='tight')
plt.savefig('TP_both.pdf', bbox_inches='tight')