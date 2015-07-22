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
C2K = 0


# IMPORT
data1 = np.genfromtxt('capteursTP_nomacro/Capteur1.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )
# data2 = np.genfromtxt('capteursTP_nomacro/Capteur2.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )
# data3 = np.genfromtxt('capteursTP_nomacro/Capteur3.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )
data4 = np.genfromtxt('capteursTP_nomacro/Capteur4.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","FractionLiq","FractionBCC","FractionFCC","FractionM7C3","FractionCementite") )
# data5 = np.genfromtxt('capteursTP_nomacro/Capteur5.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
# data6 = np.genfromtxt('capteursTP_nomacro/Capteur6.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
# data7 = np.genfromtxt('capteursTP_nomacro/Capteur7.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )
# data8 = np.genfromtxt('capteursTP_nomacro/Capteur8.txt', delimiter=None, skip_header=0, skip_footer=0, names=True , usecols=("Temps","TemperatureC") )

x, y1, y2, y3, y4, y5 = data1['Temps'], data1['FractionLiq'], data1['FractionBCC'], data1['FractionFCC'], data1['FractionM7C3'], data1['FractionCementite']
# x2, y2 = data2['Temps'], data1['TemperatureC']
# x3, y3 = data3['Temps'], data3['TemperatureC']
# x4, y4 = data4['Temps'], data4['TemperatureC']

# SETTINGS
NbMarker = 2000
alphaT = 0.85
width1 = 2
ms = 6
ls ='-'
c1, c2 , c3, c4, c5 = "y" , "b", "r", "g", "m"
m1, m2 , m3, m4, m5 = "s" , "o", "v", "d" , "x"
# m1, m2 , m3, m4, m5= "" , "", "", "", ""

# PLOT 1
fig, ax1 = plt.subplots(figsize=(8,8))

ax1.plot(x,y1, color= c1, linestyle= ls, marker= m1, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="Liquid"  )
ax1.plot(x, y2, color= c2, linestyle= ls, marker= m2, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="BCC"  )
ax1.plot(x, y3, color= c3, linestyle= ls, marker= m3, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="FCC"  )
ax1.plot(x, y4, color= c4, linestyle= ls, marker= m4, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="M7C3"  )
ax1.plot(x, y5, color= c5, linestyle= ls, marker= m5, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="CEM"  )

x, y1, y2, y3, y4, y5 = data4['Temps'], data4['FractionLiq'], data4['FractionBCC'], data4['FractionFCC'], data4['FractionM7C3'], data4['FractionCementite']
ls ='--'
ax1.plot(x,y1, color= c1, linestyle= ls, marker= m1, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="Liquid"  )
ax1.plot(x, y2, color= c2, linestyle= ls, marker= m2, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="BCC"  )
ax1.plot(x, y3, color= c3, linestyle= ls, marker= m3, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="FCC"  )
ax1.plot(x, y4, color= c4, linestyle= ls, marker= m4, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="M7C3"  )
ax1.plot(x, y5, color= c5, linestyle= ls, marker= m5, markersize=ms, linewidth=width1,   markevery=NbMarker, alpha=alphaT, label="CEM"  )

# ax1.set_title('Transformation Paths (without macrosegregation)')
ax1.set_ylabel("Volume Fraction (-)")
ax1.set_xlabel('Time (sec)')
ax1.set_xlim(xmax=12000)
ax1.set_ylim(ymin=-0.05, ymax=1.05)
ax1.grid(True)


handles, labels = ax1.get_legend_handles_labels()
display = (0,1,2)

# Create custom artists
Liquid = plt.Line2D((0,1),(0,0), color=c1,  linestyle='-', marker= m1,  linewidth=2)
BCC = plt.Line2D((0,1),(0,0), color=c2,  linestyle='-',  marker= m2,  linewidth=2)
FCC = plt.Line2D((0,1),(0,0), color=c3,  linestyle='-',  marker=m3, linewidth=2)
CARB = plt.Line2D((0,1),(0,0), color=c4,  linestyle='-', marker=m4,  linewidth=2)
CEM = plt.Line2D((0,1),(0,0), color=c5,  linestyle='-',  marker=m5, linewidth=2)

pos1 = plt.Line2D((0,1),(0,0), color="k",  linestyle='-',  linewidth=2)
pos4 = plt.Line2D((0,1),(0,0), color="k",  linestyle='--', linewidth=2)
ax1.legend([Liquid, BCC, FCC, CARB, CEM, pos1,pos4],['LIQ', 'BCC', 'FCC', 'M$_7$C$_3$', 'CEM','Bottom', 'Top'],loc='right', fancybox=True, shadow=True)

# plt.show()
plt.savefig('TP_nomacro.png', dpi=300, bbox_inches='tight')
plt.savefig('TP_nomacro.pdf', bbox_inches='tight')