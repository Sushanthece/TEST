import pandas as pd 

data = pd.read_csv('data_detail_intro_third.csv')

data['Date'] = [('0'+j.split('/')[0]+'-0'+j.split('/')[1]+'-'+j.split('/')[2]  if len(j.split('/')[0])==1 else j.split('/')[0]+'-0'+j.split('/')[1]+'-'+j.split('/')[2] ) if len(j.split('/')[1])==1 else j.split('/')[0]+'-'+j.split('/')[1]+'-'+j.split('/')[2]  for j in data['Date']]


data.to_csv('data_detail_intro_third.csv',index=False)
