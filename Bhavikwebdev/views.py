#This file is created by Bhavik
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text input from user
    djtext = request.POST.get('text','default')
    #Checking checkbox values
    removepunc = request.POST.get('removepunc','off')
    capfulltext = request.POST.get('capfulltext','off')
    newlinerem = request.POST.get('newlinerem','off')
    extraspacerem = request.POST.get('extraspacerem','off')
    # charcount = request.GET.get('charcount','off')

    #Transforming the text on basis of user checks
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose':'Remove punctuations','analyzed_text': analyzed}
        djtext = analyzed
    
    if capfulltext == "on":
        analyzed = djtext.upper()
        params = {'purpose':'Capatilize All Letters','analyzed_text': analyzed}
        djtext = analyzed

    if newlinerem == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char

        params = {'purpose':'Capatilize All Letters','analyzed_text': analyzed}
        djtext = analyzed

    if extraspacerem == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index+1] == " "):
                analyzed += char                

        params = {'purpose':'Capatilize All Letters','analyzed_text': analyzed}
        djtext = analyzed
    
    if not (removepunc =="on" or extraspacerem == "on" or capfulltext =="on" or newlinerem =="on"):
        params = {'purpose':'No Option Selected','analyzed_text': 'Please select any options available to edit your text'}

    return render(request, "analyze.html", params)
