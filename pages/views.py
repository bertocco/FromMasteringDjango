"""
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    # Prima della lezione 6 (=intro dei template)
    #return HttpResponse("<h1>The home page.</h1>")
    # Lezione 6: uso dei template
    return render(request, 'base.html')
"""
# New view for dynamic content:
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from . models import Page

from . forms import ContactForm

def index(request, pagename):
    pagename = '/' + pagename
    #pg = Page.objects.get(permalink=pagename)
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title':pg.title,
        'content':pg.bodytext,
        'last_update':pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)

def contact(request):
    submitted =False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})

