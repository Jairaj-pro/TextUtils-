# I have created this file 
import re
from django import http
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #params = {'name':'Jairaj Singh' , 'place':'India'}
    #return HttpResponse("home <a href='./removepunc'>RemovePunc</a>")
    return render(request, 'index.html')

"""def google(reuqest):
    return HttpResponse("<a href='https://www.google.com/'>google</a>")

def youtube(reuquest):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=1cS_8K74-Lc'>Youtube</a>")

def phub(request):
    return HttpResponse("<a href='www.pornhub.com'>Study Material</a>")"""

def analyze(request):
    returnText = request.GET.get('text','default text')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    charcount=request.GET.get('charcount','off')
    newlineremover = request.GET.get('newlineremover','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if(removepunc=="on"):
        analyzed_text=""
        for i in range(len(returnText)):
            if(returnText[i] not in punctuations):
                analyzed_text+=returnText[i]
        params = {'analyzed_text':analyzed_text}
        return render(request,'analyze.html',params)
    elif(fullcaps=='on'):
        analyzed_text=returnText.upper()
        params = {'analyzed_text':analyzed_text}
        return render(request,'analyze.html',params)
    elif(charcount=='on'):
        length=0
        for i in range(len(returnText)):
            length+=1
        answer='of length '+str(length)
        params={'analyzed_text':answer}
        return render(request,'analyze.html',params)
    elif(newlineremover=='on'):
        analyzed_text=""
        for i in range(len(returnText)):
            if(returnText[i]!='\n'):
                analyzed_text+=returnText[i]
        params={'analyzed_text':analyzed_text}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error")
    # print(returnText)
    # print(removepunc)
    # return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("Cap First")

# def newlineremover(request):
#     return HttpResponse('new line remover')

# def spaceremover(request):
#     return HttpResponse('space remover')

# def charcount(request):
#     return HttpResponse('char count')