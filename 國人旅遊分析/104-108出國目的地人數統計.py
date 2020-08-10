# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 23:40:01 2020

@author: clementchi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#使得圖形化能夠顯示中文字
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
mpl.rcParams['axes.unicode_minus'] = False
import seaborn as sns
#載入104-108的CSV資料
df108 = pd.read_csv("108出國旅客按年齡統計.csv",encoding = "utf-8")
df107 = pd.read_csv("107出國旅客按年齡統計.csv",encoding = "utf-8")
df106 = pd.read_csv("106出國旅客按年齡統計.csv",encoding = "utf-8")
df105 = pd.read_csv("105出國旅客按年齡統計.csv",encoding = "utf-8")
df104 = pd.read_csv("104出國旅客按年齡統計.csv",encoding = "utf-8")
#去除不必要的資料
drop108 = df108.drop(df108.columns[0],axis=1)
drop108 = df108.drop(df108.index[184],axis=0)
drop107 = df107.drop(df108.columns[0],axis=1)
drop107 = df107.drop(df108.index[184],axis=0)
drop106 = df106.drop(df108.columns[0],axis=1)
drop106 = df106.drop(df108.index[184],axis=0)
drop105 = df105.drop(df108.columns[0],axis=1)
drop105 = df105.drop(df108.index[184],axis=0)
drop104 = df104.drop(df108.columns[0],axis=1)
drop104 = df104.drop(df108.index[184],axis=0)
#合併104-108的CSV資料並用'Year'當index
#File_merge = pd.concat([drop108, drop107, drop106, drop105, drop104], axis=0, join='inner')
#File_merge.set_index('Year', inplace=True)
#File_merge
#載入薪資資料
salary=pd.read_json('salary.json')
salary1=salary.drop('Year',axis=1)

#各年平均薪資
sax=['104','105','106','107','108']
say=salary['salary']
plt.figure(figsize=(8,6),facecolor='#9999ff')
plt.plot(sax,say,'bo-',color='red',label='薪水')
plt.xlabel("年")
plt.ylabel("薪水")
plt.title('104-105年薪水漲幅程度')
plt.ylim(48000,55000)
plt.legend(loc=2)

plt.show()
#取出各104-108熱門旅遊國家人數
drop108.sort_values(['Subtotals'], ascending=False).head(5)
drop107.sort_values(['Subtotals'], ascending=False).head(5)
drop106.sort_values(['Subtotals'], ascending=False).head(5)
drop105.sort_values(['Subtotals'], ascending=False).head(5)
drop104.sort_values(['Subtotals'], ascending=False).head(5)
#將Subtotals使其視覺化
plt.figure(figsize=(13,6))
head108 = drop108.sort_values(['Subtotals'], ascending=False).head(7)
sns.barplot(x='Countries',y='Subtotals',data=head108)
plt.title('108年')
plt.figure(figsize=(13,6))
head107 = drop107.sort_values(['Subtotals'], ascending=False).head(7)
sns.barplot(x='Countries',y='Subtotals',data=head107)
plt.title('107年')
plt.figure(figsize=(13,6))
head106 = drop106.sort_values(['Subtotals'], ascending=False).head(7)
sns.barplot(x='Countries',y='Subtotals',data=head106)
plt.title('106年')
plt.figure(figsize=(13,6))
head105 = drop105.sort_values(['Subtotals'], ascending=False).head(7)
sns.barplot(x='Countries',y='Subtotals',data=head105)
plt.title('105年')
plt.figure(figsize=(13,6))
head104 = drop105.sort_values(['Subtotals'], ascending=False).head(7)
sns.barplot(x='Countries',y='Subtotals',data=head104)
plt.title('104年')
plt.show()

#104-108篩選各年齡層出國目的地前五國家
yt10812 = drop108.sort_values(['1-12Years'], ascending=False).head(5)
yt10819 = drop108.sort_values(['13-19Years'], ascending=False).head(5)
yt10829 = drop108.sort_values(['20-29Years'], ascending=False).head(5)
yt10839 = drop108.sort_values(['30-39Years'], ascending=False).head(5)
yt10849 = drop108.sort_values(['40-49Years'], ascending=False).head(5)
yt10859 = drop108.sort_values(['50-59Years'], ascending=False).head(5)
yt10860 = drop108.sort_values(['60Years and Over'], ascending=False).head(5)
#各年齡層出國目的地視覺化
category = yt10812['Countries']                    # 製作圓餅圖的類別標籤
Value12 = yt10812["1-12Years"]                     # 製作圓餅圖的數值來源
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)                     
# Value12=數值
# labels =分類的標記
# autopct =四捨五入至小數點後面位數
# explode =設定分隔的區塊位置
# pctdistance =數值與圓餅圖的圓心距離
# radius =圓餅圖的半徑，預設是1
# center = 圓餅圖的圓心座標
# shadow=是否使用陰影
plt.legend(loc = "best")                       # 設定legnd的位置
plt.title("108年1-12歲前五大出國地", x=0.5, y=1.03)  # 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

category = yt10819['Countries']
Value12 = yt10819["13-19Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("108年13-19歲前五大出國地", x=0.5, y=1.03)

category = yt10829['Countries']
Value12 = yt10829["20-29Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("108年20-29歲前五大出國地", x=0.5, y=1.03)

category = yt10839['Countries']
Value12 = yt10839["30-39Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("108年30-39歲前五大出國地", x=0.5, y=1.03)

category = yt10849['Countries']
Value12 = yt10849["40-49Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("108年40-49歲前五大出國地", x=0.5, y=1.03)

category = yt10859['Countries']
Value12 = yt10859["50-59Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("108年50-59歲前五大出國地", x=0.5, y=1.03)

category = yt10860['Countries']
Value12 = yt10860["60Years and Over"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("108年60歲後五大出國地", x=0.5, y=1.03)
plt.show()

yt10712 = drop107.sort_values(['1-12Years'], ascending=False).head(5)
yt10719 = drop107.sort_values(['13-19Years'], ascending=False).head(5)
yt10729 = drop107.sort_values(['20-29Years'], ascending=False).head(5)
yt10739 = drop107.sort_values(['30-39Years'], ascending=False).head(5)
yt10749 = drop107.sort_values(['40-49Years'], ascending=False).head(5)
yt10759 = drop107.sort_values(['50-59Years'], ascending=False).head(5)
yt10760 = drop107.sort_values(['60Years and Over'], ascending=False).head(5)

category = yt10712['Countries']
Value12 = yt10712["1-12Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("107年1-12歲前五大出國地", x=0.5, y=1.03)

category = yt10712['Countries']
Value12 = yt10712["13-19Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("107年13-19歲前五大出國地", x=0.5, y=1.03)

category = yt10729['Countries']
Value12 = yt10729["20-29Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("107年20-29歲前五大出國地", x=0.5, y=1.03)

category = yt10739['Countries']
Value12 = yt10739["30-39Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("107年30-39歲前五大出國地", x=0.5, y=1.03)

category = yt10749['Countries']
Value12 = yt10749["40-49Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("107年40-49歲前五大出國地", x=0.5, y=1.03)

category = yt10759['Countries']
Value12 = yt10759["50-59Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("107年50-59歲前五大出國地", x=0.5, y=1.03)

category = yt10760['Countries']
Value12 = yt10760["60Years and Over"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("107年60歲後五大出國地", x=0.5, y=1.03)
plt.show()

yt10612 = drop106.sort_values(['1-12Years'], ascending=False).head(5)
yt10619 = drop106.sort_values(['13-19Years'], ascending=False).head(5)
yt10629 = drop106.sort_values(['20-29Years'], ascending=False).head(5)
yt10639 = drop106.sort_values(['30-39Years'], ascending=False).head(5)
yt10649 = drop106.sort_values(['40-49Years'], ascending=False).head(5)
yt10659 = drop106.sort_values(['50-59Years'], ascending=False).head(5)
yt10660 = drop106.sort_values(['60Years and Over'], ascending=False).head(5)

category = yt10612['Countries']
Value12 = yt10612["1-12Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("106年01-12歲前五大出國地", x=0.5, y=1.03)

category = yt10619['Countries']
Value12 = yt10619["13-19Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("106年13-19歲前五大出國地", x=0.5, y=1.03)

category = yt10629['Countries']
Value12 = yt10629["20-29Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("106年20-29歲前五大出國地", x=0.5, y=1.03)

category = yt10639['Countries']
Value12 = yt10639["30-39Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("106年30-39歲前五大出國地", x=0.5, y=1.03)

category = yt10649['Countries']
Value12 = yt10649["40-49Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("106年40-49歲前五大出國地", x=0.5, y=1.03)

category = yt10659['Countries']
Value12 = yt10659["50-59Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("106年50-59歲前五大出國地", x=0.5, y=1.03)

category = yt10660['Countries']
Value12 = yt10660["60Years and Over"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("106年60歲後五大出國地", x=0.5, y=1.03)
plt.show()

yt10512 = drop105.sort_values(['1-12Years'], ascending=False).head(5)
yt10519 = drop105.sort_values(['13-19Years'], ascending=False).head(5)
yt10529 = drop105.sort_values(['20-29Years'], ascending=False).head(5)
yt10539 = drop105.sort_values(['30-39Years'], ascending=False).head(5)
yt10549 = drop105.sort_values(['40-49Years'], ascending=False).head(5)
yt10559 = drop105.sort_values(['50-59Years'], ascending=False).head(5)
yt10560 = drop105.sort_values(['60Years and Over'], ascending=False).head(5)

category = yt10512['Countries']
Value12 = yt10512["1-12Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("105年1-12歲前五大出國地", x=0.5, y=1.03)

category = yt10519['Countries']
Value12 = yt10519["13-19Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("105年13-19歲前五大出國地", x=0.5, y=1.03)

category = yt10529['Countries']
Value12 = yt10529["20-29Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("105年20-29歲前五大出國地", x=0.5, y=1.03)

category = yt10539['Countries']
Value12 = yt10539["30-39Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("105年30-39歲前五大出國地", x=0.5, y=1.03)

category = yt10549['Countries']
Value12 = yt10549["40-49Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("105年40-49歲前五大出國地", x=0.5, y=1.03)

category = yt10559['Countries']
Value12 = yt10559["50-59Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("105年50-59歲前五大出國地", x=0.5, y=1.03)

category = yt10560['Countries']
Value12 = yt10560["60Years and Over"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("105年60歲後五大出國地", x=0.5, y=1.03)
plt.show()

yt10412 = drop104.sort_values(['1-12Years'], ascending=False).head(5)
yt10419 = drop104.sort_values(['13-19Years'], ascending=False).head(5)
yt10429 = drop104.sort_values(['20-29Years'], ascending=False).head(5)
yt10439 = drop104.sort_values(['30-39Years'], ascending=False).head(5)
yt10449 = drop104.sort_values(['40-49Years'], ascending=False).head(5)
yt10459 = drop104.sort_values(['50-59Years'], ascending=False).head(5)
yt10460 = drop104.sort_values(['60Years and Over'], ascending=False).head(5)

category = yt10412['Countries']
Value12 = yt10412["1-12Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("104年1-12歲前五大出國地", x=0.5, y=1.03)

category = yt10429['Countries']
Value12 = yt10429["13-19Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("104年13-19歲前五大出國地", x=0.5, y=1.03)

category = yt10419['Countries']
Value12 = yt10419["20-29Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("104年20-29歲前五大出國地", x=0.5, y=1.03)

category = yt10439['Countries']
Value12 = yt10439["30-39Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("104年30-39歲前五大出國地", x=0.5, y=1.03)

category = yt10449['Countries']
Value12 = yt10449["40-49Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("104年40-49歲前五大出國地", x=0.5, y=1.03)

category = yt10559['Countries']
Value12 = yt10559["50-59Years"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("104年50-59歲前五大出國地", x=0.5, y=1.03)

category = yt10460['Countries']
Value12 = yt10460["60Years and Over"]
plt.figure(figsize=(8,8))
separeted = (0, 0, 0.3, 0, 0)
pictures,category_text,percent_text = plt.pie(Value12,labels = category, autopct = "%0.2f%%", explode = separeted, pctdistance = 0.65, radius = 1, center = (-10,0), shadow=True)
plt.legend(loc = "best")
plt.title("104年60歲後五大出國地", x=0.5, y=1.03)
plt.show()













