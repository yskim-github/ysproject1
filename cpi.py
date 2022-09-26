import csv
import pandas as pd
import datetime
import geopandas as gpd
import matplotlib.pyplot as plt
import mapclassify
from mpl_toolkits.axes_grid1 import make_axes_locatable

###############평년조생종################################################################################################
cpi2=pd.DataFrame()
for i in range(1991,2021):
    a1=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/%d/tavg_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    b1=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/%d/sunshine_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    a2=pd.concat([a1.iloc[:,0],a1.iloc[:,3:]],axis=1)
    a3=a2.transpose()
    a3.rename(columns=a3.iloc[0],inplace=True)
    a4=a3.iloc[1:,:]
    b2=pd.concat([b1.iloc[:,0],b1.iloc[:,3:]],axis=1)
    b3=b2.transpose()
    b3.rename(columns=b3.iloc[0],inplace=True)
    b4=b3.iloc[1:,:]
    a4['date']=pd.to_datetime(a4.index)
    a4.set_index('date',inplace=True)
    b4['date']=pd.to_datetime(b4.index)
    b4.set_index('date',inplace=True)

    day=datetime.datetime(i,8,5)#조생종
    day2=day+datetime.timedelta(days=40)
    a5=a4.loc[day:day2].mean()
    b5=pd.to_numeric(b4.loc[day:day2].sum()/60)
    aa=4.383/1000
    bb=-1.953/100000
    cc=21.9
    cpi1=b5*(aa-bb*pow((a5-cc),2))
    cpi1=pd.Series(cpi1,name='%d' %i)
    cpi2=pd.concat([cpi2,cpi1], axis=1)

cpi3=cpi2.mean(axis='columns')
cpi4=pd.Series(cpi3,name='cpiearly30')
cpi4.to_csv("./cpi/cpiearly30.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
cpisigun=pd.merge(sigun3,cpi4, left_index=True, right_index=True,how='left')
cpigeo=gpd.GeoDataFrame(cpisigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpiearly30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeo.plot(column='cpiearly30',cmap="jet",ax=ax,legend=True,cax=cax, vmax=2, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpiearly30.png')
plt.show()

##########################조생종2021###################################################################################
a1=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/2021/tavg_mask_farmland.2021.csv",encoding='cp949')
b1=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/2021/sunshine_mask_farmland.2021.csv",encoding='cp949')
a2=pd.concat([a1.iloc[:,0],a1.iloc[:,3:]],axis=1)
a3=a2.transpose()
a3.rename(columns=a3.iloc[0],inplace=True)
a4=a3.iloc[1:,:]
b2=pd.concat([b1.iloc[:,0],b1.iloc[:,3:]],axis=1)
b3=b2.transpose()
b3.rename(columns=b3.iloc[0],inplace=True)
b4=b3.iloc[1:,:]
a4['date']=pd.to_datetime(a4.index)
a4.set_index('date',inplace=True)
b4['date']=pd.to_datetime(b4.index)
b4.set_index('date',inplace=True)

day=datetime.datetime(2021,8,5)#조생종
#daym=datetime.datetime(2021,8,15)#중생종
#day=datetime.datetime(2021,8,25)#만생종
day2=day+datetime.timedelta(days=40)
a5=a4.loc[day:day2].mean()
b5=pd.to_numeric(b4.loc[day:day2].sum()/60)
#b5=pd.to_numeric(b4.loc[day:day2].sum())
aa=4.383/1000
bb=-1.953/100000
cc=21.9
#aa=0.187
#bb=0.0034
#cc=22.75
acpi1=b5*(aa-bb*pow((a5-cc),2))
acpi1.head()
acpi1.columns=['SIGUNGU_NM','CPI']
print(acpi1.columns)

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
acpi2=pd.Series(acpi1,name='cpiearly2021')
acpi2
acpi2.to_csv("./cpi/cpiearly2021.csv", index = True, encoding='cp949')
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
cpisigun=pd.merge(sigun3,acpi2, left_index=True, right_index=True,how='left')
cpisigun.head()
cpigeo=gpd.GeoDataFrame(cpisigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpiearly2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeo.plot(column='cpiearly2021',cmap="jet",ax=ax,legend=True,cax=cax, vmax=2, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpiearly2021.png')
plt.show()

cpiearlydiff=acpi2-cpi4
acpi2d=pd.Series(cpiearlydiff,name='cpiearlydiff')
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
acpi2d.to_csv("./cpi/cpiearlydiff.csv", index = True, encoding='cp949')
cpisigun=pd.merge(sigun3,acpi2d, left_index=True, right_index=True,how='left')
cpisigun.head()
cpigeo=gpd.GeoDataFrame(cpisigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpiearlydiff')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeo.plot(column='cpiearlydiff',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=1, vmin=-1, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpiearlydiff.png')
plt.show()


###############평년중생종################################################################################################
cpi2m=pd.DataFrame()
for i in range(1991,2021):
    a1=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/%d/tavg_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    b1=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/%d/sunshine_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    a2=pd.concat([a1.iloc[:,0],a1.iloc[:,3:]],axis=1)
    a3=a2.transpose()
    a3.rename(columns=a3.iloc[0],inplace=True)
    a4=a3.iloc[1:,:]
    b2=pd.concat([b1.iloc[:,0],b1.iloc[:,3:]],axis=1)
    b3=b2.transpose()
    b3.rename(columns=b3.iloc[0],inplace=True)
    b4=b3.iloc[1:,:]
    a4['date']=pd.to_datetime(a4.index)
    a4.set_index('date',inplace=True)
    b4['date']=pd.to_datetime(b4.index)
    b4.set_index('date',inplace=True)

    daym=datetime.datetime(i,8,15)#중생종
    day2m=daym+datetime.timedelta(days=40)
    a5m=a4.loc[daym:day2m].mean()
    b5m=pd.to_numeric(b4.loc[daym:day2m].sum()/60)
    aa=4.383/1000
    bb=-1.953/100000
    cc=21.9
    cpi1m=b5m*(aa-bb*pow((a5m-cc),2))
    cpi1m=pd.Series(cpi1m,name='%d' %i)
    cpi2m=pd.concat([cpi2m,cpi1m], axis=1)

cpi3m=cpi2m.mean(axis='columns')
cpi4m=pd.Series(cpi3m,name='cpimedian30')
cpi4m.to_csv("./cpi/cpimedian30.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
cpisigun=pd.merge(sigun3,cpi4m, left_index=True, right_index=True,how='left')
cpigeo=gpd.GeoDataFrame(cpisigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpimedian30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeo.plot(column='cpimedian30',cmap="jet",ax=ax,legend=True,cax=cax, vmax=2, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpimedian30.png')
plt.show()

###########################중생종2021###################################################################################
a1=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/2021/tavg_mask_farmland.2021.csv",encoding='cp949')
b1=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/2021/sunshine_mask_farmland.2021.csv",encoding='cp949')
a2=pd.concat([a1.iloc[:,0],a1.iloc[:,3:]],axis=1)
a3=a2.transpose()
a3.rename(columns=a3.iloc[0],inplace=True)
a4=a3.iloc[1:,:]
b2=pd.concat([b1.iloc[:,0],b1.iloc[:,3:]],axis=1)
b3=b2.transpose()
b3.rename(columns=b3.iloc[0],inplace=True)
b4=b3.iloc[1:,:]
a4['date']=pd.to_datetime(a4.index)
a4.set_index('date',inplace=True)
b4['date']=pd.to_datetime(b4.index)
b4.set_index('date',inplace=True)

#day=datetime.datetime(2021,8,5)#조생종
daym=datetime.datetime(2021,8,15)#중생종
#day=datetime.datetime(2021,8,25)#만생종
day2m=daym+datetime.timedelta(days=40)
a5m=a4.loc[daym:day2m].mean()
b5m=pd.to_numeric(b4.loc[daym:day2m].sum()/60)

aa=4.383/1000
bb=-1.953/100000
cc=21.9
#aa=0.187
#bb=0.0034
#cc=22.75
acpi1m=b5m*(aa-bb*pow((a5m-cc),2))
acpi1m.head()
acpi1m.columns=['SIGUNGU_NM','CPI']
print(acpi1m.columns)
sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2m=pd.DataFrame(sigun)
acpi2m=pd.Series(cpi1m,name='cpimedian2021')
acpi2m.index
acpi2m.to_csv("./cpi/cpimedian2021.csv", index = True, encoding='cp949')
sigun3m=sigun2m.set_index('SIGUNGU_NM',append=False)
sigun3m.index
cpisigunm=pd.merge(sigun3m,acpi2m, left_index=True, right_index=True,how='left')
cpisigunm.head()
cpigeom=gpd.GeoDataFrame(cpisigunm)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpimedian2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeom.plot(column='cpimedian2021',cmap="jet",ax=ax,legend=True,cax=cax, vmax=2, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpimedian2021.png')
plt.show()

cpimediandiff=acpi2m-cpi4m
acpi2md=pd.Series(cpimediandiff,name='cpimediandiff')
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
acpi2md.to_csv("./cpi/cpimediandiff.csv", index = True, encoding='cp949')
cpisigun=pd.merge(sigun3,acpi2md, left_index=True, right_index=True,how='left')
cpisigun.head()
cpigeo=gpd.GeoDataFrame(cpisigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpimediandiff')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeo.plot(column='cpimediandiff',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=1, vmin=-1, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpimediandiff.png')
plt.show()

###############평년중만생종################################################################################################
cpi2l=pd.DataFrame()
for i in range(1991,2021):
    a1=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/%d/tavg_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    b1=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/%d/sunshine_mask_farmland.%d.csv" %(i,i),encoding='cp949')
    a2=pd.concat([a1.iloc[:,0],a1.iloc[:,3:]],axis=1)
    a3=a2.transpose()
    a3.rename(columns=a3.iloc[0],inplace=True)
    a4=a3.iloc[1:,:]
    b2=pd.concat([b1.iloc[:,0],b1.iloc[:,3:]],axis=1)
    b3=b2.transpose()
    b3.rename(columns=b3.iloc[0],inplace=True)
    b4=b3.iloc[1:,:]
    a4['date']=pd.to_datetime(a4.index)
    a4.set_index('date',inplace=True)
    b4['date']=pd.to_datetime(b4.index)
    b4.set_index('date',inplace=True)

    dayl=datetime.datetime(i,8,25)#중만생종
    day2l=dayl+datetime.timedelta(days=40)
    a5l=a4.loc[dayl:day2l].mean()
    b5l=pd.to_numeric(b4.loc[dayl:day2l].sum()/60)
    aa=4.383/1000
    bb=-1.953/100000
    cc=21.9
    cpi1l=b5l*(aa-bb*pow((a5l-cc),2))
    cpi1l=pd.Series(cpi1l,name='%d' %i)
    cpi2l=pd.concat([cpi2l,cpi1l], axis=1)

cpi3l=cpi2l.mean(axis='columns')
cpi4l=pd.Series(cpi3l,name='cpilate30')
cpi4l.to_csv("./cpi/cpilate30.csv", index = True, encoding='cp949')

sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2=pd.DataFrame(sigun)
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
cpisigun=pd.merge(sigun3,cpi4l, left_index=True, right_index=True,how='left')
cpigeo=gpd.GeoDataFrame(cpisigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpilate30')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeo.plot(column='cpilate30',cmap="jet",ax=ax,legend=True,cax=cax, vmax=2, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpilate30.png')
plt.show()

##############################중만생종2021##################################################################################
a1=pd.read_csv("D:/climatechange/data/tavg_mask_farmland/2021/tavg_mask_farmland.2021.csv",encoding='cp949')
b1=pd.read_csv("D:/climatechange/data/sunshine_mask_farmland/2021/sunshine_mask_farmland.2021.csv",encoding='cp949')
a2=pd.concat([a1.iloc[:,0],a1.iloc[:,3:]],axis=1)
a3=a2.transpose()
a3.rename(columns=a3.iloc[0],inplace=True)
a4=a3.iloc[1:,:]
b2=pd.concat([b1.iloc[:,0],b1.iloc[:,3:]],axis=1)
b3=b2.transpose()
b3.rename(columns=b3.iloc[0],inplace=True)
b4=b3.iloc[1:,:]
a4['date']=pd.to_datetime(a4.index)
a4.set_index('date',inplace=True)
b4['date']=pd.to_datetime(b4.index)
b4.set_index('date',inplace=True)

#day=datetime.datetime(2021,8,5)#조생종
#day=datetime.datetime(2021,8,15)#중생종
dayl=datetime.datetime(2021,8,25)#중만생종
day2l=dayl+datetime.timedelta(days=40)
a5l=a4.loc[dayl:day2l].mean()
b5l=pd.to_numeric(b4.loc[dayl:day2l].sum()/60)
#b5=pd.to_numeric(b4.loc[day:day2].sum())
aa=4.383/1000
bb=-1.953/100000
cc=21.9
#aa=0.187
#bb=0.0034
#cc=22.75
acpi1l=b5l*(aa-bb*pow((a5l-cc),2))
acpi1l.head()
acpi1l.columns=['SIGUNGU_NM','CPI']
print(acpi1l.columns)
sigun_f="sigungu_2016_proj_167.shp"
sigun=gpd.read_file(sigun_f)
sigun
sigun2l=pd.DataFrame(sigun)
acpi2l=pd.Series(acpi1l,name='cpilate2021')
acpi2l.index
acpi2l.to_csv("./cpi/cpilate2021.csv", index = True, encoding='cp949')
sigun3l=sigun2l.set_index('SIGUNGU_NM',append=False)
sigun3l.index
cpisigunl=pd.merge(sigun3l,acpi2l, left_index=True, right_index=True,how='left')
cpisigunl.head()
cpigeol=gpd.GeoDataFrame(cpisigunl)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpilate2021')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeol.plot(column='cpilate2021',cmap="jet",ax=ax,legend=True,cax=cax, vmax=2, vmin=0, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpilate2021.png')
plt.show()

cpilatediff=acpi2l-cpi4l
acpi2ld=pd.Series(cpilatediff,name='cpilatediff')
sigun3=sigun2.set_index('SIGUNGU_NM',append=False)
sigun3.index
acpi2ld.to_csv("./cpi/cpilatediff.csv", index = True, encoding='cp949')
cpisigun=pd.merge(sigun3,acpi2ld, left_index=True, right_index=True,how='left')
cpisigun.head()
cpigeo=gpd.GeoDataFrame(cpisigun)
fig, ax= plt.subplots(1,1)
divider=make_axes_locatable(ax)
plt.title('cpilatediff')
cax=divider.append_axes('bottom',size='5%', pad=0.5)
cpigeo.plot(column='cpilatediff',cmap="gnuplot",ax=ax,legend=True,cax=cax, vmax=1, vmin=-1, edgecolor='black', linewidth=0.1, legend_kwds={'label': "CPI",'orientation': "horizontal", 'fmt':"{:.2f}"})
plt.savefig('./cpi/cpilatediff.png')
plt.show()