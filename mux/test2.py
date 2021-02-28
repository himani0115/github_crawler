import requests
import os
import csv  
import json
import pandas as pd
keyword='ansible'
# s=('https://api.github.com/search/repositories', params={'q':'ansible+language:python-created:>=2016-03-31'})

# print(s)
data = requests.get('https://api.github.com/search/repositories', params={'q':
'comments:500..2000'})
data_json = data.json()
print(data_json)
print(len(data_json['items']))
for i in data_json['items']:
# #     print(len(data_json['items']))
#     # df = pd.DataFrame.from_dict(data_json)
#     # file_name='test111'
#     # df.to_csv(file_name+ '.csv')
#     # df.to_csv(file_name+'.txt')
    # print(i['forks_count']) #org:ansible language:python forks:>120
    # print(i['created_at'])    #org:ansible language:python created:>2018-09-20  
    # print(i['stargazers_count']) #org:ansible language:python stars:>120
    # print(i['pushed_at']) #org:ansible language:python pushed:>2018-12-12
    print(i['full_name'])
    #print(i['repo'])#org:org:ansible or repo:ansible/ansible language:python
