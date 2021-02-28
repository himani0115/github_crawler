import csv
import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def github_auth(request):
    if request.method == "POST":
        token = request.POST['auth_token']#'6a7e57e12e821ab4540e6fadc5dcdf5876b00ae5'
        user_name = request.POST['username'] #'himani0115'#
        git_session = requests.Session()
        git_session.auth=(user_name, token)
        return HttpResponse(user_name,token)

def read_from_text(request):
    if request.method == "POST":
        repo_url=request.POST['repo_url']
        app_source = repo_url.replace("//github.com", "//api.github.com/repos")
        return HttpResponse(app_source)

def read_from_csv(request):
    file = request.FILES['file']
    decoded_file = file.read().decode('utf-8').splitlines()
    csv_apps = csv.DictReader(decoded_file)
    data=[]
    for row in csv_apps:
        try:
            app_source = row[0].replace("//github.com", "//api.github.com/repos")
            print(app_source, )
            data.append(app_source)
        except:
            pass
    return HttpResponse(data)