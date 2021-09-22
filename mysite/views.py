# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    global params
    djtext = request.POST.get('text', 'default') #Get the text
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    lower = request.POST.get('lower' ,'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(lower=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Change to Lowercase', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(charactercounter=="on"):
        analyzed = ""
        for char in djtext:
            return HttpResponse(len(djtext))
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
    if(removepunc != "on" and fullcaps != "on" and lower!= "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on"):
        return HttpResponse("Please Select any option and try again...")
    return render(request, 'analyze.html', params)

def aboutus(request):
    return render(request, 'aboutus.html')
def Contactus(request):
    return render(request, 'Contactus.html')
