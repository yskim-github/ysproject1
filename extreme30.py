import csv
import pandas as pd
import datetime
import geopandas as gpd
import matplotlib.pyplot as plt
import mapclassify
from mpl_toolkits.axes_grid1 import make_axes_locatable


##############################이상기후 평균기온 평년#########################################################################33
a=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/tavg_10davg_mask_farmland/%d/tavg_10davg_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    a.append(f)

a1=list()
for j in range(0,30):
    f1=a[j].transpose()
    f1.rename(columns=f1.iloc[0],inplace=True)
    f1=f1.iloc[1:,:]
    f1['date']=pd.to_datetime(f1.index)
    f1.set_index('date',inplace=True)
    a1.append(f1)

a1[0]['month']=a1[0].index[0:len(a1[0].index)].month
a1[0]['day']=a1[0].index[0:len(a1[0].index)].day
a2=a1[0]

for k in range(1,30):
    a1[k]['month']=a1[k].index[0:len(a1[k].index)].month
    a1[k]['day']=a1[k].index[0:len(a1[k].index)].day
    a2=pd.concat([a1[k],a2], axis=0)

a3=a2.reset_index()
a4=a3.iloc[:,1:]
a5=a4.groupby(['month','day'],as_index=False).mean()
a5_1=a4.groupby(['month','day'],as_index=False).std()
a6=a5.iloc[:,2:]
a6_1=a5_1.iloc[:,2:]
a7=a6+(2*a6_1)
a8=a6-(2*a6_1)
a9=pd.merge(a7,a5.iloc[:,:2], left_index=True, right_index=True,how='left') 
a10=pd.merge(a8,a5.iloc[:,:2], left_index=True, right_index=True,how='left') 
a11=a9.iloc[:,:167]
a12=a10.iloc[:,:167]
#index가 있으면 비교구문에서 에러발생하여 다음 구문 실행
a13=a11.reset_index(drop=True,inplace=False)#366일평년상한(2.29포함)
a14=a12.reset_index(drop=True,inplace=False)#366일평년하한(2.29포함)

da=a9[(a9['month']==2)&(a9['day']==29)].index
a15=a9.drop(da,axis=0) 
a16=a10.drop(da,axis=0)
a17=a15.iloc[:,:167]
a18=a16.iloc[:,:167]
a19=a17.reset_index(drop=True,inplace=False)#365일평년상한(2.29제외)
a20=a18.reset_index(drop=True,inplace=False)#365일평년하한(2.29제외)

aa1=list()
for m in range(0,30):
    g1=a1[m].reset_index(drop=True, inplace=False).iloc[:,:167]
    if len(g1)==365:
        g2=(g1>a19)|(g1<a20)
        g3=pd.merge(g2,a5.iloc[:,:2], left_index=True, right_index=True,how='left')
        aa1.append(g3)
    else:
        g2=(g1>a13)|(g1<a14)
        g3=pd.merge(g2,a5.iloc[:,:2], left_index=True, right_index=True,how='left')
        aa1.append(g3)

aa2=aa1[0]
for k in range(1,30):
    aa2=pd.concat([aa1[k],aa2], axis=0)

aa3=aa2.groupby(['month','day'],as_index=False).mean()
aa4=aa3.iloc[:,2:]
aa5=aa4.sum()
aa5=pd.Series(aa5,name='extavg30')
aa5.index
aa5.to_csv("./extreme/extavg30.csv", index = True, encoding='cp949')
aa6=aa5.mean()

aa1hi=list()
for m in range(0,30):
    g1=a1[m].reset_index(drop=True, inplace=False).iloc[:,:167]
    if len(g1)==365:
        g2=(g1>a19)
        g3=pd.merge(g2,a5.iloc[:,:2], left_index=True, right_index=True,how='left')
        aa1hi.append(g3)
    else:
        g2=(g1>a13)
        g3=pd.merge(g2,a5.iloc[:,:2], left_index=True, right_index=True,how='left')
        aa1hi.append(g3)

aa2hi=aa1hi[0]
for k in range(1,30):
    aa2hi=pd.concat([aa1hi[k],aa2hi], axis=0)


aa3hi=aa2hi.groupby(['month','day'],as_index=False).mean()
aa4hi=aa3hi.iloc[:,2:]
aa5hi=aa4hi.sum()
aa5hi=pd.Series(aa5hi,name='extavg30hi')
aa5hi.index
aa5hi.to_csv("./extreme/extavg30hi.csv", index = True, encoding='cp949')
aa6hi=aa5hi.mean()

aa1lo=list()
for m in range(0,30):
    g1=a1[m].reset_index(drop=True, inplace=False).iloc[:,:167]
    if len(g1)==365:
        g2=(g1<a20)
        g3=pd.merge(g2,a5.iloc[:,:2], left_index=True, right_index=True,how='left')
        aa1lo.append(g3)
    else:
        g2=(g1<a14)
        g3=pd.merge(g2,a5.iloc[:,:2], left_index=True, right_index=True,how='left')
        aa1lo.append(g3)

aa2lo=aa1lo[0]
for k in range(1,30):
    aa2lo=pd.concat([aa1lo[k],aa2lo], axis=0)

aa3lo=aa2lo.groupby(['month','day'],as_index=False).mean()
aa4lo=aa3lo.iloc[:,2:]
aa5lo=aa4lo.sum()
aa5lo=pd.Series(aa5lo,name='extavg30lo')
aa5lo.index
aa5lo.to_csv("./extreme/extavg30lo.csv", index = True, encoding='cp949')
aa6lo=aa5lo.mean()

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,aa5, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('extavg30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='extavg30',cmap="jet", ax=ax,legend=True,cax=cax, vmax=70, vmin=10, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./extreme/extavg30.png')
plt.show()

#############이상기후 평균기온 2021년#############################################################################################
a21=pd.read_csv("D:/climatechange/data/tavg_10davg_mask_farmland/2021/tavg_10davg_mask_farmland.2021.csv",encoding='cp949')
a21=a21.transpose()
a21.rename(columns=a21.iloc[0],inplace=True)
a21=a21.iloc[1:,:]
a21['date']=pd.to_datetime(a21.index)
a21.set_index('date',inplace=True)
a21['month']=a21.index[0:len(a21.index)].month
a21['day']=a21.index[0:len(a21.index)].day
a31=a21.reset_index(drop=True,inplace=False)
a41=a31.iloc[:,:-2]
a41_1=a41.reset_index(drop=True,inplace=False)

if len(a41_1)==365: #고온저온 합
    a51=(a41_1>a19)|(a41_1<a20)
else:
    a51=(a41_1>a13)|(a41_1<a14)

if len(a41_1)==365: #고온
    a51_1=(a41_1>a19)
else:
    a51_1=(a41_1>a13)

if len(a41_1)==365: #저온
    a51_2=(a41_1<a20)
else:
    a51_2=(a41_1<a14)

a61=a51.sum()#시군별통계
a61
a61=pd.Series(a61,name='extavg')
a61.index
a71=a61.mean()#전국통계
a61.to_csv("./extreme/extavg2021.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,a61, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('extavg2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='extavg', cmap="jet",ax=ax,legend=True,cax=cax, vmax=70, vmin=10, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./extreme/extavg2021.png')
plt.show()

a81=a71-aa5
a81=pd.Series(a81,name='extavgdiff')
a81.index
a91=a81.mean()#전국통계
#a91.to_csv("./extreme/a91.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,a81, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('extavgdiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='extavgdiff',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=20, vmin=10, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./extreme/extavgdiff2021.png')
plt.show()

hitempdiff=a51_1-aa6hi
lotempdiff=a51_2-aa6lo
#############이상기후 강수량 평년################################################################################################3
b=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/prcp_10davg_mask_farmland/%d/prcp_10davg_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    b.append(f)

b1=list()
for j in range(0,30):
    f1=b[j].transpose()
    f1.rename(columns=f1.iloc[0],inplace=True)
    f1=f1.iloc[1:,:]
    f1['date']=pd.to_datetime(f1.index)
    f1.set_index('date',inplace=True)
    b1.append(f1)

b1[0]['month']=b1[0].index[0:len(b1[0].index)].month
b1[0]['day']=b1[0].index[0:len(b1[0].index)].day
b2=b1[0]

for k in range(1,30):
    b1[k]['month']=b1[k].index[0:len(b1[k].index)].month
    b1[k]['day']=b1[k].index[0:len(b1[k].index)].day
    b2=pd.concat([b1[k],b2], axis=0)

b3=b2.reset_index()
b4=b3.iloc[:,1:]

b5=list()
b6=[1,3,5,7,8,10,12]
i=0
for m in range(1,13):
    if m in b6:
        for n in range(1,32):
            bb=b4.groupby(['month','day'],as_index=False).get_group((m,n))
            b5.append(bb)
            i=i+1
    elif m == 2:
        for n in range(1,30):
            bb=b4.groupby(['month','day'],as_index=False).get_group((m,n))
            b5.append(bb)
            i=i+1
    else:
        for n in range(1,31):
            bb=b4.groupby(['month','day'],as_index=False).get_group((m,n))
            b5.append(bb)
            i=i+1

#b5[0].max(axis=0)
b7=list()
for o in range(0,366):
    h1=b5[o].iloc[:,0].sort_values(ascending=False)
    for p in range(1,169):
        g1=b5[o].iloc[:,p].sort_values(ascending=False)
        h1=pd.concat([h1,g1],axis=1)
    b7.append(h1)

b8=b7[0].iloc[1,:]
for q in range(1,366):
    if q != 59:
        b9=b7[q].iloc[1,:]
        b8=pd.concat([b8,b9],axis=1)
    else:
        b9=b7[q].iloc[0,:]
        b8=pd.concat([b8,b9],axis=1)

b10=b8.transpose()
b11=b10.reset_index(drop=True,inplace=False).iloc[:,:-2]
b11 #상위 퍼센타일 기준(2.29포함)
b11_1=b11.drop([59],axis=0).reset_index(drop=True,inplace=False)#상위 퍼센타일 기준(2.29제외)
b10
b12=b7[0].iloc[28,:]
for r in range(1,366):
    if r != 59:
        b13=b7[r].iloc[28,:]
        b12=pd.concat([b12,b13],axis=1)
    else:
        b13=b7[r].iloc[5,:]
        b12=pd.concat([b12,b13],axis=1)

b14=b12.transpose()
b15=b14.reset_index(drop=True,inplace=False).iloc[:,:-2]
b15 #하위 퍼센타일 기준(2.29포함)
b15_1=b15.drop([59],axis=0).reset_index(drop=True,inplace=False)#하위 퍼센타일 기준(2.29제외)

b16=(b11==b11)|(b15==b15)
b16_1=(b11==b11)
b16_2=(b15==b15)

b17=b16.sum()/30*2*2 #시군별통계
b17_1=b16_1.sum()/30*2
b18_1=b17_1.mean()
b17_2=b16_2.sum()/30*2
b18_2=b17_2.mean()
b17=pd.Series(b17,name='exrain30')
b17.index
b17.to_csv("./extreme/exrain30.csv", index = True, encoding='cp949')
b17_1.to_csv("./extreme/exrain30hi.csv", index = True, encoding='cp949')
b17_2.to_csv("./extreme/exrain30lo.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

exrainsigun=pd.merge(sigun3,b17, left_index=True, right_index=True,how='left')
exrainsigun.head()
exraingeo=gpd.GeoDataFrame(exrainsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('exrain30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
exraingeo.plot(column='exrain30',cmap="jet",ax=ax,legend=True,cax=cax, vmax=200, vmin=20, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./extreme/exrain30.png')
plt.show()

####################이상기후 강수량 2021년##################################################################################
e1=pd.read_csv("D:/climatechange/data/prcp_10davg_mask_farmland/2021/prcp_10davg_mask_farmland.2021.csv",encoding='cp949')
e2=e1.transpose()
e2.rename(columns=e2.iloc[0],inplace=True)
e2=e2.iloc[1:,:]
e2['date']=pd.to_datetime(e2.index)
e2.set_index('date',inplace=True)
e2['month']=e2.index[0:len(e2.index)].month
e2['day']=e2.index[0:len(e2.index)].day
e3=e2.reset_index(drop=True,inplace=False)
e4=e3.iloc[:,:-2]
e4_1=e4.reset_index(drop=True,inplace=False)

if len(e4_1)==365: #과우다우 합
    e5=(e4_1>b11_1)|(e4_1<b15_1)
else:
    e5=(e4_1>b11)|(e4_1<b15)

if len(e4_1)==365: #다우
    e5_1=(e4_1>b11_1)
else:
    e5_1=(e4_1>b11)

if len(e4_1)==365: #과우
    e5_2=(e4_1<b15_1)
else:
    e5_2=(e4_1<b15)
e6=e5.sum()#시군별통계
e6
e6_1=e5_1.sum()
e6_2=e5_2.sum()
e7_1=e6_1.mean()
e7_2=e6_2.mean()
e6=pd.Series(e6,name='exrain2021')
e6.index
e7=e6.mean()#전국통계
e6.to_csv("./extreme/exrain2021.csv", index = True, encoding='cp949')
e6_1.to_csv("./extreme/exrain2021hi.csv", index = True, encoding='cp949')
e6_2.to_csv("./extreme/exrain2021lo.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

exrainsigun=pd.merge(sigun3,e6, left_index=True, right_index=True,how='left')
exrainsigun.head()
exraingeo=gpd.GeoDataFrame(exrainsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('exrain2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
exraingeo.plot(column='exrain2021',cmap="jet",ax=ax,legend=True,cax=cax, vmax=200, vmin=20, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./extreme/exrain2021.png')
plt.show()

b81=e6-b17
b81=pd.Series(b81,name='exraindiff')
b81.index
b91=b81.mean()#전국통계
b81.to_csv("./extreme/exraindiff2021.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,b81, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='exraindiff',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=160, vmin=-10, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.title('exraindiff2021')
plt.savefig('./extreme/exraindiff2021.png')
plt.show()

hiraindiff=e7_1-b18_1
loraindiff=e7_2-b18_2

##############################이상기후 일조시간 평년#########################################################################33
s=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/sunshine_10davg_mask_farmland/%d/sunshine_10davg_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    s.append(f)

s1=list()
for j in range(0,30):
    f1=s[j].transpose()
    f1.rename(columns=f1.iloc[0],inplace=True)
    f1=f1.iloc[1:,:]
    f1['date']=pd.to_datetime(f1.index)
    f1.set_index('date',inplace=True)
    s1.append(f1)

s1[0]['month']=s1[0].index[0:len(s1[0].index)].month
s1[0]['day']=s1[0].index[0:len(s1[0].index)].day
s2=s1[0]

for k in range(1,30):
    s1[k]['month']=s1[k].index[0:len(s1[k].index)].month
    s1[k]['day']=s1[k].index[0:len(s1[k].index)].day
    s2=pd.concat([s1[k],s2], axis=0)

s3=s2.reset_index()
s4=pd.concat([s3.iloc[:,1:-2]/60,s3.iloc[:,168:]], axis=1)
s5=s4.groupby(['month','day'],as_index=False).mean()
s5_1=s4.groupby(['month','day'],as_index=False).std()
s6=s5.iloc[:,2:]
s6_1=s5_1.iloc[:,2:]
s7=s6+(2*s6_1)
s8=s6-(2*s6_1)
s9=pd.merge(s7,s5.iloc[:,:2], left_index=True, right_index=True,how='left') 
s10=pd.merge(s8,s5.iloc[:,:2], left_index=True, right_index=True,how='left') 
s11=s9.iloc[:,:167]
s12=s10.iloc[:,:167]
#index가 있으면 비교구문에서 에러발생하여 다음 구문 실행
s13=s11.reset_index(drop=True,inplace=False)#366일평년상한(2.29포함)
s14=s12.reset_index(drop=True,inplace=False)#366일평년하한(2.29포함)

ds=s9[(s9['month']==2)&(s9['day']==29)].index
s15=s9.drop(ds,axis=0) 
s16=s10.drop(ds,axis=0)
s17=s15.iloc[:,:167]
s18=s16.iloc[:,:167]
s19=s17.reset_index(drop=True,inplace=False)#365일평년상한(2.29제외)
s20=s18.reset_index(drop=True,inplace=False)#365일평년하한(2.29제외)

ss1=list()
for m in range(0,30):
    t1=s1[m].reset_index(drop=True, inplace=False).iloc[:,:167]/60
    if len(t1)==365:
        t2=(t1>s19)|(t1<s20)
        t3=pd.merge(t2,s5.iloc[:,:2], left_index=True, right_index=True,how='left')
        ss1.append(t3)
    else:
        t2=(t1>s13)|(t1<s14)
        t3=pd.merge(t2,s5.iloc[:,:2], left_index=True, right_index=True,how='left')
        ss1.append(t3)

ss2=ss1[0]
for k in range(1,30):
    ss2=pd.concat([ss1[k],ss2], axis=0)

ss3=ss2.groupby(['month','day'],as_index=False).mean()
ss4=ss3.iloc[:,2:]
ss5=ss4.sum()
ss5=pd.Series(ss5,name='exsun30')
ss5.index
ss6=ss5.mean()
ss5.to_csv("./extreme/exsun30.csv", index = True, encoding='cp949')

ss1hi=list()
for m in range(0,30):
    t1=s1[m].reset_index(drop=True, inplace=False).iloc[:,:167]/60
    if len(t1)==365:
        t2=(t1>s19)
        t3=pd.merge(t2,s5.iloc[:,:2], left_index=True, right_index=True,how='left')
        ss1hi.append(t3)
    else:
        t2=(t1>s13)
        t3=pd.merge(t2,s5.iloc[:,:2], left_index=True, right_index=True,how='left')
        ss1hi.append(t3)

ss2hi=ss1hi[0]
for k in range(1,30):
    ss2hi=pd.concat([ss1hi[k],ss2hi], axis=0)

ss3hi=ss2hi.groupby(['month','day'],as_index=False).mean()
ss4hi=ss3hi.iloc[:,2:]
ss5hi=ss4hi.sum()
ss5hi=pd.Series(ss5hi,name='exsun30hi')
ss5hi.index
ss6hi=ss5hi.mean()
ss5hi.to_csv("./extreme/exsun30hi.csv", index = True, encoding='cp949')

ss1lo=list()
for m in range(0,30):
    t1=s1[m].reset_index(drop=True, inplace=False).iloc[:,:167]/60
    if len(t1)==365:
        t2=(t1<s20)
        t3=pd.merge(t2,s5.iloc[:,:2], left_index=True, right_index=True,how='left')
        ss1lo.append(t3)
    else:
        t2=(t1<s14)
        t3=pd.merge(t2,s5.iloc[:,:2], left_index=True, right_index=True,how='left')
        ss1lo.append(t3)

ss2lo=ss1lo[0]
for k in range(1,30):
    ss2lo=pd.concat([ss1lo[k],ss2lo], axis=0)

ss3lo=ss2lo.groupby(['month','day'],as_index=False).mean()
ss4lo=ss3lo.iloc[:,2:]
ss5lo=ss4lo.sum()
ss5lo=pd.Series(ss5lo,name='exsun30lo')
ss5lo.index
ss6lo=ss5lo.mean()
ss5lo.to_csv("./extreme/exsun30lo.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,ss5, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('exsun30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='exsun30',cmap="YlOrRd", ax=ax,legend=True,cax=cax, vmax=30, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./extreme/exsun30.png')
plt.show()

#############이상기후 일조시간 2021년#############################################################################################
s21=pd.read_csv("D:/climatechange/data/sunshine_10davg_mask_farmland/2021/sunshine_10davg_mask_farmland.2021.csv",encoding='cp949')
s21=s21.transpose()
s21.rename(columns=s21.iloc[0],inplace=True)
s21=s21.iloc[1:,:]
s21['date']=pd.to_datetime(s21.index)
s21.set_index('date',inplace=True)
s21['month']=s21.index[0:len(s21.index)].month
s21['day']=s21.index[0:len(s21.index)].day
s31=s21.reset_index(drop=True,inplace=False)
s41=s31.iloc[:,:-2]/60
s41_1=s41.reset_index(drop=True,inplace=False)

if len(s41_1)==365: #고온저온 합
    s51=(s41_1>s19)|(s41_1<s20)
else:
    s51=(s41_1>s13)|(s41_1<s14)
    
if len(s41_1)==365: #고온
    s51_1=(s41_1>s19)
else:
    s51_1=(s41_1>s13)

if len(s41_1)==365: #저온
    s51_2=(s41_1<s20)
else:
    s51_2=(s41_1<s14)

s61=s51.sum()#시군별통계
s61_1=s51_1.sum()
s61_2=s51_2.sum()
s61=pd.Series(s61,name='exsun2021')
s61.index
s71=s61.mean()#전국통계
s61.to_csv("./extreme/exsun2021.csv", index = True, encoding='cp949')
s61_1.to_csv("./extreme/exsun2021hi.csv", index = True, encoding='cp949')
s61_2.to_csv("./extreme/exsun2021lo.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,s61, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('exsun2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='exsun2021',cmap="YlOrRd",ax=ax,legend=True,cax=cax, vmax=30, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./extreme/exsun2021.png')
plt.show()

s81=s71-ss5
s81=pd.Series(s81,name='exsundiff')
s81.index
s91=s81.mean()#전국통계
s81.to_csv("./extreme/exsundiff2021.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
 
tempsigun=pd.merge(sigun3,s81, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('exsundiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='exsundiff',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=5, vmin=-5, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Day",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./extreme/exsundiff2021.png')
plt.show()

hisundiff=s51_1-ss6hi
losundiff=s51_2-ss6lo

exdata={‘hitemp’:[a51_1, aa6hi, hitempdiff], ‘lotemp’:[a51_2, aa6lo, lotempdiff], ‘hirain’:[e7_1, b18_1, hiraindiff],‘lorain’:[e7_2, b18_2, loraindiff], ‘hisun’:[s51_1, ss6hi, hisundiff], ‘losun’:[s51_2, ss6lo, losundiff]}
exdatafr=DataFrame(exdata)
exdatafr.to_csv("./extreme/exdatafr2021.csv", index = True, encoding='cp949')