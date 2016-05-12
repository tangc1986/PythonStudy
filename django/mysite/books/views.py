from django.shortcuts import render
from books.models import Book

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Enter a search term.')
        elif len(q) > 20:
            error.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                                              {'books': books, 'query': q})            
    return render_to_response('search_form.html', {'errors': error})

#def search(request):
    #if 'q' in request.GET and request.GET['q']:
        #q = request.GET['q']
        #books = Book.objects.filter(title__icontains=q)
        #return render_to_response('search_results.html',
                                  #{'books': books, 'query': q})
    #else:
        ##return HttpResponse('Please submit a search term.')
        #return render_to_response('search_form.html', {'error': True})