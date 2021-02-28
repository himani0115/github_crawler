import requests
from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render

# Create your views here.

def search_repo(request):
    if request.method == "POST":
        keyword=request.POST['keyword']
    data = requests.get('https://api.github.com/search/repositories', params={'q': keyword + 'language:python'})
    data_json = data.json()
    file_name= 'test11'
    if file_name:
        for i in data_json['items']:
            df = pd.DataFrame.from_dict(data_json['items'])
            df.to_csv(file_name + '.csv')
            df.to_csv(file_name + '.txt')
            print(i['name'])
    return HttpResponse(data_json['items'])
