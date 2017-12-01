from django.shortcuts import render

def index(request):
    '''Homepage of learing_logs'''
    return render(request,'learing_logs/index.html')

