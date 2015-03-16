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
fig,ax =plt.subplots()
plt.axis('off')
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CREATE CUSTOM LEGEND <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# Get artists and labels for legend and chose which ones to display
handles, labels = ax.get_legend_handles_labels()
display = (0,1,2)

# Create custom artists
CEM_art = plt.Line2D((0,1),(0,0), color=colorCEM, marker=markerCEM, linestyle='-', linewidth=2)
M7C3_art = plt.Line2D((0,1),(0,0), color=colorM7C3, marker=markerM7C3, linestyle='-', linewidth=2)
FCC_art = plt.Line2D((0,1),(0,0), color=colorFCC, marker=markerFCC, linestyle='-', linewidth=2)
BCC_art = plt.Line2D((0,1),(0,0), color=colorBCC, marker=markerBCC, linestyle='-', linewidth=2)
LIQ_art = plt.Line2D((0,1),(0,0), color=colorLIQ, marker=markerLIQ, linestyle='-', linewidth=2)

#Create legend from custom artist/label lists
fig.legend([handle for i,handle in enumerate(handles) if i in display]+[LIQ_art, BCC_art, FCC_art, M7C3_art, CEM_art],
         [label for i,label in enumerate(labels) if i in display]+['LIQ', 'BCC','FCC',  'M$_7$C$_3$', 'CEM'],loc='upper right', fancybox=True, shadow=True) 
		 
# plt.show()
plt.savefig('Tabulation_Legend.png', dpi=300, bbox_inches='tight')
plt.savefig('Tabulation_Legend.pdf', bbox_inches='tight')