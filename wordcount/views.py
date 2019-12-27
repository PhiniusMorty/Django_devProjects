# @Date:   2019-10-02T12:00:09+05:30
# @Last modified time: 2019-10-06T16:19:41+05:30
from django.http import HttpResponse
from django.shortcuts import render
import operator

#functions for accepting the request and showing html page.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    #word_count is the format in which the request is being stored
    fulltext = request.GET['Word_count']
    wordlist = fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            #add to worddictionary
            worddictionary[word]=1

        sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'worddictionary':sortedwords})
