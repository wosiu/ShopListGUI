from django.shortcuts import render, redirect
from models import *
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def searches(request):
    searchEntries = Search.objects.all()
    template = loader.get_template('searches.html')
    context = {
        'searchEntries': searchEntries,
    }
    return HttpResponse(template.render(context, request))


def offers(request, search_id):
    offerEntries = Offer.objects.filter(search_id__exact=6)
    template = loader.get_template('offers.html')
    context = {
        'offerEntries': offerEntries,
    }
    return HttpResponse(template.render(context, request))


def choose(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    search = Search.objects.get(id=offer.search_id)
    
    return redirect('offers')