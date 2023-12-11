import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb 

def read_data(r):

    df = pd.read_csv(r)
    
    df=df.drop(['2022','Unnamed: 67','Country Code','Indicator Name','Indicator Code'],axis=1)
    
    df=df[['Country Name','1960','1970','1980','1990','2000','2010','2020']]
    
    df_new = df.set_index('Country Name', drop=True)
    
    df_new=df_new.transpose()

    df_new=df_new.reset_index()

    df_country=df_new[['index','Aruba','Africa Eastern and Southern','Afghanistan','Africa Western and Central','Angola']]
    
    df_country.rename(columns={'index': 'Year'}, inplace=True)
    
    return df,df_country

df1,df2=read_data('rating1.csv')

df1.describe

df2.describe

aruba=df2['Aruba'].tolist()

africa_east=df2['Africa Eastern and Southern'].tolist()

afga=df2['Afghanistan'].tolist()

africa_west=df2['Africa Western and Central'].tolist()

angola=df2['Angola'].tolist()

year=df2['Year'].tolist()

country=['Aruba','Africa Eastern and Southern','Afghanistan','Africa Western and Central','Angola']


avg=[]
def avg_rating(df):
    
    df =df.drop(['Year'],axis=1)

    for i in range (len(year)):

        value=np.mean(df.iloc[i].tolist())

        avg.append(value)

    return avg

year_wise=avg_rating(df2)

plt.figure(figsize=(7, 4))

plt.scatter(year, year_wise)

plt.plot(year, year_wise)

plt.title("fertility rate over year")

plt.show()

plt.figure(figsize=(10, 3))

plt.subplot(1,2,1)

plt.plot(year, aruba, label="Aruba")

plt.title('Aruba fertility rate')

plt.subplot(1,2,2)

plt.plot(year,angola, label="Angola")

plt.title('Angola fertility rate')

plt.tight_layout()

plt.show()

plt.figure(figsize=(7, 4))

plt.plot(year, aruba, label="Aruba", linestyle="--")

plt.plot(year,africa_east, label="Africa East", linestyle="--", color="red")

plt.plot(year,afga, label="Afghanistan", linestyle="--")

plt.plot(year,africa_west, label="Africa West", linestyle="--")

plt.plot(year,angola, label="Angola", linestyle="--")

plt.title("fatality rates in different countries")

plt.legend()

plt.show()

dataplot = sb.heatmap(df2.corr(), cmap="YlGnBu", annot=True) 
 
plt.show() 

year_1960=[aruba[0],africa_east[0],afga[0],africa_west[0],angola[0]]

year_1970=[aruba[1],africa_east[1],afga[1],africa_west[1],angola[1]]

year_1980=[aruba[2],africa_east[2],afga[2],africa_west[2],angola[2]]

year_1990=[aruba[3],africa_east[3],afga[3],africa_west[3],angola[3]]

year_2000=[aruba[4],africa_east[4],afga[4],africa_west[4],angola[4]]

year_2010=[aruba[5],africa_east[5],afga[5],africa_west[5],angola[5]]

year_2020=[aruba[6],africa_east[6],afga[6],africa_west[6],angola[6]]

bar_width = 0.1

index = range(len(country))

plt.figure(figsize=(10, 5))

plt.bar(index,year_1960, bar_width, label="1960")

plt.bar([i +bar_width for i in index],year_1970, bar_width, label="1970")

plt.bar([i +2* bar_width for i in index], year_1980, bar_width, label="1980")

plt.bar([i +3* bar_width for i in index],year_1990, bar_width, label="1990")

plt.bar([i +4* bar_width for i in index],year_2000, bar_width, label="2000")

plt.bar([i +5* bar_width for i in index],year_2010, bar_width, label="2010")

plt.bar([i +6* bar_width for i in index],year_2020, bar_width, label="2020")

plt.xlabel("Year")

plt.ylabel("fertility rate")

plt.title("Comparison of Average fertility rate accross different country")

plt.xticks([i + bar_width / 2 for i in index], country, rotation=45)
plt.legend()

plt.tight_layout()

plt.show()
