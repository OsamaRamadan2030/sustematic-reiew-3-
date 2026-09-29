import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
plt.rcParams.update({'font.family':'Liberation Sans','font.size':9,'axes.edgecolor':'#52514e','axes.labelcolor':'#0b0b0b',
 'xtick.color':'#52514e','ytick.color':'#52514e','savefig.dpi':600})
INK='#0b0b0b'; SEC='#52514e'; GRID='#e6e5e1'

# ---------------- Figure 1: PRISMA 2020 flow ----------------
fig, ax = plt.subplots(figsize=(7.2, 7.0)); ax.set_xlim(0,100); ax.set_ylim(22,120); ax.axis('off')
def box(x,y,w,h,txt,bold_first=True,fs=8.2,lw=1.0,ec=INK,align='center'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0,rounding_size=0.8",fc='white',ec=ec,lw=lw))
    ax.text(x+(w/2 if align=='center' else 1.6), y+h/2, txt, ha=align, va='center', fontsize=fs, color=INK, linespacing=1.35, wrap=True)
def arrow(x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color=INK,lw=0.9,mutation_scale=9))
def band(y,h,label):
    ax.add_patch(FancyBboxPatch((0.5,y),5,h,boxstyle="round,pad=0,rounding_size=0.8",fc='#dce9f8',ec='#2a78d6',lw=0.8))
    ax.text(3,y+h/2,label,rotation=90,ha='center',va='center',fontsize=8.5,fontweight='bold',color='#184f95')
ax.text(30,118,'Identification of studies via databases and registers',ha='center',va='center',fontsize=8.6,fontweight='bold')
ax.text(80,118,'Identification of studies via other methods',ha='center',va='center',fontsize=8.6,fontweight='bold')
band(95,20,'Identification'); band(58,34,'Screening'); band(40,15,'Eligibility'); band(24,13,'Included')
box(8,97,46,17,"Records identified (n = 14,667)\nBibliographic databases (9): n = 14,388\nGoogle Scholar (first 200 results): n = 200\nTrial/study registries: n = 41\nProQuest Dissertations & Theses: n = 38",fs=7.8)
box(60,97,38,17,"Records identified (n = 245)\nCitation searching: n = 147\nPreprint servers: n = 63\nJournal hand-searching: n = 29\nAuthor contact: n = 6",fs=7.8)
ax.plot([31,31],[97,94],color=INK,lw=0.9); ax.plot([79,79,31],[97,94,94],color=INK,lw=0.9); arrow(31,94,31,91.6)
box(8,84.5,46,7.5,"Records combined before\ndeduplication (n = 14,912)")
box(60,84.5,38,7.5,"Duplicate records removed\nbefore screening (n = 5,433)")
arrow(54,88.2,60,88.2)
arrow(31,85,31,80.5)
box(8,74,46,6.5,"Records screened (n = 9,479)")
box(60,74,38,6.5,"Records excluded (n = 9,127)")
arrow(54,77.2,60,77.2); arrow(31,74,31,69.5)
box(8,63,46,6.5,"Reports sought for retrieval (n = 352)")
box(60,62.5,38,7.5,"Reports not retrieved (n = 11)\n(not assessed for eligibility)",fs=7.8)
arrow(54,66.2,60,66.2); arrow(31,63,31,53.6)
box(8,45,46,8.5,"Reports assessed for eligibility (n = 341)\nincluding 11 assessed from the abstract and\nother accessible primary material",fs=7.8)
box(60,30.5,38,29,"Reports excluded (n = 294)\n• No prospective fall outcome or no valid\n   temporal separation: 99\n• Fall detection/event recognition: 53\n• No individualized model performance: 44\n• No sensor-derived gait predictor: 35\n• Age criterion not met: 27\n• Ineligible publication type: 20\n• Simulated or synthetic fall data: 10\n• Duplicate report: 6",fs=7.3,align='left')
arrow(54,49.2,60,49.2); arrow(31,45,31,35.5)
box(8,24.5,46,11,"Reports included in the review (n = 47)\n36 complete article; 11 abstract and other\naccessible primary material\nIndependent cohort families (n = 37)",lw=1.6,ec='#184f95',fs=7.8)
fig.savefig('fig/Figure1_PRISMA.png',bbox_inches='tight',dpi=600); plt.close(fig)

# ---------------- Figure 2: AUC vs events ----------------
data = [('Dasgupta 2022',14,.99,'I'),('Shah 2023',25,.94,'A'),('Giardini 2025',10,.91,'A'),('Guan 2025',15,.89,'I'),('Sturchio 2021',14,.87,'A'),
('Sotirakis 2024',23,.85,'I'),('Ma 2022',14,.838,'A'),('Doi 2013',16,.81,'A'),('Lo 2019',39,.79,'I'),('Greene 2012',83,.78,'I'),('Horak 2023',91,.751,'A'),
('Nait Aicha 2018',101,.75,'I'),('Schwenk 2014',28,.771,'A'),('Bizovska 2018',15,.760,'A'),('Adeli 2023',20,.762,'I'),('Marschollek 2011',19,.72,'I'),
('Maiora 2024',21,.73,'I'),('Suffoletto 2026',94,.72,'A'),('Mignardot 2014',20,.70,'A'),('Caronni 2023',82,.69,'A'),('Lai 2025',5,.688,'F'),
('Roshdibenam 2021',25,.56,'I'),('Zhang 2024',105,.53,'X'),('Silva 2020',74,.505,'I')]
style={'A':('Apparent (development data)','o','#2a78d6'),'I':('Internal validation (resampling or split)','s','#eb6834'),
       'F':('Prospective evaluation of a fixed score','D','#1baf7a'),'X':('Independent-cohort evaluation (original coefficients)','^','#4a3aa7')}
off={'Dasgupta 2022':(6,-2,'left'),'Shah 2023':(6,-2,'left'),'Giardini 2025':(-6,-2,'right'),'Guan 2025':(6,-2,'left'),'Sturchio 2021':(-6,2,'right'),
'Sotirakis 2024':(6,-2,'left'),'Ma 2022':(-6,-5,'right'),'Doi 2013':(6,-3,'left'),'Lo 2019':(6,-3,'left'),'Greene 2012':(6,4,'left'),'Horak 2023':(-6,-6,'right'),
'Nait Aicha 2018':(6,-3,'left'),'Schwenk 2014':(6,0,'left'),'Bizovska 2018':(-6,3,'right'),'Adeli 2023':(6,-7,'left'),'Marschollek 2011':(-6,0,'right'),
'Maiora 2024':(6,-4,'left'),'Suffoletto 2026':(7,-8,'left'),'Mignardot 2014':(6,-4,'left'),'Caronni 2023':(-6,-3,'right'),'Lai 2025':(6,-3,'left'),
'Roshdibenam 2021':(6,-3,'left'),'Zhang 2024':(-6,6,'right'),'Silva 2020':(-6,6,'right')}
fig, ax = plt.subplots(figsize=(7.2,4.6))
ax.axhline(0.5,color=SEC,lw=0.9,ls=(0,(4,3)),zorder=1); ax.text(4.1,0.508,'Chance (AUC = 0.50)',fontsize=7.5,color=SEC)
ax.axhline(0.761,color='#898781',lw=0.9,ls=(0,(1,2)),zorder=1,label='Median representative AUC (0.761)')
LIM={'Greene 2012','Ma 2022','Giardini 2025','Suffoletto 2026'}
CI={'Doi 2013':(0.69,0.93),'Mignardot 2014':(0.64,0.75),'Horak 2023':(0.680,0.821),'Shah 2023':(0.84,1.00),'Dasgupta 2022':(0.98,1.00),'Roshdibenam 2021':(0.33,0.74)}
for n,e,a,k in data:
    if n in CI:
        lo,hi=CI[n]; ax.plot([e,e],[max(lo,0.45),hi],color=style[k][2],lw=0.9,alpha=0.45,zorder=1,solid_capstyle='butt')
        if lo<0.45: ax.annotate('',xy=(e,0.452),xytext=(e,0.47),arrowprops=dict(arrowstyle='-|>',color=style[k][2],lw=1.0,mutation_scale=7))
for k,(lab,mk,col) in style.items():
    pts=[d for d in data if d[3]==k and d[0] not in LIM]
    ptl=[d for d in data if d[3]==k and d[0] in LIM]
    ax.scatter([p[1] for p in pts],[p[2] for p in pts],marker=mk,s=46,c=col,edgecolors='white',linewidths=1.2,label=f'{lab} (n = {len([d for d in data if d[3]==k])})',zorder=3)
    if ptl: ax.scatter([p[1] for p in ptl],[p[2] for p in ptl],marker=mk,s=40,facecolors='white',edgecolors=col,linewidths=1.6,zorder=3)
from matplotlib.lines import Line2D
extra=[Line2D([0],[0],marker='o',color='w',markerfacecolor='white',markeredgecolor='#52514e',markersize=6.5,markeredgewidth=1.5,label='Open marker: report without complete-article access'),
       Line2D([0],[0],color='#52514e',lw=1.1,label='95% CI or range across resamples (where reported)')]
for n,e,a,k in data:
    dx,dy,ha=off[n]; ax.annotate(n,(e,a),xytext=(dx,dy),textcoords='offset points',fontsize=6.8,color=INK,ha=ha,va='center')
ax.set_xscale('log'); ax.set_xlim(3.8,160); ax.set_ylim(0.45,1.03)
ax.set_xticks([5,10,15,20,30,50,75,100,150]); ax.set_xticklabels(['5','10','15','20','30','50','75','100','150'])
ax.minorticks_off()
ax.set_xlabel('Participants with the outcome event (log scale)'); ax.set_ylabel('Representative AUC')
ax.grid(axis='y',color=GRID,lw=0.6); ax.spines[['top','right']].set_visible(False)
h,l=ax.get_legend_handles_labels(); ax.legend(handles=h+extra,loc='upper center',bbox_to_anchor=(0.5,-0.14),ncol=2,frameon=False,fontsize=7.4,handletextpad=0.4,columnspacing=1.2)
fig.savefig('fig/Figure2_AUC_events.png',bbox_inches='tight',dpi=600); plt.close(fig)

# ---------------- Figure 3: PROBAST+AI ----------------
cols={'Low':'#0ca30c','Unclear':'#eda100','High':'#d03b3b'}
panels=[('A. Part A: concern about model-development quality (n = 45 reports)',
  [('Participants and data sources',20,11,14),('Predictors',36,8,1),('Outcome',31,9,5),('Analysis',0,3,42),('Overall',0,2,43)]),
 ('B. Part B: risk of bias in model evaluation (n = 47 reports)',
  [('Participants and data sources',19,11,17),('Predictors',37,8,2),('Outcome',33,9,5),('Analysis',1,3,43),('Overall',0,2,45)]),
 ('C. Applicability to the intended-use population (development n = 45; evaluation n = 47)',
  [('Development: participants',43,0,2),('Development: predictors',42,3,0),('Development: outcome',43,0,2),('Development: overall',38,3,4),
   ('Evaluation: participants',45,0,2),('Evaluation: predictors',42,4,1),('Evaluation: outcome',46,0,1),('Evaluation: overall',39,4,4)])]
fig, axes = plt.subplots(3,1,figsize=(7.2,7.4),gridspec_kw={'height_ratios':[5,5,8],'hspace':0.55})
for ax,(title,rows) in zip(axes,panels):
    y=np.arange(len(rows))[::-1]
    for yi,(lab,l,u,h) in zip(y,rows):
        tot=l+u+h; left=0
        for name,val in (('Low',l),('Unclear',u),('High',h)):
            if val==0: continue
            w=100*val/tot
            ax.barh(yi,w-0.4,left=left+0.2,height=0.62,color=cols[name],edgecolor='none',)
            if w>=3.0: ax.text(left+w/2,yi,str(val),ha='center',va='center',fontsize=7.6,color='white' if name!='Unclear' else INK,fontweight='bold')
            left+=w
    ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows],fontsize=8)
    ax.set_xlim(0,100); ax.set_xticks([0,25,50,75,100]); ax.set_xticklabels(['0%','25%','50%','75%','100%'],fontsize=7.6)
    ax.set_title(title,loc='left',fontsize=8.8,fontweight='bold',color=INK)
    ax.spines[['top','right']].set_visible(False); ax.tick_params(axis='y',length=0)
from matplotlib.patches import Patch
fig.legend(handles=[Patch(fc=cols['Low'],label='Low'),Patch(fc=cols['Unclear'],label='Unclear'),Patch(fc=cols['High'],label='High')],
 loc='lower center',ncol=3,frameon=False,fontsize=8,bbox_to_anchor=(0.55,0.0))
fig.subplots_adjust(bottom=0.08)
fig.savefig('fig/Figure3_PROBAST_AI.png',bbox_inches='tight',dpi=600); plt.close(fig)
print('ok')
