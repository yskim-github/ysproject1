import csv
import pandas as pd
import datetime
import geopandas as gpd
import matplotlib.pyplot as plt
import mapclassify
from mpl_toolkits.axes_grid1 import make_axes_locatable

#########평균기온평년#############################################################################################
a=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/%d/tavg_mask_farmland.%d.csv" %(i,i),encoding='cp949')
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
a6=a5.iloc[:,2:]
a7=a6.mean()
a7=pd.Series(a7,name='tavg')
a7.index
a7.to_csv("./climate/tavg30.csv", index = True, encoding='cp949')
a8=a7.mean()
#a8.to_csv("./climate/tavg30total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,a7, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tavg30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='tavg', cmap="jet", ax=ax,legend=True,cax=cax, vmax=20, vmin=5, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/tavg30.png')
plt.show()

#########최고기온평년#############################################################################################
b=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/tmax_mask_farmland/%d/tmax_mask_farmland.%d.csv" %(i,i),encoding='cp949')
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
b5=b4.groupby(['month','day'],as_index=False).mean()
b6=b5.iloc[:,2:]
b7=b6.mean()
b7=pd.Series(b7,name='tmax')
b7.index
b7.to_csv("./climate/tmin30.csv", index = True, encoding='cp949')
b8=b7.mean()
#b8.to_csv("./climate/tmax30total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,b7, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tmax30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='tmax',cmap="jet",ax=ax,legend=True,cax=cax, vmax=25, vmin=10, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/tmax30.png')
plt.show()

#########최저기온평년#############################################################################################
c=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/tmin_mask_farmland/%d/tmin_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    c.append(f)

c1=list()
for j in range(0,30):
    f1=c[j].transpose()
    f1.rename(columns=f1.iloc[0],inplace=True)
    f1=f1.iloc[1:,:]
    f1['date']=pd.to_datetime(f1.index)
    f1.set_index('date',inplace=True)
    c1.append(f1)

c1[0]['month']=c1[0].index[0:len(c1[0].index)].month
c1[0]['day']=c1[0].index[0:len(c1[0].index)].day
c2=c1[0]

for k in range(1,30):
    c1[k]['month']=c1[k].index[0:len(c1[k].index)].month
    c1[k]['day']=c1[k].index[0:len(c1[k].index)].day
    c2=pd.concat([c1[k],c2], axis=0)

c3=c2.reset_index()
c4=c3.iloc[:,1:]
c5=c4.groupby(['month','day'],as_index=False).mean()
c6=c5.iloc[:,2:]
c7=c6.mean()
c7=pd.Series(c7,name='tmin')
c7.index
c7.to_csv("./climate/tmin30.csv", index = True, encoding='cp949')
c8=c7.mean()
#c8.to_csv("./climate/tmin30total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,c7, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tmin30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='tmin',cmap="jet",ax=ax,legend=True,cax=cax, vmax=15, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/tmin30.png')
plt.show()

#########강수량평년#############################################################################################
d=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/prcp_mask_farmland/%d/prcp_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    d.append(f)

d1=list()
for j in range(0,30):
    f1=d[j].transpose()
    f1.rename(columns=f1.iloc[0],inplace=True)
    f1=f1.iloc[1:,:]
    f1['date']=pd.to_datetime(f1.index)
    f1.set_index('date',inplace=True)
    d1.append(f1)

d1[0]['month']=d1[0].index[0:len(d1[0].index)].month
d1[0]['day']=d1[0].index[0:len(d1[0].index)].day
d2=d1[0]

for k in range(1,30):
    d1[k]['month']=d1[k].index[0:len(d1[k].index)].month
    d1[k]['day']=d1[k].index[0:len(d1[k].index)].day
    d2=pd.concat([d1[k],d2], axis=0)

d3=d2.reset_index()
d4=d3.iloc[:,1:]
d5=d4.groupby(['month','day'],as_index=False).mean()
d6=d5.iloc[:,2:]
d7=d6.sum()
d7=pd.Series(d7,name='rain30')
d7.index
d7.to_csv("./climate/rain30.csv", index = True, encoding='cp949')
d8=d7.mean()
#d8.to_csv("./climate/rain30total.csv", index = True, encoding='cp949')
d6
sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,d7, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('rain30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='rain30',cmap="Blues",ax=ax,legend=True,cax=cax, vmax=2500, vmin=1000, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Precipitation(mm)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/rain30.png')
plt.show()

#########일조시간평년#############################################################################################
e=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/%d/sunshine_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    e.append(f)

e1=list()
for j in range(0,30):
    f1=e[j].transpose()
    f1.rename(columns=f1.iloc[0],inplace=True)
    f1=f1.iloc[1:,:]
    f1['date']=pd.to_datetime(f1.index)
    f1.set_index('date',inplace=True)
    e1.append(f1)

e1[0]['month']=e1[0].index[0:len(e1[0].index)].month
e1[0]['day']=e1[0].index[0:len(e1[0].index)].day
e2=e1[0]

for k in range(1,30):
    e1[k]['month']=e1[k].index[0:len(e1[k].index)].month
    e1[k]['day']=e1[k].index[0:len(e1[k].index)].day
    e2=pd.concat([e1[k],e2], axis=0)

e3=e2.reset_index()
e4=e3.iloc[:,1:]
e5=e4.groupby(['month','day'],as_index=False).mean()/60
e6=e5.iloc[:,2:]
e7=e6.sum()
e7=pd.Series(e7,name='sun30')
e7.index
e7.to_csv("./climate/sun30.csv", index = True, encoding='cp949')
e8=e7.mean()
#e8.to_csv("./climate/sun30total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,e7, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('sun30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='sun30',cmap="YlOrRd",ax=ax,legend=True,cax=cax, vmax=2000, vmin=1000, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Sunshine(hr)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/sun30.png')
plt.show()

#########일사량평년#############################################################################################
h=list()
for i in range(1991,2021):
    f=pd.read_csv("D:/climatechange/data/ins_mask_farmland/%d/ins_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    h.append(f)

h1=list()
for j in range(0,30):
    f1=h[j].transpose()
    f1.rename(columns=f1.iloc[0],inplace=True)
    f1=f1.iloc[1:,:]
    f1['date']=pd.to_datetime(f1.index)
    f1.set_index('date',inplace=True)
    h1.append(f1)

h1[0]['month']=h1[0].index[0:len(h1[0].index)].month
h1[0]['day']=h1[0].index[0:len(h1[0].index)].day
h2=h1[0]

for k in range(1,30):
    h1[k]['month']=h1[k].index[0:len(h1[k].index)].month
    h1[k]['day']=h1[k].index[0:len(h1[k].index)].day
    h2=pd.concat([h1[k],h2], axis=0)

h3=h2.reset_index()
h4=h3.iloc[:,1:]
h5=h4.groupby(['month','day'],as_index=False).mean()
h6=h5.iloc[:,2:]
h7=h6.sum()
h7=pd.Series(h7,name='ins')
h7.index
h7.to_csv("./climate/ins30.csv", index = True, encoding='cp949')
h8=h7.mean()
#h8.to_csv("./climate/ins30total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,h7, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('ins30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='ins',cmap="YlOrRd",ax=ax,legend=True,cax=cax, vmax=6000, vmin=4000, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Insolation(MJ)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/ins30.png')
plt.show()

#############평균기온 2021년#############################################################################################
a21=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/2021/tavg_mask_farmland.2021.csv",encoding='cp949')
a21=a21.transpose()
a21.rename(columns=a21.iloc[0],inplace=True)
a21=a21.iloc[1:,:]
a21['date']=pd.to_datetime(a21.index)
a21.set_index('date',inplace=True)
a31=a21.reset_index(drop=True,inplace=False)
a41=a31.mean()
a51=pd.Series(a41,name='tavg2021')
a51.index
a51.to_csv("./climate/tavg2021.csv", index = True, encoding='cp949')
a61=a51.mean()
#a61.to_csv("./climate/tavg2021total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,a51, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tavg2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='tavg2021',cmap="jet",ax=ax,legend=True,cax=cax, vmax=20, vmin=5, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./climate/tavg2021.png')
plt.show()

a71=a51-a7
a71=pd.Series(a71,name='tavgdiff2021')
a71.index
a71.to_csv("./climate/tavgdiff2021.csv", index = True, encoding='cp949')
a81=a71.mean()#전국통계

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,a71, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tavgdiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='tavgdiff2021',cmap="gnuplot", ax=ax,legend=True,cax=cax, vmax=2, vmin=-2, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/tavgdiff2021.png')
plt.show()

#############최고기온 2021년#############################################################################################
b21=pd.read_csv("D:/climatechange/data/tmax_mask_farmland/2021/tmax_mask_farmland.2021.csv",encoding='cp949')
b21=b21.transpose()
b21.rename(columns=b21.iloc[0],inplace=True)
b21=b21.iloc[1:,:]
b21['date']=pd.to_datetime(b21.index)
b21.set_index('date',inplace=True)
b31=b21.reset_index(drop=True,inplace=False)
b41=b31.mean()
b51=pd.Series(b41,name='tmax2021')
b51.index
b51.to_csv("./climate/tmax2021.csv", index = True, encoding='cp949')
b61=b51.mean()
#b61.to_csv("./climate/tmax2021total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,b51, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tmax2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='tmax2021',cmap="jet", ax=ax,legend=True,cax=cax, vmax=25, vmin=10, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./climate/tmax2021.png')
plt.show()

b71=b51-b7
b71=pd.Series(b71,name='tmaxdiff2021')
b71.index
b71.to_csv("./climate/tmaxdiff2021.csv", index = True, encoding='cp949')
b81=b71.mean()#전국통계

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,b71, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tmaxdiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='tmaxdiff2021',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=2, vmin=-2, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/tmaxdiff2021.png')
plt.show()

#############최저기온 2021년#############################################################################################
c21=pd.read_csv("D:/climatechange/data/tmin_mask_farmland/2021/tmin_mask_farmland.2021.csv",encoding='cp949')
c21=c21.transpose()
c21.rename(columns=c21.iloc[0],inplace=True)
c21=c21.iloc[1:,:]
c21['date']=pd.to_datetime(c21.index)
c21.set_index('date',inplace=True)
c31=c21.reset_index(drop=True,inplace=False)
c41=c31.mean()
c51=pd.Series(c41,name='tmin2021')
c51.index
c51.to_csv("./climate/tmin2021.csv", index = True, encoding='cp949')
c61=c51.mean()
#c61.to_csv("./climate/tmin2021total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,c51, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tmin2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='tmin2021',cmap="jet",ax=ax,legend=True,cax=cax, vmax=15, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./climate/tmin2021.png')
plt.show()

c71=c51-c7
c71=pd.Series(c71,name='tmindiff2021')
c71.index
c71.to_csv("./climate/tmindiff2021.csv", index = True, encoding='cp949')
c81=c71.mean()#전국통계

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,c71, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('tmindiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='tmindiff2021',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=2, vmin=-2, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Temperature(\N{DEGREE SIGN}C)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/tmindiff2021.png')
plt.show()

#############강수량 2021년#############################################################################################
d21=pd.read_csv("D:/climatechange/data/prcp_mask_farmland/2021/prcp_mask_farmland.2021.csv",encoding='cp949')
d21=d21.transpose()
d21.rename(columns=d21.iloc[0],inplace=True)
d21=d21.iloc[1:,:]
d21['date']=pd.to_datetime(d21.index)
d21.set_index('date',inplace=True)
d31=d21.reset_index(drop=True,inplace=False)
d41=pd.to_numeric(d31.sum())
d51=pd.Series(d41,name='rain2021')
d51.index
d51.to_csv("./climate/rain2021.csv", index = True, encoding='cp949')
d61=d51.mean()
#d61.to_csv("./climate/rain2021total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,d51, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('rain2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='rain2021',cmap="Blues",ax=ax,legend=True,cax=cax, vmax=2500, vmin=1000, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Precipitation(mm)",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./climate/rain2021.png')
plt.show()

d71=d51-d7
d71=pd.Series(d71,name='raindiff2021')
d71.index
d71.to_csv("./climate/raindiff2021.csv", index = True, encoding='cp949')
d81=d71.mean()#전국통계

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,d71, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('raindiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='raindiff2021',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=200, vmin=-400, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Precipitation(mm)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/raindiff2021.png')
plt.show()

#############일조시간 2021년#############################################################################################
e21=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/2021/sunshine_mask_farmland.2021.csv",encoding='cp949')
e21=e21.transpose()
e21.rename(columns=e21.iloc[0],inplace=True)
e21=e21.iloc[1:,:]
e21['date']=pd.to_datetime(e21.index)
e21.set_index('date',inplace=True)
e31=e21.reset_index(drop=True,inplace=False)
e41=pd.to_numeric(e31.sum()/60)
e51=pd.Series(e41,name='sun2021')
e51.index
e51.to_csv("./climate/sun2021.csv", index = True, encoding='cp949')
e61=e51.mean()
#e61.to_csv("./climate/sun2021total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,e51, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('sun2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='sun2021',cmap="YlOrRd",ax=ax,legend=True,cax=cax, vmax=2000, vmin=1000, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Sunshine(hr)",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./climate/sun2021.png')
plt.show()

e71=e51-e7
e71=pd.Series(e71,name='sundiff2021')
e71.index
e71.to_csv("./climate/sundiff2021.csv", index = True, encoding='cp949')
e81=e71.mean()#전국통계

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,e71, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('sundiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='sundiff2021',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=400, vmin=-300, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Sunshine(hr)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/sundiff2021.png')
plt.show()

#############일사량 2021년#############################################################################################
h21=pd.read_csv("D:/climatechange/data/ins_mask_farmland/2021/ins_mask_farmland.2021.csv",encoding='cp949')
h21=h21.transpose()
h21.rename(columns=h21.iloc[0],inplace=True)
h21=h21.iloc[1:,:]
h21['date']=pd.to_datetime(h21.index)
h21.set_index('date',inplace=True)
h31=h21.reset_index(drop=True,inplace=False)
h41=pd.to_numeric(h31.sum())
h51=pd.Series(h41,name='ins2021')
h51.index
h51.to_csv("./climate/ins2021.csv", index = True, encoding='cp949')
h61=h51.mean()
#h61.to_csv("./climate/ins2021total.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

extavgsigun=pd.merge(sigun3,h51, left_index=True, right_index=True,how='left')
extavgsigun.head()
extavggeo=gpd.GeoDataFrame(extavgsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('ins2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
extavggeo.plot(column='ins2021',cmap="YlOrRd",ax=ax,legend=True,cax=cax, vmax=6000, vmin=4000, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Insolation(MJ)",'orientation': "horizontal", 'fmt':"{:.2f}"})
#vmax와 vmin을 이용해서 범례의 최대최소값 조정
plt.savefig('./climate/ins2021.png')
plt.show()

h71=h51-h7
h71=pd.Series(h71,name='insdiff2021')
h71.index
h71.to_csv("./climate/insdiff2021.csv", index = True, encoding='cp949')
h81=h71.mean()#전국통계

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index

tempsigun=pd.merge(sigun3,h71, left_index=True, right_index=True,how='left')
tempsigun.head()
tempgeo=gpd.GeoDataFrame(tempsigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('insdiff2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
tempgeo.plot(column='insdiff2021',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=700, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "Insolation(MJ)",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./climate/insdiff2021.png')
plt.show()

climatedata={‘tmin’:[c61, c8, c81], ‘tmax’:[b61, b8, b81], ‘tavg’:[a61, a8, a81],‘rain’:[d61, d8, d81], ‘sun’:[e61, e8, e81], ‘ins’:[h61, h8, h81]}
climatedatafr=DataFrame(climatedata)
climatedatafr.to_csv("./climate/climatedatafr2021.csv", index = True, encoding='cp949')