from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, "home.html")

def by_value(el):
    return el[1]

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    count = len(wordlist)

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=by_value, reverse=True)

    return render(request, "count.html", {"fulltext": fulltext, "count": count, "sortedwords": sortedwords})