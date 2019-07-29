import csv
import pandas as pd
import os
from PIL import Image
import io
import requests
from io import BytesIO
from io import StringIO
from math import log, exp, tan, atan, ceil
from PIL import Image
import sys
import urllib.request
from math import log, exp, tan, atan, pi, ceil
import requests
import matplotlib.pyplot as plt
zoom=16
scale=1
largura, alturaplus=800,800
df=pd.read_csv('us-airportsnew.csv')
names=df['name']

latitude=df['latitude']
longitude=df['longitude']
# print(names,longitude,latitude)
os.chdir("images")
print(type(names.values))
listnames=[]
for i in names.values:
         
 listnames.append(i)
# print(listnames)
df['new'] = df[['latitude', 'longitude']].apply(lambda x: ','.join(x.astype(str)), axis=1)
position=df['new']
# print(df['new'].values[0])
for u in range(len(listnames)):

 for i in df['new'].values:
        #    print(listnames[u])
           urlparams = urllib.parse.urlencode({'center': i,
                                      'zoom': str(zoom),
                                      'size': '%dx%d' % (largura, alturaplus),
                                      'maptype': 'satellite',
                                      'sensor': 'false'
                                     })
  
    
           img = open(listnames[u]+'.png','wb')
        # url = 'https://maps.googleapis.com/maps/api/staticmap?key=API_KEY' + urlparams
           f=requests.get('https://maps.googleapis.com/maps/api/staticmap?'+urlparams+'&key=API_KEY').content
        #    print(f)
           img.write(f)
           img.close()
           
           u += 1
 break
           
