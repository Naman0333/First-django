# import Library
from django.http import HttpResponse
from django.shortcuts import render

#first View
def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcounter','off')

    #check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed =" "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed text in Uppercase','analyzed_text':analyzed}
        djtext = analyzed
    if (newlineremover == "on"):
        analyzed =""
        for char in djtext:
            if char != "\n" and char!='\r':
                analyzed = analyzed + char
        params = {'purpose' :'New Line Remover', 'analyzed_text':analyzed}
        djtext = analyzed
    if (extraspaceremover == 'on'):
        analyzed =""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] ==" "):
                analyzed = analyzed + char
        params = {'purpose' : 'Extra Space Remove','analyzed_text':analyzed}
        djtext = analyzed
    if charcount == 'on':
        analyzed= 0
        for char in djtext:
            analyzed +=1
        params = {'purpose':'Character Count','analyzed_text':analyzed}
    #check any checkbox not on:
    if (removepunc != 'on') and (fullcaps != 'on') and (newlineremover != 'on') and (extraspaceremover != 'on') and (charcount != 'on'):
        return  render(request,'Error.html')
    return render(request,'analyze.html',params)
