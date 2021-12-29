import requests
from bs4 import BeautifulSoup
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


URL='https://pl.wikipedia.org/wiki/Miasta_w_Polsce'
r = requests.get(URL)
#print(r.content)
if r.status_code==200:
    zupa=BeautifulSoup(r.content,'html.parser')
    #print(zupa.prettify())
    elem=zupa.find('table',{'class':'wikitable'})
    #print(elem)
    df = pd.read_html(str(elem))[0]
    print(df)
    df = df.drop(['Miasto'],axis=1)
    #print(df['szer'].hist())
    print(df)
    df = df.rename(columns={'Miasto':'MIASTO','Województwo':'WOJE'})
    print(df)
    #print(df['WOJE'].hist())


r = TrendReq()
r.build_payload(kw_list=['Zestaw Maty'])
df = r.interest_by_region()
df.reset_index().plot('geoName',y='Zestaw Maty',figsize=(120,4),kind='bar')
#plt.show()
rel = r.related_topics()
rel.values()
print(rel)
df_trendy = r.trending_searches(pn='poland')
print(df_trendy.head(10))
df_trendy = r.today_searches(pn='PL')
print(df_trendy.head(10))
