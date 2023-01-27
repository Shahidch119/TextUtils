# I have created this file  -Shahid

from django.http import HttpResponse
from django.shortcuts import render


# Code for Video-16
#POST REQUEST in Django

def index(request):
    # params = {'name': 'shahid', 'place': 'Mars'}
    return render(request, 'index.html')


def analyze (request):
    #Get the Text
    djtext = request.POST.get ('text', 'default')

    #Check the Checkbox Values
    removepunc = request.POST.get ('removepunc', 'off')
    fullcaps = request.POST.get ('fullcaps', 'off')
    newlineremover = request.POST.get ('newlineremover', 'off')
    extraspaceremover = request.POST.get ('extraspaceremover', 'off')

    #Check Which Check Box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

            params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        # Analyze the Text
        return render (request, 'analyze.html', params)

        params = {'purpose': 'Remove to UpperCase', 'analyzed_text': analyzed}
        djtext=analyed
        # Analyze the Text
        #return render (request, 'analyze.html', params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper ()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render (request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render (request, 'analyze.html', params)


    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate (djtext):

            if not (djtext [index] == " " and djtext [index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render (request, 'analyze.html', params)

    # else:
    #     return HttpResponse ("Error")

    return render (request, 'analyze.html', params)
