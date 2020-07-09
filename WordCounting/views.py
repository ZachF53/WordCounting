from django.http import HttpResponse
from django.shortcuts import render
import operator


def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #Add To Dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords},)